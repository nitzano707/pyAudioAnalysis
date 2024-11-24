from flask import Flask, request, jsonify
from pyAudioAnalysis import audioSegmentation as aS

app = Flask(__name__)

@app.route('/diarize', methods=['POST'])
def diarize():
    # קבל קובץ אודיו מבקשת POST
    audio_file = request.files['file']
    audio_file.save("uploaded_audio.wav")

    # הפעל Speaker Diarization
    segmentation = aS.speakerDiarization("uploaded_audio.wav", n_speakers=2)

    return jsonify({"segmentation": segmentation.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
