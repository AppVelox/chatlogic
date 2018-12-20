from flask import Flask, request
from chatlogic import LogicClient, message

app = Flask(__name__)
client = LogicClient('<YOUR_URL>')


@client.add_handler(type='text')
def text_handler(incoming):
    msg = message.Message(incoming.text)
    client.send_message(msg, incoming.user_id, incoming.platform)


@app.route('/incoming')
def incoming():
    if request.json:
        client.process_json(request.json)
    return ''
