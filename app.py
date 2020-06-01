from flask import Flask, request
from slack import WebClient
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config.from_pyfile('./conf/slack-project-conf.py')
db = SQLAlchemy(app)

from db import Message

@app.route('/bot/message')
def sendMesage():
    messageToSend = request.args.get("message")

    client = WebClient(token=app.config['SLACK_KEY'])
    try:
        #send message to slack
        response = client.chat_postMessage(
            channel='#general',
            text=messageToSend)
        assert response["message"]["text"] == messageToSend

        #save message to database
        messageClass = Message(message=messageToSend,
                               created_on=datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        db.session.add(messageClass)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500
    return '', 204



@app.route('/bot/list/message')
def getMessages():
    try:
        query = Message.query.all()
        print(query[0])
        print(query)
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500
    return '', 204




if __name__ == '__main__':
    app.run()
