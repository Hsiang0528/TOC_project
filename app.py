import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

# import pygraphviz
from transitions.extensions import GraphMachine

load_dotenv()


machine = TocMachine(
    states=["user", "pet", "pet2","fortune", "fortune2","user_1", "graph","start", "I","E","IN","IS","EN","ES","INT","IST","ENT","EST","INF","ISF","ENF","ESF","INTJ","ISTJ","ENTJ","ESTJ","INFJ","ISFJ","ENFJ","ESFJ","INTP","ISTP","ENTP","ESTP","INFP","ISFP","ENFP","ESFP"],
    transitions=[
        # # 寵物
        # {
        #     "trigger": "advance",
        #     "source": "user",
        #     "dest": "pet",
        #     "conditions": "user_to_pet",
        # },
        # {
        #     "trigger": "advance",
        #     "source": "pet",
        #     "dest": "pet2",
        #     "conditions": "pet_to_pet2",
        # },
        # {
        #     "trigger": "pet2_to_user",
        #     "source": "pet2",
        #     "dest": "user",
        # },
        # 運勢
        {
            "trigger": "advance",
            "source": "user",
            "dest": "fortune",
            "conditions": "user_to_fortune",
        },
        {
            "trigger": "advance",
            "source": "fortune",
            "dest": "fortune2",
            "conditions": "fortune_to_fortune2",
        },
        {
            "trigger": "fortune2_to_user",
            "source": "fortune2",
            "dest": "user",
        },
        # FSM圖
        {
            "trigger": "advance",
            "source": "user",
            "dest": "graph",
            "conditions": "user_to_graph",
        },
        {
            "trigger": "back",
            "source": "graph",
            "dest": "user",
        },
        # 心理測驗
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "user_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "I",
            "conditions": "start_to_I",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "E",
            "conditions": "start_to_E",
        },
        {
            "trigger": "advance",
            "source": "I",
            "dest": "IN",
            "conditions": "I_to_IN",
        },
        {
            "trigger": "advance",
            "source": "I",
            "dest": "IS",
            "conditions": "I_to_IS",
        },
        {
            "trigger": "advance",
            "source": "E",
            "dest": "EN",
            "conditions": "E_to_EN",
        },
        {
            "trigger": "advance",
            "source": "E",
            "dest": "ES",
            "conditions": "E_to_ES",
        },
        {
            "trigger": "advance",
            "source": "IN",
            "dest": "INT",
            "conditions": "IN_to_INT",
        },
        {
            "trigger": "advance",
            "source": "IS",
            "dest": "IST",
            "conditions": "IS_to_IST",
        },
        {
            "trigger": "advance",
            "source": "EN",
            "dest": "ENT",
            "conditions": "EN_to_ENT",
        },
        {
            "trigger": "advance",
            "source": "ES",
            "dest": "EST",
            "conditions": "ES_to_EST",
        },
        {
            "trigger": "advance",
            "source": "IN",
            "dest": "INF",
            "conditions": "IN_to_INF",
        },
        {
            "trigger": "advance",
            "source": "IS",
            "dest": "ISF",
            "conditions": "IS_to_ISF",
        },
        {
            "trigger": "advance",
            "source": "EN",
            "dest": "ENF",
            "conditions": "EN_to_ENF",
        },
        {
            "trigger": "advance",
            "source": "ES",
            "dest": "ESF",
            "conditions": "ES_to_ESF",
        },
        {
            "trigger": "advance",
            "source": "INT",
            "dest": "INTJ",
            "conditions": "INT_to_INTJ",
        },
        {
            "trigger": "advance",
            "source": "IST",
            "dest": "ISTJ",
            "conditions": "IST_to_ISTJ",
        },
        {
            "trigger": "advance",
            "source": "ENT",
            "dest": "ENTJ",
            "conditions": "ENT_to_ENTJ",
        },
        {
            "trigger": "advance",
            "source": "EST",
            "dest": "ESTJ",
            "conditions": "EST_to_ESTJ",
        },
        {
            "trigger": "advance",
            "source": "INF",
            "dest": "INFJ",
            "conditions": "INF_to_INFJ",
        },
        {
            "trigger": "advance",
            "source": "ISF",
            "dest": "ISFJ",
            "conditions": "ISF_to_ISFJ",
        },
        {
            "trigger": "advance",
            "source": "ENF",
            "dest": "ENFJ",
            "conditions": "ENF_to_ENFJ",
        },
        {
            "trigger": "advance",
            "source": "ESF",
            "dest": "ESFJ",
            "conditions": "ESF_to_ESFJ",
        },
        {
            "trigger": "advance",
            "source": "INT",
            "dest": "INTP",
            "conditions": "INT_to_INTP",
        },
        {
            "trigger": "advance",
            "source": "IST",
            "dest": "ISTP",
            "conditions": "IST_to_ISTP",
        },
        {
            "trigger": "advance",
            "source": "ENT",
            "dest": "ENTP",
            "conditions": "ENT_to_ENTP",
        },
        {
            "trigger": "advance",
            "source": "EST",
            "dest": "ESTP",
            "conditions": "EST_to_ESTP",
        },
        {
            "trigger": "advance",
            "source": "INF",
            "dest": "INFP",
            "conditions": "INF_to_INFP",
        },
        {
            "trigger": "advance",
            "source": "ISF",
            "dest": "ISFP",
            "conditions": "ISF_to_ISFP",
        },
        {
            "trigger": "advance",
            "source": "ENF",
            "dest": "ENFP",
            "conditions": "ENF_to_ENFP",
        },
        {
            "trigger": "advance",
            "source": "ESF",
            "dest": "ESFP",
            "conditions": "ESF_to_ESFP",
        },
        {
            "trigger": "ans_to_user",
            "source": ["INTJ","ISTJ","ENTJ","ESTJ","INFJ","ISFJ","ENFJ","ESFJ","INTP","ISTP","ENTP","ESTP","INFP","ISFP","ENFP","ESFP"],
            "dest": "user",
        },
        {
            "trigger": "advance",
            "source": ["start", "I","E","IN","IS","EN","ES","INT","IST","ENT","EST","INF","ISF","ENF","ESF","INTJ","ISTJ","ENTJ","ESTJ","INFJ","ISFJ","ENFJ","ESFJ","INTP","ISTP","ENTP","ESTP","INFP","ISFP","ENFP","ESFP"],
            "dest": "user_1",
            "conditions": "go_to_user_1",
        },
        {
            "trigger": "uu",
            "source": "user_1",
            "dest": "user",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

#
# 

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if machine.state == "user" :
                send_text_message(event.reply_token, "Please type \"START\" to start 心理測驗.\nPlesae type \"FORTUNE\" to start 今日星座運勢\nYou can type\"RESTART\" to restart anytime !")
            else :
                send_text_message(event.reply_token, "Please type valid answer !")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
