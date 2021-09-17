import requests
import time
def gudok (i = 0.1, chastota = 1000): # функция воспроизведения звука
    print ("\a", end = "\r")
    time.sleep (i)


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


soobchenie='СОС СОС СОС' 
soobchenie=soobchenie.lower()

x=soobchenie[0]
xx=soobchenie[1]
xxx=soobchenie[2]
probel1=soobchenie[3]
y=soobchenie[4]
yy=soobchenie[5]
yyy=soobchenie[6]
probel2=soobchenie[7]
z=soobchenie[8]
zz=soobchenie[9]
zzz=soobchenie[10]
morz=azbukaMorze[x]+azbukaMorze[xx]+azbukaMorze[xxx]+\
    azbukaMorze[probel1]+azbukaMorze[y]+azbukaMorze[yy]+\
    azbukaMorze[yyy]+azbukaMorze[probel2]+azbukaMorze[z]+\
    azbukaMorze[zz]+azbukaMorze[zzz]        
print(morz)
if morz[0] == '.':
    gudok(i = 0.1)
elif morz[0] == '-':
    gudok(i = 0.3)
elif morz[0] == '/':
    time.sleep(0.5)
if morz[1] == '.':
    gudok(i = 0.1)
elif morz[1] == '-':
    gudok(i = 0.3)
elif morz[1] == '/':
    time.sleep(0.5)
if morz[2] == '.':
    gudok(i = 0.1)
elif morz[2] == '-':
    gudok(i = 0.3)
elif morz[2] == '/':
    time.sleep(0.5)
if morz[3] == '.':
    gudok(i = 0.1)
elif morz[3] == '-':
    gudok(i = 0.3)
elif morz[3] == '/':
    time.sleep(0.5)
if morz[4] == '.':
    gudok(i = 0.1)
elif morz[4] == '-':
    gudok(i = 0.3)
elif morz[4] == '/':
    time.sleep(0.5)
if morz[5] == '.':
    gudok(i = 0.1)
elif morz[5] == '-':
    gudok(i = 0.3)
elif morz[5] == '/':
    time.sleep(0.5)
if morz[6] == '.':
    gudok(i = 0.1)
elif morz[6] == '-':
    gudok(i = 0.3)
elif morz[6] == '/':
    time.sleep(0.5)
if morz[7] == '.':
    gudok(i = 0.1)
elif morz[7] == '-':
    gudok(i = 0.3)
elif morz[7] == '/':
    time.sleep(0.5)
if morz[8] == '.':
    gudok(i = 0.1)
elif morz[8] == '-':
    gudok(i = 0.3)
elif morz[8] == '/':
    time.sleep(0.5)
if morz[9] == '.':
    gudok(i = 0.1)
elif morz[9] == '-':
    gudok(i = 0.3)
elif morz[9] == '/':
    time.sleep(0.5)
if morz[10] == '.':
    gudok(i = 0.1)
elif morz[10] == '-':
    gudok(i = 0.3)
elif morz[10] == '/':
    time.sleep(0.5)               
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
robot(adres,soobchenie)


#'---. . .-.. --- .-- . -.- / .-- / --- .--. .- ... -. --- ... - ..'