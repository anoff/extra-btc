from flask import Flask, send_file, request
from io import BytesIO
from lib.data import get_price
from lib.graph import graph as draw_img
from lib.config import from_query as cfg_from_query

app = Flask(__name__)

@app.route('/')
def response():
    cfg = cfg_from_query(request.args.to_dict())
    # fetch data
    res = get_price(start=cfg["start"], end=cfg["end"])
    x = res['x']
    y = res['y']
    labels = [elm[0:7] for elm in res['labels']]

    # create image
    img = draw_img(x, y, labels, cfg["fit_ranges"], cfg["fit_forecast"])
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run()
