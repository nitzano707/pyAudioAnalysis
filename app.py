from flask import Flask, request, jsonify
import os
from pyAudioAnalysis import audioSegmentation as aS

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Speaker Diarization Web App</h1><p>Upload an audio file to start speaker recognition.</p>"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filepath = os.path.join("uploads", file.filename)
        file.save(filepath)
        # שימוש ב-pyAudioAnalysis לזיהוי הדוברים
        try:
            speaker_labels = aS.speaker_diarization(filepath, 2)  # קבע 2 דוברים כמותחל
            return jsonify({"result": speaker_labels.tolist()})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
