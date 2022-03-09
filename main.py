from multiprocessing.reduction import steal_handle
from numpy import char
import requests
import folium
import telebot

bot = telebot.TeleBot('secret')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "Введи ip-адрес")

@bot.message_handler(content_types='text')
def handle_text(message): 
    if message.text == "32.22.2.5":
        getInfoIP(message.text)
        bot.send_message(message.chat.id, "uwu")
    else:
        bot.send_message(message.chat.id, "UWU")
  

def getInfoIP(message):
        adres = requests.get('http://ip-api.com/json/' + message).json()

        # data = {
        #     '[IP]': adres.get('query'),
        #     '[Int prov]': adres.get('isp'),
        #     '[Org]': adres.get('org'),
        #     '[Country]': adres.get('country'),
        #     '[Region Name]': adres.get('regionName'),
        #     '[Cuty]': adres.get('city'),
        #     '[ZIP]': adres.get('zip'),
        #     '[Lat]': adres.get('lat'),
        #     '[Lon]': adres.get('lon'),
        # }

        # for k,v in data.items():
        #     print(f'{k} : {v}')
        
        area = folium.Map(location=[adres.get('lat'), adres.get('lon')])
        area.save(f'{adres.get("query")}.html')
        with open("32.22.2.5.html","rb") as f:
            bot.send_document(f)    

# def main():
#     while True:
#         message = input()
#         start_message(message)


bot.polling(none_stop=True, interval=0)

# if __name__ == '__main__':
#      main()