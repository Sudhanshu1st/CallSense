# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import assemblyai as aai

# replace with your API token
aai.settings.api_key = f"9218a99d02b744f99c3002035c7cd980"

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

text = transcript.text
text_file_path = r"C:\Users\sudha\My Projects\nlp-sentiment-analysis\data\transcript.txt"

with open(text_file_path, "w", encoding="utf-8") as text_file:
    text_file.write(text)

# Print a confirmation message
print(f"Transcript saved to {text_file_path}")

print(transcript.text)
