from flask import Flask, request, jsonify
from slack import WebClient
from flask_sqlalchemy import SQLAlchemy
import datetime
from db import Message

application = Flask(__name__)
application.config.from_pyfile('./conf/slack-project-conf.py')
db = SQLAlchemy(application)
application.debug = True

@application.route('/bot/message', methods=['POST'])
def sendMesage():
    messageToSend = request.args.get("message")

    client = WebClient(token=application.config['SLACK_KEY'])
    try:
        # send message to slack
        response = client.chat_postMessage(
            channel=application.config['SLACK_CHANNEL'],
            text=messageToSend)
        assert response["message"]["text"] == messageToSend

        # save message to database
        messageClass = Message(message=messageToSend,
                               created_on=datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
        db.session.add(messageClass)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500
    return '', 204


@application.route('/bot/list/message', methods=['GET'])
def getMessages():
    try:
        rows = Message.query.order_by(Message.created_on.desc())
        records = [row.to_json() for row in rows]
        return jsonify(records), 200
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500

@application.route('/')
def test():
    return '', 204

if __name__ == '__main__':
    application.run(host='0.0.0.0')
