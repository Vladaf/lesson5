import os
import glob
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    PrefixHandler,
    Filters,
)


TOKEN = "1797502466:AAFWqi9q5E2eR78wWocaLDBT2nd93pUDRoE"

HELP = """
Формат комманд с (*): (имя_файла текст)
ПРОБЕЛ МЕЖДУ ИМЕНЕМ ФАЙЛА И ТЕКСТОМ ВАЖЕН!!!

#newFile - создание нового файла или перезапись существующего (*)
#writeFile - дозаписывание файла (*)
#readFile - чтение файла
#delFile - удаление файла

/allFiles - список файлов
"""


def help(bot, context):
    bot.message.reply_text(HELP)

def newFile(bot, context):
    message = bot.message.text[9:]
    k = 0 
    for i in message:
        if i != " ":
            k += 1
        else:
            break
    name = message[:k]
    k += 1
    text = message[k:]
    with open("{}.txt".format(name), "w") as file:
        file.write(text)
    bot.message.reply_text("Файл {} создан/перезаписан!".format(name))

def writeFile(bot, context):
    message = bot.message.text[11:]
    k = 0 
    for i in message:
        if i != " ":
            k += 1
        else:
            break
    name = message[:k]
    k += 1
    text = message[k:]
    with open("{}.txt".format(name), "a") as file:
        file.write(" " + text)
    bot.message.reply_text("Файл {} дозаписан!".format(name))

def readFile(bot, context):
    text = bot.message.text[10:]
    with open("{}.txt".format(text), "r") as file:
        f = file.read()
        bot.message.reply_text(f)

def delFile(bot, context):
    text = bot.message.text[9:]
    os.remove(text + ".txt")
    bot.message.reply_text("Файл {} удалён!".format(text))

def allFiles(bot, context):
    gl = glob.glob('*.txt')
    res = ""
    for i in gl:
        res = res + i + "\n"
    bot.message.reply_text(res)

def run_bot():
    bot = Updater(TOKEN, use_context = True)
    dispatcher = bot.dispatcher
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(PrefixHandler("#", "newFile", newFile))
    dispatcher.add_handler(PrefixHandler("#", "writeFile", writeFile))
    dispatcher.add_handler(PrefixHandler("#", "readFile", readFile))
    dispatcher.add_handler(PrefixHandler("#", "delFile", delFile))
    dispatcher.add_handler(CommandHandler("allFiles", allFiles))
    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    run_bot()