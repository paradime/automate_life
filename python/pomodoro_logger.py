from pygame import mixer
from time import sleep
import pytz
from datetime import datetime
import os
import json
fileDir = os.path.dirname(os.path.realpath('__file__'))
ocarina = os.path.join(fileDir, '../OOT_Secret.wav')
times = {'w': 25, 'r': 5}
mixer.init(frequency=32000)

def read():
    block = input('Is this a (w)ork or (r)est block?(w or r)')
    if block == 'r':
        start_timer(times[block])
    else:
        if(log_exists()):
            tasks = existing_tasks()
            for i in range(len(tasks)):
                print(str(i) + ': ' + tasks[i])
            print(str(len(tasks)) + ': New Task')
            num = int(input('Choose a task'))
            if(num == len(tasks)):
                task = input('What are you working on now?')
            else:
                task = tasks[num]
        else:
            task = input('What are you working on?')
        start_timer(times[block])
        write_to_log(task)
    read()

def write_to_log(task_name):
    index = len(existing_tasks()) if log_exists() else 0;
    with open(file_name(), 'a+') as f:
        f.write(str(index) + ' ' + task_name + '\n')

def existing_tasks():
    with open(file_name()) as task_list:
        raw_tasks = task_list.readlines()
    return list(map((lambda x: x.split()[1].strip()), raw_tasks))

def file_name():
    return datetime.utcnow().strftime('%d-%m-%y')+'.log'

def log_exists():
    return os.path.isfile(file_name())

def start_timer(minutes):
    seconds = minutes * 1
    for time_since in range(0, seconds):
        m, s = divmod((seconds - time_since), 60)
        print("%02d:%02d" % (m, s))
        sleep(1)
        print(chr(27) + "[2J") # clear terminal
    play_sound()

def play_sound():
    mixer.music.load(ocarina)
    mixer.music.play()

while(True):
    read()
