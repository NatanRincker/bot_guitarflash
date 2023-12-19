import PySimpleGUI as sg

def start_gui():
    layout = [
        [sg.Text('Game URL:'), sg.InputText(key='_URL_')],
        [sg.Button('Put Game on screen', key='_PUT_GAME_'),
         sg.Button('Start BOT', key='_START_BOT_')],
    ]
    window = sg.Window('Guitar Flash BOT', layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '_PUT_GAME_':
            url = values['_URL_']
            #put_game_on_screen(url)
        elif event == '_START_BOT_':
            pass
            #start_bot()

start_gui()