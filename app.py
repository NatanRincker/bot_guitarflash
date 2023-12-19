import pyautogui as pyg
import keyboard
import webbrowser
from multiprocessing import Process
from common import pressHoldRelease
import PySimpleGUI as sg

watch_process_list = []

def start_bot():
    key_loc_dectionary = {'a': [541, 793], 's': [642, 792], 'j': [
        742, 792], 'k': [843, 795], 'l': [943, 790]}
    print(f'watching keys...')
    for key, pixel in key_loc_dectionary.items():
        watch_process = Process(target=watch_key, args=(key, pixel))
        watch_process.start()
        watch_process_list.append(watch_process)

def stop_bot():
    for process in watch_process_list:
        process.terminate()

def watch_key(key: str, pixel):
    print(f'watching key {key} at pixel{pixel}')
    while keyboard.is_pressed('p') == False:
        if key_is_couvered(pixel):
            pressHoldRelease(key)
    print(f'Stopped watch for key {key}')


def key_is_couvered(bottom_pixel):
    return not pyg.pixelMatchesColor(bottom_pixel[0], bottom_pixel[1], (0, 0, 0))


def get_game_on_screen(url: str):
    webbrowser.open_new_tab(url)
    pyg.moveTo(203, 435, duration=1)
    pyg.scroll(-200)


def start_gui():
    layout = [
        [sg.Text('Game URL:'), sg.InputText(key='_URL_')],
        [sg.Button('Put Game on screen', key='_PUT_GAME_'),
         sg.Button('Start BOT', key='_START_BOT_'),
         sg.Button('Stop BOT', key='_STOP_BOT_')],
        [sg.Text('you can also press "1" on keyboard to stop the BOT')]
    ]
    window = sg.Window('Guitar Flash BOT', layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '_PUT_GAME_':
            url = values['_URL_']
            get_game_on_screen(url)
        elif event == '_START_BOT_':
            start_bot()
        elif event == '_STOP_BOT_':
            pyg.press('1', presses=2, interval=0.5)


if __name__ == '__main__':
    start_gui()