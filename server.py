from flask import Flask, jsonify
from emotion_detection import emotion_detector
app = Flask("Emotion App")

@app.route('/')
def index():
    text1 = "I love this new technology."
    emotions = emotion_detector(text1)
    #return "Hello how are you??"
    return f"The detected emotion is: {emotions}"
    #return jsonify({"text": text1, "emotion": emotions})

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=8080, debug=True)