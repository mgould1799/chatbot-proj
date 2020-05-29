from flask import Flask, request, make_response
from slack import WebClient
from slack.errors import SlackApiError
import json

app = Flask(__name__)
app.config.from_pyfile('./conf/slack-project-conf.py')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    name = request.args.get("name")
    return 'Hello, ' + str(name)

@app.route('/bot/message')
def sendMesage():
    message = request.args.get("message")

    client = WebClient(token=app.config['SLACK_KEY'])
    try:
        response = client.chat_postMessage(
            channel='#general',
            text=message)
        assert response["message"]["text"] == message
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
    return '', 204

if __name__ == '__main__':
    app.run()
