from cgitb import text
from random import expovariate
import requests
import re
import string
from bs4 import BeautifulSoup
import time
import webbrowser
from sys import argv
from time import sleep

from origamibot import OrigamiBot as Bot
from origamibot.listener import Listener

print("Bot Start")
#url = requests.get("https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/Procesador-AMD-Ryzen-5-5600-S-AM4-3-50GHz-Six-Core-32MB-L3-Cache-con-Disipador-Wraith-Stealth.html")

#soup = BeautifulSoup(url.content, "html.parser")
#resultado = soup.find("span", {"class": "priceText"})
#precioInicio_text = resultado.text
#precio = re.sub("\$|\,|","", precioInicio_text)
#print("Actual Price: $" + precio)

class BotsCommands:
    def __init__(self, bot: Bot,):  # Can initialize however you like
        self.bot = bot

    def start(self, message):   # /start command
        self.bot.send_message(
            message.chat.id,
            'Hello user!\nThis is a Price Checker for your favorite store\n /url "link" to add the link to the article \n /price "XXXX" to set the expected price')

    def url(self, message, urlGet: str): # /Add url
        global urlView
        urlView = urlGet
        url = requests.get(urlGet)
        soup = BeautifulSoup(url.content, "html.parser")
        resultado = soup.find("span", {"class": "priceText"})
        precioInicio_text = resultado.text
        precio = re.sub("\$|\,|","", precioInicio_text)
        print("Actual Price: $" + precio)
        global precioInit 
        precioInit = float(precio)
        self.bot.send_message(message.chat.id,"Item Saved")

    def price(self, message, price: float): # /Add expected Price
        if precioInit < price:
            self.bot.send_message(message.chat.id,f"Offer, The price downs to:\n {'$ '+str(precioInit)}\nLink: {str(urlView)}")
            print(precioInit)
        else:
            self.bot.send_message(message.chat.id,"No Offer")
            print("No offer")

    def _not_a_command(self):   # This method not considered a command
        print('I am not a command')

if __name__ == '__main__':
    bot_token = '5627768852:AAH5afLkApzk_l3r8NQWqDtaPUkHAMeE-bA' # We can fix the bot token here
    token = (argv[1] if len(argv) > 1 else bot_token)
    bot = Bot(token)   # Create instance of OrigamiBot class

    # Add a command holder
    bot.add_commands(BotsCommands(bot))

    bot.start()   # start bot's threads
    while True:
        sleep(1)
        # Can also do some useful work i main thread
        # Like autoposting to channels for example


