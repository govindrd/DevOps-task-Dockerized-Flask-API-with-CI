from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

PORT = os.getenv("PORT")
if not PORT:
    raise Exception("PORT environment variable not set")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

@app.route("/", methods=["GET"])
def home():
    app.logger.info("Home endpoint called")
    return jsonify(message="API is running")

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    app.logger.info(f"Echo called with data: {data}")
    return jsonify(received=data)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))
