from flask import Flask
from training.train import train_model
import os

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return 'alive'

@app.route("/train", methods = ["GET"])
def train():
    train_model()
    return 'training ok'

@app.route("/predict", methods = ["POST"])
def predict():
    
    return 'prediction ok'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host = "0.0.0.0", port = port , threaded = True, debug = True)