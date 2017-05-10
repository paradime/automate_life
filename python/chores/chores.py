from twilio.rest import TwilioRestClient
import threading
import json

class Chores:
    def __init__(self):
        self.time_dict = {'dryer': 60, 'wash': 40, 'dishwasher': 60, 'test0': 0, 'test1': 1}
        with open('config.json') as data_file:
            self.data = json.load(data_file)
        self.scheduler = []

    def empty(self):
        return all(map(lambda t : not t.is_alive(), self.scheduler))

    def get_delay(self, task):
        return self.time_dict.get(task, -1)

    def send_sms(self, task):
        account_sid = self.data['twilio']['account_sid']
        auth_token = self.data['twilio']['auth_token']
        client = TwilioRestClient(account_sid, auth_token)
        message = ("Your " + task + " is done")
        client.messages.create(body=message, 
                to= self.data['twilio']['to_number'],
                from_= self.data['twilio']['from_number'])

    def delay(self, task):
        t = threading.Timer(self.get_delay(task)*60, self.send_sms, (task,))
        t.start()
        self.scheduler.append(t)
