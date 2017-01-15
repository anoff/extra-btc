from flask import Flask, send_file
from io import BytesIO
from lib.data import get_price
from lib.graph import graph as draw_img
import datetime

app = Flask(__name__)

# config
start_date = '2013-01-01'
end_date = datetime.date.today().isoformat()
fit_ranges = [30, 90, 180, 360] # ranges in days that should show up as individual linear regressions
fit_forecast = 180 # how many days the fittet curves should be extrapolated

@app.route('/')
def hello_world():
    # fetch data
    res = get_price(start=start_date, end=end_date)
    x = res['x']
    y = res['y']
    labels = [elm[0:7] for elm in res['labels']]

    # create image
    img = draw_img(x, y, labels)
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run()
