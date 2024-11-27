import os
import csv

# Define the directory containing the .wav files and transcripts
TARGET_DIR = "./resemble"

# Define the output CSV file
OUTPUT_CSV = "resemble_starting.csv"

# Create the CSV file and write the header
with open(OUTPUT_CSV, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Audio Clip", "Tag Name", "Original Transcript", "Updated Transcript"])

    # Walk through the target directory
    for root, dirs, files in os.walk(TARGET_DIR):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            wav_files = [f for f in os.listdir(dir_path) if f.endswith('.wav')]
            transcript_path = os.path.join(dir_path, 'transcript.txt')

            # Read the transcript if it exists
            if os.path.exists(transcript_path):
                with open(transcript_path, 'r') as transcript_file:
                    original_transcript = transcript_file.read().strip()
            else:
                original_transcript = ""

            # Write a row for each .wav file
            for wav_file in wav_files:
                audio_clip = f"https://samples.caledon.ai/resemble/{dir_name}/{wav_file}"
                writer.writerow([audio_clip, dir_name, original_transcript, ""])
