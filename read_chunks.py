import requests
import os
import json
 
def create_embedding(text_list):
    r= requests.post('http://localhost:11434/api/embed',json={
        'model':'bge-m3',  #3 we are using the bge m3 model to create embeddings
        "input":text_list
    })
    embedding = r.json()["embeddings"]
    # print(embedding[0:5])## basicallty wew are taking the weights of the first five dimensions
    return(embedding)

# a=create_embeddings('cat sat on the mat')
# print(a)
jsons=os.listdir("jsons") # list of all jsons
my_dicts=[] 
chunk_id=0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content=json.load(f)
    embeddings=create_embedding([c['text']for c in content['chunks']])
        
    for i,chunk in enumerate (content['chunks']):# basically enumurate function gives us the index and the iterable
        chunk['chunk_id']=chunk_id
        chunk['embedding']= embeddings[i]
        chunk_id+=1
        my_dicts.append(chunk)
    
    break
# print(my_dicts)









