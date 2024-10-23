from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)

# Simulate a threat database with a few example hashes (MD5)
malicious_hashes = [
    "d41d8cd98f00b204e9800998ecf8427e",  # Example of a malicious hash
]

@app.route('/')
def index():
    return "Threat Detection Backend Running"

@app.route('/detect', methods=['POST'])
def detect_threat():
    input_data = request.form.get('inputData')
    file = request.files.get('file')

    # Check URL threat (simple string matching for this example)
    if input_data:
        if "malicious" in input_data:
            return jsonify({'type': 'danger', 'message': 'URL detected as malicious!'})

    # Check file threat (hash comparison)
    if file:
        file_content = file.read()
        file_hash = hashlib.md5(file_content).hexdigest()

        if file_hash in malicious_hashes:
            return jsonify({'type': 'danger', 'message': 'File detected as malicious!'})

    return jsonify({'type': 'success', 'message': 'No threat detected!'})

if __name__ == "__main__":
    app.run(debug=True)
