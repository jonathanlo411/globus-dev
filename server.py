from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
import globus_sdk

# === Server Setup ---
load_dotenv()
CLIENT_ID = os.getenv('ClientID')
CLIENT_SECRET = os.getenv('ClientSecret')
client = globus_sdk.NativeAppAuthClient(CLIENT_ID)
app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

# --- API ---

@app.route('/api/auth')
def auth():
    client.oauth2_start_flow()
    authorize_url = client.oauth2_get_authorize_url()
    return {
        "auth_url": authorize_url
    }, 200
# def auth():
#     client.oauth2_start_flow()
#     authorize_url = client.oauth2_get_authorize_url()
#     return {
#         "auth_url": authorize_url
#     }, 200

@app.route("/api/search")
def search():
    return {
        "ok": 1
    }, 200