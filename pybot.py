from flask import Flask, request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])

def bot():

    user_msg = request.values.get('Body', '').lower()

    response = MessagingResponse()

    q = user_msg

    results = []

    for i in search(q, num_results=3):
        results.append(i)

    msg = response.message(f"--- Results for '{user_msg}' ---")
    for result in results:
        msg = response.message(result)

    return str(response)

if __name__ == "__main__":
    app.run()
