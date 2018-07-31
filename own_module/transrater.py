from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname
import json

userName = 'your user name'
userPassword = 'your password'
speech_to_text = SpeechToTextV1(
    username=userName,
    password=userPassword
)

selectContentType = 'audio/wav'
selectKeyWords = 'DaiGo'
selectModel = 'ja-JP_BroadbandModel'
selectJsonTag1 = 'results'
selectJsonTag2 = 'alternatives'
selectJsonTag3 = 'transcript'
def speechToText(audioName):
    convertTextArray = []
    with open(join(dirname(__file__), './.', audioName),
                   'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type=selectContentType,
            model=selectModel,
            timestamps=True,
            word_alternatives_threshold=0.2,
            keywords=[selectKeyWords],
            keywords_threshold=0.5)
    for i in range(0, len(speech_recognition_results[selectJsonTag1])):
        convertTextArray.append(speech_recognition_results[selectJsonTag1][i][selectJsonTag2][0][selectJsonTag3])

    return convertTextArray
