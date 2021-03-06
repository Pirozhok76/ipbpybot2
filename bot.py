import os
import logging

from parse import parse
from karma import karma
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hello.')


def help(update, context):
    update.message.reply_text('Create an Issue if you want (https://github.com/nullawhale/ipbpybot2)')


def echo(update, context):
    if update.message.text == '++' or update.message.text == '--':
        update.message.reply_text(karma(update.message))
    else:    
        update.message.reply_text(parse(update.message.text))



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
