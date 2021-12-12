import os

from telegram import Bot
from twilio.rest import Client


def open_barrier(caller_id):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.calls.create(
        to=os.environ['BARRIER_GSM_NUMBER'],
        from_=caller_id,
        twiml='<Response><Say>Contact SET_CONTACT_INFO_HERE for questions.</Say></Response>',
        timeout="15",
        time_limit="5")

    return message.sid


def notify_via_telegram(chat_id, visitor):
    bot = Bot(os.environ['TELEGRAM_BOT_CREDENTIALS'])
    bot.send_message(chat_id=chat_id, text=f'{visitor} just asked to open the barrier')
