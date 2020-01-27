import re

def karma(message):
    count = 0
    chat_id = message.chat.id
    user = message.reply_to_message.from_user
    username = 'doe'
    if user.username != '':
        username = user.username
    else:
        username = user.first_name + " " + user.last_name

    return 'Поднял карму {} до {}!'.format(username, count)
