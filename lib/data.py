import requests
import datetime

def get_price(start='2013-01-01', end=datetime.date.today().isoformat(), currency='USD'):
    r = requests.get('http://api.coindesk.com/v1/bpi/historical/close.json?currency={2}&start={1}&end={0}'
    .format(end, start, currency))
    data = r.json()['bpi']
    x = list(data.keys())
    x.sort()
    y = [data[e] for e in x]
    # transform to date
    t = [datetime.datetime.strptime(elm, '%Y-%m-%d') for elm in x]
    dt = [(elm - t[0]).days for elm in t]

    return {'x': dt, 'y': y, 'labels': x}
