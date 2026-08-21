import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "nomic-embed-text",  # bgeM3 model not responding well with the lastest versions of ollama
            "input": text_list
        }
    )

    if r.status_code != 200:
        raise RuntimeError(r.text)

    return r.json()["embeddings"]


jsons = os.listdir("jsons")  # List all the json files
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")

    #  MINIMAL FIX: avoid empty text (prevents NaN)
    embeddings = create_embedding([c.get("text") or " " for c in content["chunks"]])
    # previously tried different method but failed miserably as it was very slow
    # print(content['chunks'])
    # print([c.get("number") or " " for c in content["chunks"]])
    # a=[1,2,3]
    # print([c for c in a])
    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        # print(i)
        # print(chunk)
        # if i==5:
        #     break ## for now i'll read 5 chunks only
    # break # right now i am only 1 file                           ## NOTEE -- embeddings are basically vectors only ## 

df = pd.DataFrame.from_records(my_dicts) # now we created a dataframe from the above dictionary
# print(df)
# now i will save this dataframe using joblib 
joblib.dump(df,'embeddings.joblib') # creates a new file embeddings .jobliob    

# incoming_query=input("ask a question")
# question_embedding=create_embedding([incoming_query])[0]
# # print(question_embedding)
# #  now basically i want to find similarities of question_embeddingwith other embeddings 
# # print(np.vstack(df['embedding'].values)) # now it will make it as a 2D vector
# # print(np.vstack(df['embedding'].shape))
# similarities=cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()   #using np.vstack= 2d vector
# print(similarities)
# top_results=3
# max_indx=similarities.argsort()[::-1][0:top_results] # argsort will show me the index of the maximum values of the embeddings
# print(max_indx)
# new_df=df.loc[max_indx]
# print(new_df[["title","number","text"]])


## Line number 51 till here pulled in the next file proces_incoming.py