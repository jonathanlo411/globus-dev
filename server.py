from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

# === Server Setup ---
load_dotenv()
CLIENT_ID = os.getenv('ClientID')
CLIENT_SECRET = os.getenv('ClientSecret')
app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

# --- API ---

@app.route('/api/auth')
def auth():
    res = requests.post(f'https://auth.globus.org/v2/oauth2/authorize?response_type=code&client_id={CLIENT_ID}')
    data = res.text
    print(data, flush=True)
    return {
        "ok": 1
    }, 200

@app.route("/api/search")
def search():
    return {
        "ok": 1
    }, 200