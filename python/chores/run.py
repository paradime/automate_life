from flask import Flask, abort
app = Flask(__name__)
from chores import Chores

ch = Chores()
@app.route('/<chore>')
def start_chore(chore):
    if ch.get_delay(chore) >= 0: 
        ch.delay(chore)
        return 'Starting %s, sms is sent in %i minute' % (chore, ch.get_delay(chore))
    abort(404)

@app.route('/active')
def active():
    return 'No' if ch.empty() else 'Yes'

if __name__ == '__main__':
    app.run()
