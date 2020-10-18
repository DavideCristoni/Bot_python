import telepot
import time
import json
import urllib
import requests


#initialating bot 
token ='1249142248:AAFAyKZQpOuuGHFVr9OHfe_FZuQJLXeg3m4'
bot = telepot.Bot(token)

    
#chat response
step =1
def on_chat_message(msg):
    global step
    content_type, chat_type, chat_id = telepot.glance(msg)
    name = msg["from"]["first_name"]
    txt = msg['text']
    print(txt)
    if step == 1 and txt == '/help':  
        bot.sendMessage(chat_id,'Ciao {}, le mie funzionalità sono : ' .format(name))
        bot.sendMessage(chat_id,'/myip - shows the public ip of the user')
        bot.sendMessage(chat_id,'/getinfo - user info')
        bot.sendMessage(chat_id,'/weather - get weather in Bologna ')
    elif  step == 1 and txt == '/myip':
        link = "http://ip.42.pl/raw"
        ip = urllib.request.urlopen(link).read()
        bot.sendMessage(chat_id, ip)
    elif  step == 1 and txt == '/getinfo':
        info = json.dumps(bot.getUpdates(),sort_keys=True, indent=4) #get delle info e tramite json.dump 
        bot.sendMessage(chat_id,info)
    elif step == 1 and txt == '/weather':
        bot.sendMessage(chat_id,'Now enter the town like Bologna or Roma')
        step = 2
    elif step == 2 : 
        content_type, chat_type, chat_id = telepot.glance(msg)
        town = msg['text']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c0968cc770af6fa1b88465560036d1e1&lang=it'.format(town)
        response = requests.get(url)
        data = response.json()
        formatted_data = data.values()
        arr = []
        for x in formatted_data:
            arr.append(x)        
        bot.sendMessage(chat_id,'Town : {}'.format(arr[11]))
        bot.sendMessage(chat_id,'Weather : {}'.format(arr[1][0]['description']))
        bot.sendMessage(chat_id,'Temperature : {}'.format(arr[3]['temp']))
        bot.sendMessage(chat_id,'Pressure : {} '.format(arr[3]['pressure']))
        step = 1
         
          

def Main():
    bot.message_loop(on_chat_message)
    while 1:
        time.sleep(10)

Main()
