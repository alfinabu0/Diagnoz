from google.cloud import speech
import json

client = speech.SpeechClient.from_service_account_file('key.json')

file_name = 'D:/Diagnoz/patient_pre_recorded/p.akash.mp3'

with open(file_name, 'rb') as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)

config = speech.RecognitionConfig(
    sample_rate_hertz = 44100,
    enable_automatic_punctuation = False,
    language_code = 'en-IN'

)


response = client.recognize(
    config=config,
    audio=audio_file
)
 #max audio 60s:
def responseParser():
    for result in response.results:
        print(result.alternatives[0].transcript)

responseParser()