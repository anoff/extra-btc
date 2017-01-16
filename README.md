extra-btc
===

> extrapolate bitcoin market trends with fancy graphs and lambda functions 📈ƛ🐦

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Getting started](#getting-started)
- [Todo](#todo)
- [License](#license)

<!-- /TOC -->

# Getting started

You need to have `python` and a package manager (e.g. `miniconda`) installed. The code is tested on python `3.5.2` only.
Install the required packages using the following command:

```bash
pip -r requirements.txt install
```

Start the app with `python app.py`

# Todo
- [x] parse query arguments
- [ ] robustify argument parsing (e.g. wrong format in date)
- [ ] make lambda-ish
- [x] fix x-labels
- [ ] beautify the plot
- [ ] use [seaborn](http://seaborn.pydata.org/) instead of prettyplotlib

# License

MIT © [Andreas Offenhäuser](http://anoff.io)
