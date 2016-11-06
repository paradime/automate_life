from trello import TrelloClient
from time import sleep
from pygame import mixer
from datetime import datetime
import json
"""
TODO: 
pull credentials from a file
make OO
"""
times = {'w': 25, 'r': 5}
mixer.init(frequency=32000)
todo_list = '5810b18d4e03d4ebbb720c59'
working_list = '57bc53df9cb4d2b03128c6f1'
done_list = '57bc53d84d25a907e342159f'

with open('config.json') as data_file:
    data = json.load(data_file)
key = data['trello']['api_key']
api_secret = data['trello']['api_secret']
oauth_token = data['trello']['oauth_token']
oauth_token_secret = data['trello']['oauth_token_secret']
board_id = data['trello']['board_id']
trello = TrelloClient(api_key = key, api_secret=api_secret, token=oauth_token, token_secret=oauth_token_secret)

def read():
    block = input('Is this a (w)ork or (r)est block, or (new) card?(w, r, new)')
    if block == 'new':
        handle_new_command()
    else:
        start_timer(times[block])

def handle_new_command():
    board = trello.get_board(board_id)
    working = board.get_list(working_list)
    todo = board.get_list(todo_list)
    if len(working.list_cards()) > 0: working.list_cards()[0].change_list(done_list) 
    todo_cards = todo.list_cards()
    for index in range(len(todo_cards)):
        print(str(index) + ' : ' + todo_cards[index].name)
    selection = input('which card are you working on?')
    todo_cards[int(selection)].change_list(working_list)

def mark_card():
    board = trello.get_board(board_id)
    working = board.get_list(working_list)
    todo = board.get_list(todo_list)
    now = datetime.now()
    comment = now.strftime("Completed 1 pomodoro on %Y-%m-%d %H:%M")
    if len(working.list_cards()) > 0: working.list_cards()[0].comment(comment)
    
def start_timer(minutes):
    seconds = minutes
    for time_since in range(0, seconds):
        m, s = divmod((seconds - time_since), 60)
        print("%02d:%02d" % (m, s))
        sleep(1)
        print(chr(27) + "[2J") # clear terminal
    play_sound()
    mark_card()

def play_sound():
    mixer.music.load('OOT_Secret.wav')
    mixer.music.play()

while(True):
    read()

