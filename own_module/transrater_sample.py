from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname
import json

userName = 'your user name'
userPassword = 'your password'
speech_to_text = SpeechToTextV1(
    username=userName,
    password=userPassword
)

files = ['000_audio.wav']
for file in files:
    with open(join(dirname(__file__), './.', file),
                   'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='ja-JP_BroadbandModel',
            timestamps=True,
            word_alternatives_threshold=0.9,
            keywords=['DaiGo'],
            keywords_threshold=0.5)
    print(speech_recognition_results)
    print()
    print('===')
    print(len(speech_recognition_results['results']))
    print()
    for i in range(0, len(speech_recognition_results['results'])):
        print(speech_recognition_results['results'][i]['alternatives'][0]['transcript'])
