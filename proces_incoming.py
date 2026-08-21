import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import joblib 
import requests


# def create_embedding(text_list):
#     # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings  tghis model fails bge--m3
#     r = requests.post("http://localhost:11434/api/embed", json={
#         "model": "bge-m3",
#         "input": text_list
#     })

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "nomic-embed-text",  # bgeM3 model not responding well with the lastest versions of ollama
            "input": text_list
        }
    )

    embedding = r.json()["embeddings"] 
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        # "model": "deepseek-r1",
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False 
    })
    response = r.json() # converting the http request to python dictionary and returning as a json
    print(response)
    return response


df = joblib.load('embeddings.joblib')


incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0] 

# Find similarities of question_embedding with other embeddings
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding']).shape)
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
# print(similarities)
top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results]
# print(max_indx)
new_df = df.loc[max_indx] 
# print(new_df[["title", "number", "text"]])
# .to json helps to converrt pandas dataframe into json

prompt=f'''i am teaching web development course from sigma web development course. Here arw the video subtitle
chunks containing the video title,video number ,start time in seconds,end time in seconds, the text at 
that time.
{new_df[["title", "number", "start","end","text"]].to_json(orient="records")} 

---------------
"{incoming_query}"
user asked this question related to the video chunks, you have to answer where and how much content is taught 
in  which video(in which video and at what timestamp in seconds and minutes) and then guide the user to go to that particular video
. If user asks unrelated questions , tell him that you can only answer questions related to the course in a human
form'''

with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)  





# for index,item in new_df.iterrows():
#     print(index,item['title'],item['number'],item['text'],item['start'],item['end'])