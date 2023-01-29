import telegram
import responses as R
import asyncio
import constants as keys
from telegram.ext import *


# dispatcher = Application.builder().token(keys.API_KEY).build()


def start(update, context):
    update.message.reply_text("Welcome to the hackathon adviser bot! How can I help you today? Type /help to know more about commands")


def help(update, context):
    update.message.reply_text(
        """
        /start -> welcome to the channel
/help -> displays the reply for each command
/UpcomingHackathonsSchedule -> link of website for hackathons
/HackathonMaterial -> options for techstack

        """
    )

def UpcomingHackathonsSchedule(update, context):
    update.message.reply_text(
        """ Browse upcoming hackathons at : https://devfolio.co/hackathons 
            or
https://unstop.com/hackathons?filters=open&types=oppstatus """
    )
    # Use conversation handler to handle user input and continue scheduling process

def HackathonMaterial(update, context):
    update.message.reply_text(
        """type /AppDev for app development track
type /WebsiteDevelopment for Web dev track
type /TelegramBot for Bot Development track
type /ARfilters for AR filter development track
type /GameDev for Game development track using unity"""
    )

def AppDev(update, context):
    update.message.reply_text("App development playlist using flutter by net ninjas: https://www.youtube.com/watch?v=sfA3NWDBPZ4&list=PL4cUxeGkcC9j--TKIdkb3ISfRbJeJYQwC")

def WebsiteDevelopment(update, context):
    update.message.reply_text("Web development playlist by apna college: https://www.youtube.com/watch?v=l1EssrLxt7E&list=PLfqMhTWNBTe3H6c9OGXb5_6wcc1Mca52n")

def TelegramBot(update, context):
    update.message.reply_text("Basic Telegram Bot development: https://youtu.be/227uk4kDTM8 ")

def ARfilters(update, context):
    update.message.reply_text("AR filter development by GDSC IGDTUW: https://youtu.be/9grxqjXlMS0 ")

def GameDev(update, context):
    update.message.reply_text("Roll a ball game using unity(Following this tutorial one will learn maximum aspects of unity): https://learn.unity.com/project/roll-a-ball")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)
    # Use conversation handler to handle user input and continue scheduling process

# def cancel(update, context):
#     update.message.reply_text("What date is the appointment you would like to cancel?")
#     # Use conversation handler to handle user input and continue cancelling process

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():

    updater = Updater(keys.API_KEY)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text, handle_message)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('UpcomingHackathonsSchedule', UpcomingHackathonsSchedule))
    dispatcher.add_handler(CommandHandler('HackathonMaterial', HackathonMaterial))
    dispatcher.add_handler(CommandHandler('AppDev', AppDev))
    dispatcher.add_handler(CommandHandler('WebsiteDevelopment', WebsiteDevelopment))
    dispatcher.add_handler(CommandHandler('TelegramBot', TelegramBot))
    dispatcher.add_handler(CommandHandler('ARfilters', ARfilters))
    dispatcher.add_handler(CommandHandler('GameDev', GameDev))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
