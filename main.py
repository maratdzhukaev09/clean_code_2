import requests
import time
def gudok (i = 0.1, chastota = 1000):
    print ("\a", end = "\r")
    time.sleep (i)

content = '---. . .-.. --- .-- . -.- / .-- / --- .--. .- ... -. --- ... - ..' 

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






adres = 'http://192.168.24.173:8080'

def communication(adres):
    response = requests.get(adres)
    if response.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')    

#communication(adres)
# for word in content:
#     for symbol in word:
#         if symbol == '.':
#             gudok(i = 0.1)
#         elif symbol == '-':
#             gudok(i = 0.7)
#         elif symbol == '/':
#             time.sleep(1)


def robot(adres, m):
    response = requests.post(adres,m)
    if response.status_code == 200:
        print('Команда принята')
        print('Бегу к вам!')
    else:
        print('Команда не принята! Продолжаю выполнять прежнюю инструкцию.')
robot(adres, 'soss')            