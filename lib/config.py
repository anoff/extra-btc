import datetime
import ast

def from_query(args):
    print(args)
    if 'start' in args:
        start = args['start']
    else:
        start = '2013-01-01'

    if 'end' in args:
        end = args['end']
    else:
        end = datetime.date.today().isoformat()

    if 'fit' in args:
        fit_ranges = ast.literal_eval(args['fit'])
    else:
        fit_ranges = [30, 90, 180, 360] # ranges in days that should show up as individual linear regressions

    if 'forecast' in args:
        forecast = int(args['forecast'])
    else:
        forecast = 180 # how many days the fittet curves should be extrapolated

    return {
        "start": start,
        "end": end,
        "fit_ranges": fit_ranges,
        "fit_forecast": forecast
    }
