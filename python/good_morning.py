import webbrowser, sched, random, time, datetime

sites = [
    "https://www.youtube.com/user/jsconfeu/playlists",
    "https://www.reddit.com/r/dailyprogrammer/",
    "https://github.com/getify/You-Dont-Know-JS/blob/master/async%20&%20performance/README.md#you-dont-know-js-async--performance",
    "https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html",
    "http://shichuan.github.io/javascript-patterns/"
    ]

def load_site():
    webbrowser.open(random.sample(sites, 1)[0])

while(True):
    f = open('date', 'r')
    date = f.read()
    f.close()
    today = datetime.datetime.today()
    beginning = datetime.datetime(today.year, today.month, today.day)
    while(str(beginning)== date):
        time.sleep(60)
        today = datetime.datetime.today()
        beginnig = datetime.datetime(today.year, today.month, today.day)
    f = open('date', 'w')
    f.write(str(beginning))
    f.close()

    load_site()
    time.sleep(61)
