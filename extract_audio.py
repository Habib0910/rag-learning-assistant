
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

    # Full audio conversion 
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

