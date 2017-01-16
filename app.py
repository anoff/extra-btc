from flask import Flask, send_file, request
from io import BytesIO
from lib.data import get_price
from lib.graph import graph as draw_img
import datetime

app = Flask(__name__)

@app.route('/')
def response():
    print(request.args)
    if request.args.get('start_date'):
        start_date = request.args.get('start_date')
    else:
        start_date = '2013-01-01'
    if request.args.get('end_date'):
        end_date = request.args.get('end_date')
    else:
        end_date = datetime.date.today().isoformat()
    if request.args.get('fit'):
        fit_ranges = request.args.getlist('fit')
        fit_ranges = [int(x) for x in fit_ranges]
    else:
        fit_ranges = [30, 90, 180, 360] # ranges in days that should show up as individual linear regressions
    if request.args.get('fit_forecast'):
        fit_forecast = int(request.args.get('fit_forecast'))
    else:
        fit_forecast = 180 # how many days the fittet curves should be extrapolated
    # fetch data
    print(end_date)
    res = get_price(start=start_date, end=end_date)
    x = res['x']
    y = res['y']
    labels = [elm[0:7] for elm in res['labels']]

    # create image
    img = draw_img(x, y, labels, fit_ranges, fit_forecast)
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run()
