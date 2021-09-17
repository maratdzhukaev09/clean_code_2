import requests
import time
def gudok (i = 0.1, chastota = 1000): # функция воспроизведения звука
    print ("\a", end = "\r")
    time.sleep (i)

soobchenie_1 = '---. . .-.. --- .-- . -.- / .-- / --- .--. .- ... -. --- ... - ..' 

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

def communication(adres): # функция для проверки связи с роботом
    r = requests.get(adres)
    if r.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')    

#communication(adres)


soobchenie_2='СОС СОС СОС' 
soobchenie_2=soobchenie_2.lower()

x=soobchenie_2[0]
xx=soobchenie_2[1]
xxx=soobchenie_2[2]
probel1=soobchenie_2[3]
y=soobchenie_2[4]
yy=soobchenie_2[5]
yyy=soobchenie_2[6]
probel2=soobchenie_2[7]
z=soobchenie_2[8]
zz=soobchenie_2[9]
zzz=soobchenie_2[10]
morz=azbukaMorze[x]+azbukaMorze[xx]+azbukaMorze[xxx]
print(morz)
# for word in soobchenie_1:
#     for symbol in word:
#         if symbol == '.':
#             gudok(i = 0.1)
#         elif symbol == '-':
#             gudok(i = 0.7)
#         elif symbol == '/':
#             time.sleep(1)
def robot(a, m): # функция для посыла сообщения роботу
    r = requests.post(a,m.encode('utf-8'))
    if r.status_code == 200:
        print('Команда принята.')
        time.sleep(1)
        print('Бегу к вам!')
    else:
        print('Команда не принята. Продолжаю выполнять прежнюю инструкцию.')
robot(adres,soobchenie_2)


#'---. . .-.. --- .-- . -.- / .-- / --- .--. .- ... -. --- ... - ..'