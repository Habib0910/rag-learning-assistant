## CONVERT ALL videos to mp3
# import os 
# import subprocess

# files = os.listdir("videos") 
# for file in files: 
#     print(file)
#     tutorial_number = file.split("-")[0].split("#")[1]
#     print(tutorial_number)
#     file_name = file.split(" ｜ ")[0]
#     print( tutorial_number,  file_name)
#     subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
    
    
    
# import os #connects your code to operating system  ## basically the osmodule lets your code to ....create folders; delete files; list files;check paths etc.
# import subprocess  #module that allows your Python program to run other programs on your computer.  eg-Running ffmpeg etc..

# files = os.listdir("videos")

# for file in files:
#     print(file)

#     # FIX 1: tutorial # is always AFTER the "-" part
#     tutorial_part = file.split("-")[1]          # " Tutorial #3.mp4"
#     tutorial_number = tutorial_part.split("#")[1].split(".")[0]   # "3"
#     print(tutorial_number)

#     # FIX 2: do NOT use " ｜ ", get filename without extension
#     file_name = file.rsplit(".", 1)[0]          # remove .mp4
#     print(tutorial_number, file_name)

#     subprocess.run([
#         "ffmpeg",
#         "-i", f"videos/{file}",
#         f"audios/{tutorial_number}_{file_name}.mp3"
#     ])


import os
import subprocess 

files = os.listdir("videos")

sample_created = False  # <-- flag to create only one sample.mp3

for file in files:
    print(file)

    tutorial_part = file.split("-")[1]          
    tutorial_number = tutorial_part.split("#")[1].split(".")[0]
    print(tutorial_number)

    file_name = file.rsplit(".", 1)[0]          
    print(tutorial_number, file_name)

    # Full audio conversion (same as before)
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", f"videos/{file}",
        f"audios/{tutorial_number}_{file_name}.mp3"
    ])

    # -----------------------------------------------------
    # CREATE ONLY ONE sample.mp3 (first time only)
    # -----------------------------------------------------
    if not sample_created:
        subprocess.run([
            "ffmpeg",
            "-y",
            "-i", f"videos/{file}",
            "-t", "10",              # take only first 10 seconds
            "audios/sample.mp3"      # one single output file
        ])
        sample_created = True        # prevent more samples

