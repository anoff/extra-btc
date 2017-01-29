from io import BytesIO
from lib.data import get_price
from lib.graph import graph as draw_img
from lib.config import from_query as cfg_from_query

def response(event, context):
    return {
        "statusCode": 200,
        "body": "weeee",
        "headers": {
            "Content-Type": "application/json"
        }
    }

def handler(event, context):
    # cfg = cfg_from_query(event["queryStringParameters"])
    cfg = {
        "start": '2013-01-01',
        "end": "2016-01-20",
        "fit_ranges": [10, 30, 90],
        "fit_forecast": 30
    }
    # fetch data
    res = get_price(start=cfg["start"], end=cfg["end"])
    x = res['x']
    y = res['y']
    labels = [elm[0:7] for elm in res['labels']]

    # create image
    img = draw_img(x, y, labels, cfg["fit_ranges"], cfg["fit_forecast"])
    return {
        "statusCode": 200,
        "body": img,
        "headers": {
            "Content-Type": "image/png"
        }
    }
