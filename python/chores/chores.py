from twilio.rest import TwilioRestClient
import sched, time
import json

time_dict = {'dryer': 60, 'wash': 40, 'dishwasher': 60, 'test': 0}
with open('config.json') as data_file:
    data = json.load(data_file)

class Chores:
    def get_delay(task):
        if task in time_dict:
            return time_dict[task]
        else:
            return -1

    def send_sms(task):
        account_sid = data['twilio']['account_sid']
        auth_token = data['twilio']['auth_token']
        client = TwilioRestClient(account_sid, auth_token)
        message = ("Your " + task + " is done")
        client.messages.create(body=message, 
                to= data['twilio']['to_number'],
                from_= data['twilio']['from_number'])

    def delay(task):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(Chores.get_delay(task)*60, 1, Chores.send_sms, (task,))
        s.run()
