from cgitb import text
import requests
from WebScaping import precioInicial
from WebScaping import precioDeseado

import requests

def telegram_bot_sendtext(bot_message):

    bot_token = '5627768852:AAH5afLkApzk_l3r8NQWqDtaPUkHAMeE-bA'
    bot_chatID = '600556'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


if precioInicial < precioDeseado:
    test =  telegram_bot_sendtext(f"Oferta, bajo el precio a: {'$ '+str(precioInicial)}\nEnlace: https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/Procesador-AMD-Ryzen-5-5600-S-AM4-3-50GHz-Six-Core-32MB-L3-Cache-con-Disipador-Wraith-Stealth.html")

else:
    test = telegram_bot_sendtext("No Oferta")

