from telegram.ext import Updater, CommandHandler
from tkn import TOKEN
from process_input_and_output import *
from basic_operations import write_pid

# cet - get random quote
# lib - get random extract


def start(update, context):
    text = "Why then here does any one step forth? - Because one did survive the wreck."
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=text)


def description(update, context):
    reply = "*Commands:* \n\n" \
            "/cet - quote random paragraph\n" \
            "/cet x - to avoid spoilers, specify integer 1 <= x <= %d " \
            "so that the random quote comes from chapters [1, x]\n" \
            "/lib - quote random extract from chapter Extracts\n" \
            "/lev x y - get paragraph with index y from chapter x" % LAST_NUM

    chat_id = update.message.chat_id
    context.send_message(chat_id=chat_id, text=reply)


def cet(update, context):
    # /cet 75
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    print('split:', query)
    if len(query) == 1:
        reply = process_input_for_cet(LAST_NUM)
    elif len(query) == 2:
        reply = process_input_for_cet(query[1])
    else:
        reply = INVALID_INPUT
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=reply)


def lib(update, context):
    # /lib
    query = update['message']['text']
    print('query:', query)
    reply = process_input_for_lib()
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=reply)


def lev(update, context):
    # /lev 31 1
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    print('split:', query)
    if len(query) == 3:
        reply = process_input_for_lev(query[1], query[2])
    else:
        reply = INVALID_INPUT
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=reply)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', description)
    cet_handler = CommandHandler('cet', cet)
    lib_handler = CommandHandler('lib', lib)
    lev_handler = CommandHandler('lev', lev)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(cet_handler)
    dispatcher.add_handler(lib_handler)
    dispatcher.add_handler(lev_handler)

    updater.start_polling()


if __name__ == '__main__':
    write_pid()
    main()
