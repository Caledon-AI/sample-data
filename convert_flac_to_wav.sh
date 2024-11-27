#!/bin/bash

# Specify the directory containing the .flac files
TARGET_DIR="./resemble"

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg is not installed. Please install it using 'brew install ffmpeg' and try again."
    exit 1
fi

# Find all .flac files in the target directory and convert them to .wav
find "$TARGET_DIR" -type f -name "*.flac" -exec bash -c '
    for file; do
        echo "Converting: $file"
        ffmpeg -i "$file" "${file%.flac}.wav" || echo "Failed to convert $file"
    done
' bash {} +

echo "Conversion process completed."
