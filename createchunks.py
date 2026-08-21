# import whisper
# import json
# import os

# model = whisper.load_model("large-v2")
# audios = os.listdir("audios")
# for audio in audios:
#     if('_'in audio):
#         number=audio.split('_')[0]
#         title=audio .split('_')[1][:-4]
#         print(number,title)
        
         
# # result = model.transcribe(audio = "audios/sample.mp3", 
# result = model.transcribe(audio = f"audios/{audio}",

#                           language="hi",
#                           task="translate",
#                            word_timestamps=False )

 
# chunks = []
# for segment in result["segments"]:
#     chunks.append({"number": number,"title":title,"start": segment["start"], "end": segment["end"], "text": segment["text"]})
#     chunks_with_metadata = {"chunks":chunks,"text":result["text"]}

# # print(chunks)

# with open(f"jsons/{audio}.json", "w") as f:
#     json.dump(chunks_with_metadata,f) 
# print("habib")  

import whisper
import json
import os

model = whisper.load_model("large-v2")  # do not use turbo model if u want to do the task of transcribtion ...use large v2 this performs best

audios = os.listdir("audios")

for audio in audios: 
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}", 
        # result = model.transcribe(audio = f"audios/sample.mp3", 
                              language="hi", # basically tells whisper that spoken lang is hindi
                              task="translate", # not transcribe
                              word_timestamps=False ) # here false means timestam,ps per sentence or segments 
        # print(result)        
        chunks = []
        for segment in result["segments"]:
            print(segment)

            chunks.append({"number": number, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata,f)
            