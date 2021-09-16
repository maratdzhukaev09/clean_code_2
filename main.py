import datetime
import time
def beep(interval = 0.1, frequency = 1000):
    print ("\a", end = "\r")
    time.sleep(interval)

content = '---. . .-.. --- .-- . -.- / .-- / --- .--. .- ... -. --- ... - ..' 
for word in content:
    for symbol in word:
        if symbol == '.':
            beep(interval = 0.1)
        elif symbol == '-':
            beep(interval = 0.7)
        elif symbol == '/':
            time.sleep(1)
azbukaMorze = {'а': '.-',
               'б': '-...',
               'в': '.--',
               'г': '--.',
               'д': '-..',
               'е': '.',
               'ж': '...-',
               'з': '--..',
               'и': '..',
               'й': '.---',
               'к': '-.-',
               'л': '.-..',
               'м': '--',
               'н': '-.',
               'о': '---',
               'п': '.--.',
               'р': '.-.',
               'с': '...',
               'т': '-',
               'у': '..-',
               'ф': '..-.',
               'х': '....',
               'ц': '-.-.',
               'ч': '---.',
               'ш': '----',
               'щ': '--.-',
               'ъ': '.--.-.',
               'ы': '-.--',
               'ь': '-..-',
               'э': '..-..',
               'ю': '..--',
               'я': '.-.-',
               ' ': '/'}

text_additional = {}

name_machine = 'first'
datenow = datetime.datetime.now()
#img_

import requests


url = 'http://195.161.114.75:8080'

def check_communication(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')    

check_communication(url)
