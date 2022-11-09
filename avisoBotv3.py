from cgitb import text
from random import expovariate
from timeit import repeat
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
            'Hello user!\nThis is a Price Checker for your favorite store\n /url "link" to add the link to the article \n /price "XXXX" to set the expected price \n /stock "link" to check stock')

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

    
    def stock(self, message, urlGet: str): # /Add url
        global urlView2
        urlView2 = urlGet
        url2 = requests.get(urlGet)
        soup = BeautifulSoup(url2.content, "html.parser")
        resultado = soup.find("span", {"class": "stockFlag"})
        stockInicio_text = resultado.text
        global stock
        stock = re.sub("\$|\,|","", stockInicio_text)
        print("Actual Stock: " + stock)
        self.bot.send_message(message.chat.id,str(stock))

    def price(self, message, price: float): # /Add expected Price
        global priceE
        priceE = price
        global messageE 
        messageE = message.chat.id
        if precioInit < price:
            self.bot.send_message(message.chat.id,f"Offer, The price downs to:\n {'$ '+str(precioInit)}\nLink: {str(urlView)}")
            print(precioInit)
        else:
            self.bot.send_message(message.chat.id,"No Offer")
            print("No offer")

    def time(self, message, time: float): # /Add Time Check
        global timer
        timer = time
        self.bot.send_message(message.chat.id,f"Time Set on {time} minutes")

    def _not_a_command(self):   # This method not considered a command
        print('I am not a command')


if __name__ == '__main__':
    bot_token = '5715464516:AAHl1iXyOIRsIx9hNcKVHRt1eu5CnYOO06I' # We can fix the bot token here
    token = (argv[1] if len(argv) > 1 else bot_token)
    bot = Bot(token)   # Create instance of OrigamiBot class

    # Add a command holder
    bot.add_commands(BotsCommands(bot))

    bot.start()   # start bot's threads
    while True:
        sleep(1)
        sleep(120)
        if precioInit < priceE and priceE > 0:
            bot.send_message(messageE,f"Offer, The price downs to:\n {'$ '+str(precioInit)}\nLink: {str(urlView)}")
            bot.send_message(messageE,str(stock))
        else:
            bot.send_message(messageE,"No Offer")
        # Can also do some useful work i main thread
        # Like autoposting to channels for example


