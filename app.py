from flask import Flask, request, make_response
from slack import WebClient
from slack.errors import SlackApiError
from flask_sqlalchemy import SQLAlchemy
import time


import json

app = Flask(__name__)
app.config.from_pyfile('./conf/slack-project-conf.py')
db = SQLAlchemy(app)

from db import Message

@app.route('/bot/message')
def sendMesage():
    messageToSend = request.args.get("message")

    client = WebClient(token=app.config['SLACK_KEY'])
    try:
        # response = client.chat_postMessage(
        #     channel='#general',
        #     text=messageToSend)
        # assert response["message"]["text"] == messageToSend
        messageClass = Message(message=messageToSend, created_on=time.time())
        db.session.add(messageClass)
        db.session.commit()
        print("message added to database")
    except Exception as e:
        # You will get a SlackApiError if "ok" is False
        print(e)
        # assert e.response["ok"] is False
        # assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        # print(f"Got an error: {e.response['error']}")
    return '', 204


# def StoreMessageDB(message, timestamp):




if __name__ == '__main__':
    app.run()
