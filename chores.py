from twilio.rest import TwilioRestClient
import sched, time
import json

time_dict = {'d': 60, 'dishwasher': 60, 'test': 1}
with open('config.json') as data_file:
    data = json.load(data_file)

def read():
    task = input('what is the task? (d, w, dishwasher)')
    delay(int(time_dict[task]), task)
    
def send_sms(task):
    account_sid = data['twilio']['account_sid']
    auth_token = data['twilio']['auth_token']
    client = TwilioRestClient(account_sid, auth_token)
    message = ("Your " + task + " is done")
    client.messages.create(body=message, to='5163616129', from_='+15168744020')

def print_hello(task):
    print(message)

def delay(minutes, task):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(minutes*60, 1, send_sms, (task,))
    s.run()

read()
