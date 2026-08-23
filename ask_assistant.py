import requests
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity


def create_embedding(text):
    response = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "nomic-embed-text",
            "input": [text]
        }
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["embeddings"][0]


def generate_response(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["response"]


# Load the pre-generated transcript embeddings
df = joblib.load("embeddings.joblib")

# Get the user's question
incoming_query = input("Ask a Question: ")

# Convert the question into an embedding
question_embedding = create_embedding(incoming_query)

# Compare the question with all stored transcript embeddings
similarities = cosine_similarity(
    np.vstack(df["embedding"]),
    [question_embedding]
).flatten()

# Select the five most relevant transcript chunks
top_results = 5
top_indices = similarities.argsort()[::-1][:top_results]

relevant_chunks = df.loc[top_indices]

# Build the prompt using the retrieved transcript chunks
prompt = f"""
You are a learning assistant for a web development course.

The following are transcript chunks retrieved from the course.
Each chunk contains the video title, video number, start time,
end time, and transcript text.

Retrieved course chunks:
{relevant_chunks[["title", "number", "start", "end", "text"]].to_json(orient="records")}

User question:
"{incoming_query}"

Instructions:
- Answer only questions related to the web development course.
- Identify which video contains the relevant information.
- Provide the relevant timestamp in seconds and minutes.
- Explain briefly what is taught at that point.
- Guide the user to the relevant video.
- If the question is unrelated to the course, politely explain that
  you can only answer questions related to the course.
"""

# Save the generated prompt for debugging and inspection
with open("prompt.txt", "w") as f:
    f.write(prompt)

# Generate the final answer
response = generate_response(prompt)

print(response)

# Save the response for inspection
with open("response.txt", "w") as f:
    f.write(response)