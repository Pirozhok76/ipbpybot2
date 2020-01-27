import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hello.')


def help(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    if update.message.text == 'Саша':
        update.message.reply_text('Александр')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    token = os.environ['TELEGRAM_TOKEN']
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
