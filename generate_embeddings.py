import requests
import os
import json
import pandas as pd
import joblib


def create_embedding(text_list):
    response = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "nomic-embed-text",
            "input": text_list
        }
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["embeddings"]


json_files = os.listdir("jsons")

all_chunks = []
chunk_id = 0

for json_file in json_files:

    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    print(f"Creating embeddings for {json_file}")

    texts = [
        chunk.get("text") or " "
        for chunk in content["chunks"]
    ]

    embeddings = create_embedding(texts)

    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]

        chunk_id += 1
        all_chunks.append(chunk)


# Store chunks and embeddings in a DataFrame
df = pd.DataFrame.from_records(all_chunks)

# Save the embeddings for the retrieval stage
joblib.dump(df, "embeddings.joblib")

print(f"Created embeddings for {len(df)} chunks.")