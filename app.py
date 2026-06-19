from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8796123537:AAFIXzE_e9y-42Bj07suMndDZC76AnTuym0"
CHAT_ID = "8852013357"

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    text = data["text"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
