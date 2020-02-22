from pygame import mixer
import sys
from time import sleep
from datetime import datetime
import os
import json
fileDir = os.path.dirname(os.path.realpath('__file__'))
ocarina = os.path.join(fileDir, '..\OOT_Secret.wav')
times = {'w': 20, 'b': 5}
mixer.init(frequency=32000)
goal = 3
run = True
COMMAND_OPTIONS = """(w)ork block,
(b)reak block,
(l)ogging a task,
(r)ead the log
(e)xit the program
> """

def read():
    block = input(generate_start_text())
    if block == 'b':
        start_timer(times[block])
    elif block == 'l':
        task = input('What did you do? ')
        write_to_log(task)
    elif block == 'r':
        if(log_exists()):
            print_log()
    elif block == 'e':
        return "stop"
    else:
        if(log_exists()):
            tasks = existing_tasks()
            for i in range(len(tasks)):
                print(str(i) + ': ' + tasks[i])
            print(str(len(tasks)) + ': New Task')
            num = int(input('Choose a task '))
            task = input('What are you working on now? ') if num == len(tasks) else tasks[num]
        else:
            task = input('What are you working on? ')
        start_timer(times[block])
        write_to_log(task)
    read()

def generate_start_text():
    startText = ('-'*goal)+'|-\n'
    if (log_exists()):
        tasks = list(set(map((lambda x: x.strip()), read_log())))
        for task in tasks:
            startText = startText.replace('-', 'X', 1)
    startText += COMMAND_OPTIONS
    return startText
    
def write_to_log(task_name):
    index = len(read_log()) if log_exists() else 0
    with open(file_name_with_date(datetime.utcnow()), 'a+') as f:
        f.write(str(index) + ' ' + task_name + '\n')

def read_log():
    with open(file_name_with_date(datetime.utcnow())) as task_list:
        raw_tasks = task_list.readlines()
    return raw_tasks

def print_log():
    tasks = list(set(map((lambda x: x.strip()), read_log())))
    tasks.sort()
    for task in tasks:
        print(task)

def existing_tasks():
    raw_tasks = read_log()
    tasks = []
    for line in raw_tasks:
        tasks.append(' '.join(line.split()[1::]))
    return list(set(map((lambda x: x.strip()), tasks)))

def file_name_with_date(date):
    return date.strftime('%d-%m-%y.log')

def log_exists(log_name = file_name_with_date(datetime.utcnow())):
    return os.path.isfile(log_name)

def start_timer(minutes):
    seconds = minutes * 60
    for time_since in range(0, seconds):
        m, s = divmod((seconds - time_since), 60)
        print("%02d:%02d" % (m, s))
        sleep(1)
        clear_terminal()
    play_sound()

def clear_terminal():
    print(chr(27) + "[2J") # clear terminal
    if(sys.platform == 'win32'):
        os.system('cls')

def play_sound():
    mixer.music.load(ocarina)
    mixer.music.play()
