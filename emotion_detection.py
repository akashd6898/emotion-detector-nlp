import requests
import json

#the url works only in IBM lab, it is not a public API, need to create IBM account and get API key
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def highscore_emotion(json_parsed):
    high_score = 0.0000
    high_emotion = "happy"
    for emotion, score in json_parsed.items():
        if (float(score) > high_score):
            high_score = score
            high_emotion = emotion
    return (high_emotion) #+'='+ str(high_score))

def json_parser(text):
    json_parsed = json.loads(text).get('emotionPredictions')[0].get('emotion')
    print(json_parsed)
    return highscore_emotion(json_parsed)

def emotion_detector(text_to_analyse):
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, headers = headers, json = input_json)
    return json_parser(response.text)

#text1 = "I love this new technology."
#emotions = emotion_detector(text1)
#print(emotions)
  


