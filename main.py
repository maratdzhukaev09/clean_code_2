import requests
import time
import os
import pygame
from alive_progress import alive_bar
FREQ = 44100
BITSIZE = -16
CHANNELS = 2
BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
}
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
adres='http://192.168.24.173:8080'
def communication(adres):
    r = requests.get(adres)
    if r.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')    
    print()
communication(adres)
def playsound(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)
def play_morse_sound(morz):
    print()
    with alive_bar(len(morz), bar = 'brackets', spinner = 'dots_waves2') as bar:
        if morz[0] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[0] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[0] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[1] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[1] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[1] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[2] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[2] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[2] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[3] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[3] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[3] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[4] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[4] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[4] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[5] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[5] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[5] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()  
        if morz[6] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[6] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[6] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[7] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[7] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[7] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[8] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[8] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[8] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[9] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[9] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[9] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()   
        if morz[10] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[10] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[10] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[11] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[11] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[11] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[12] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[12] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[12] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[13] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[13] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[13] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[14] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[14] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[14] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[15] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[15] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[15] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[16] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[16] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[16] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[17] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[17] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[17] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[18] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[18] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[18] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[19] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[19] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[19] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[20] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[20] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[20] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[21] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[21] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[21] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[22] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[22] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[22] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[23] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[23] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[23] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[24] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[24] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[24] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[25] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[25] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[25] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[26] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[26] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[26] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[27] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[27] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[27] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
        if morz[28] == '.':
            playsound(pygame.mixer.Sound('dot.ogg'))
        elif morz[28] == '-':
            playsound(pygame.mixer.Sound('dash.ogg'))
        elif morz[28] == '|':
            playsound(pygame.mixer.Sound('long_silence.ogg'))
        bar()
    print()
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