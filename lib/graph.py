import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from io import BytesIO
import seaborn as sns

def graph(x, y, labels, fit_ranges=[30, 90, 180, 360], fit_forecast=180):
    # polyfit 1D
    coeff = np.polyfit(x, y, 2)
    fit_x = range(len(x) + fit_forecast)
    fit_y = [coeff[0] * (e ** 2) + coeff[1] * e + coeff[2] for e in fit_x]
    # mean deviation from fit
    errors = [y[i] - fit_y[i] for i in x]
    reg_error = np.mean(np.absolute(errors))

    # plot
    sns.set_style('whitegrid')
    sns.set_palette('deep')
    fg, ax = plt.subplots(1, figsize=(9, 6))
    plt.plot(x, y)

    # 2 degree poly fit
    plt.plot(fit_x, fit_y, 'k')
    plt.plot(fit_x, fit_y + reg_error, 'k--')
    plt.plot(fit_x, fit_y - reg_error, 'k--')

    # fit ranges
    colors = sns.color_palette(None, len(fit_ranges)+1)
    cnt = 0
    for fit_range in fit_ranges:
        tr = range(fit_range)
        yr = y[-fit_range:]
        coeff = np.polyfit(tr, yr, 2)
        tr = range(fit_range + fit_forecast)
        fit = [coeff[0] * (e ** 2) + coeff[1] * e + coeff[2] for e in tr]
        c = colors.pop(1)
        plt.plot([e + x[-fit_range] for e in tr], fit, c=c)
        ax.text(30, 2000 - (1 + cnt) * 100, '{0} days fitted'.format(fit_range), color=c, fontsize=10)
        cnt += 1

    ax.set_ylabel('price [USD]')
    ax.set_xlabel('time')
    ax.grid(True)
    ax.set_ylim(0, 2000)
    ax.set_xlim(0, x[-1] + fit_forecast)

    # adjust labels
    length = x[-1]
    ticks = np.linspace(0, length, 6).astype(np.int16)
    xlabels = [labels[val] for val in ticks]
    ax.set_xticks(ticks)
    ax.set_xticklabels(xlabels)

    # extract data from plot
    img = BytesIO()
    fg.savefig(img)
    img.seek(0)
    return img
