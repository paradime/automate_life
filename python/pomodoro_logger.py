from pygame import mixer
import sys
from time import sleep
# import pytz
from datetime import datetime
import os
import json
fileDir = os.path.dirname(os.path.realpath('__file__'))
ocarina = os.path.join(fileDir, '..\OOT_Secret.wav')
times = {'w': 25, 'b': 5}
mixer.init(frequency=32000)
goal = 3

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
    startText += """(w)ork block,
(b)reak block,
(l)ogging a task,
(r)ead the log
> """
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

def file_name():
    return datetime.utcnow().strftime('%d-%m-%y')+'.log'

def file_name_with_date(date):
    return date.strftime('%d-%m-%y.log')

def log_exists():
    return os.path.isfile(file_name_with_date(datetime.utcnow()))

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

"""
TESTS
"""
def test_file_name():
    print(file_name_with_date(datetime(1901,2,3)) == '03-02-01.log')

test_file_name()
"""
END TESTS
"""

while(True):
    read()
