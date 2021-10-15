import os
import time

import pygame
import requests
from alive_progress import alive_bar
from dotenv import load_dotenv
load_dotenv()


TEXT_MESSAGE = os.getenv('command', 'По-умолчанию').lower()
BUFFER = 1024
FRAMERATE = 60
MORSE_SOUND = {
    '.': 'dot.ogg',
    '-': 'dash.ogg',
    '|': 'long_silence.ogg',
}
MORSE_CODE = {
    'а': '.-',
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
    '1': '.----',
    '0': '-----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    ';': '-.-.-.',
    ':': '---...',
    "'": '.----.',
    '-': '-....-',
    '/': '-..-.',
    '(': '-.--.-',
    ')': '-.--.-',
    ' ': '|',
    '_': '..--.-'
}
URL = 'http://195.161.68.58'


def contact_the_robot(url):
    response = requests.get(url)
    message = 'Проверка связи с роботом...'
    print(message)
    with alive_bar(len(message), bar='brackets', spinner='radioactive') as bar:
        for _ in range(len(message)):
            time.sleep(0.06)
            bar()
    os.system('cls||clear')
    if response.status_code == 200:
        print('Связь с роботом установлена!')
    else:
        print('Нет связи с роботом')
    print()


def play_music(sound_file):
    sound = pygame.mixer.Sound(sound_file)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)


def play_morse_music(morse_message):
    print()
    with alive_bar(len(morse_message), bar='brackets',
                   spinner='dots_waves2') as bar:
        for letter in morse_message:
            if letter == '.':
                play_music(pygame.mixer.Sound('dot.ogg'))
            elif letter == '-':
                play_music(pygame.mixer.Sound('dash.ogg'))
            elif letter == '|':
                play_music(pygame.mixer.Sound('long_silence.ogg'))
            bar()
    print()


def send_message_to_robot(url, morse_message):
    print('Отправка сообщения роботу...')
    response = requests.post(url, morse_message.encode('utf-8'))
    play_morse_music(morse_message)
    if response.status_code == 200:
        print('Команда принята.')
        time.sleep(1)
        print('Бегу к вам!')
    elif response.status_code == 501:
        print('Команда принята. Продолжаю выполнять прежнюю инструкцию.')
    else:
        print('Команда не принята. Не понял вас!')


def main():
    pygame.init()
    os.system('cls||clear')
    pygame.mixer.init(BUFFER)

    morse_message = ''.join([MORSE_CODE[letter] for letter in TEXT_MESSAGE])

    contact_the_robot(URL)
    send_message_to_robot(URL, morse_message)


if __name__ == '__main__':
    main()
