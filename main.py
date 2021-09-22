import requests
import time
import sys
import os
import pygame
from sound import playsound,play_morse_sound
from sound import FREQ,BITSIZE,CHANNELS,BUFFER,FRAMERATE

pygame.init ()
os.system ('cls||clear')
pygame.mixer.init (FREQ,BITSIZE,CHANNELS,BUFFER)

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
               '1': '.---- ',
               '0': '----- ',
               '2': '..--- ',
               '3': '...-- ',
               '4': '....- ',
               '5': '..... ',
               '6': '-.... ',
               '7': '--... ',
               '8': '---.. ',
               '9': '----. ',
               ',': '--..-- ',
               '.': '.-.-.- ',
               '?': '..--.. ',
               ';': '-.-.-. ',
               ':': '---... ',
               "'": '.----. ',
               '-': '-....- ',
               '/': '-..-. ',
               '(': '-.--.- ',
               ')': '-.--.- ',
               ' ': '|',
               '_': '..--.- '}





adres='http://192.168.24.173:8080'

def communication(adres):
    r = requests.get(adres)
    if r.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')    
    print()
communication(adres)


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

def to_robot(a, m):
    print('Отправка сообщения роботу...')
    play_morse_sound(m)
    r = requests.post(a,m.encode('utf-8'))
    if r.status_code == 200:
        print('Команда принята.')
        time.sleep(1)
        print('Бегу к вам!')
    else:
        print('Команда не принята. Продолжаю выполнять прежнюю инструкцию.')

to_robot(adres,morz)



#'---. . .-.. --- .-- . -.- / .-- / --- .--. .- ... -. --- ... - ..'