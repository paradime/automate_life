from flask import Flask, abort
app = Flask(__name__)
from chores import Chores

@app.route('/<chore>')
def start_chore(chore):
    if Chores.get_delay(chore) >= 0: 
        Chores.delay(chore)
        return 'Starting %s, sms is sent in %i minute' % (chore, Chores.get_delay(chore))
    abort(404)
