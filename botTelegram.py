import requests
import re
import telebot
import time
import pyautogui
from threading import Thread


def printScrenTelegram():
    chatId = ''  # пока не поставлю сервак
    botToken = ''
    bot = telebot.TeleBot(botToken)
    while True:
        # screen = pyautogui.screenshot('screenshot.png')
        bot.send_photo(chatId, pyautogui.screenshot())
        sleep(600)
    bot.polling()


th = Thread(target=printScrenTelegram)
th.start()


# Считывание сообщений из телеграма
def checkOutTelegram():
    chatId = ''
    botToken = ''
    print('Start')
    bot = telebot.TeleBot(botToken)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        print(message.text)
        case = message.text.split()
        # Отправка скрина в телегу
        if (case[0] == "Skrin"):
            botToken = ''
            bot = telebot.TeleBot(botToken)
            bot.send_photo(chatId, pyautogui.screenshot())
        # Запуск нового окна
        if (case[0].isnumeric() and case[1].isnumeric()):
            startCSGO(case)
        # txt открытых окон
        if (case[0] == "HelpDelite"):
            HelpDelite()
        # Закрытие аккаунта
        if (case[0] == "delite" and case[1].isnumeric()):
            logDeliteAkkSteam(case)

    bot.polling(none_stop=True, interval=0)


th = Thread(target=checkOutTelegram)
th.start()
