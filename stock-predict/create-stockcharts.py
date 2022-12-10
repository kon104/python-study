import define
import mycommon as mycom

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import mplfinance as mpf

def pickup_lastrow_info(data):
    info = {}
    info['row'] = data.iloc[-1]
    info['date'] = info['row'].name
    info['idx'] = data.index.get_loc(info['date'])
    return info

def gen_chart_dir(data, endidx, endrow):
    xrow = data.iloc[endidx + 5]
    xdate = xrow.name
    rate = xrow.Close / endrow.Close
    dirname = './data/chart/'
    if rate > 1.05:
        dirname = dirname + 'up/'
    else:
        dirname = dirname + 'down/'
    return dirname

def save_chart(data, dir, code, startdate, enddate):
    filename = dir \
        + str(code) + '-' \
        + startdate.strftime("%Y%m%d") + '_' \
        + enddate.strftime("%Y%m%d") + '.png'
    mpf.plot(data, type='candle', volume=True, mav=(5, 25), savefig=filename)

def draw_chart(code):
    dir = define.CSV_DIR
    data = mycom.load_stock_csv(dir, code)
    #	print(data)
    firstdate = data.iloc[0].name
    lastinfo = pickup_lastrow_info(data)
    lastidx = lastinfo['idx']

    for row in data.itertuples():
        startdate = row.Index
        todate = startdate \
            + relativedelta(months=6) - datetime.timedelta(days=1)
        block = data[startdate : todate]
        endinfo = pickup_lastrow_info(block)
        endrow = endinfo['row']
        enddate = endinfo['date']
        endidx = endinfo['idx']
        xidx = endidx + 5
        if (xidx > lastidx):
            break

        dirname = gen_chart_dir(data, endidx, endrow)
        save_chart(block, dirname, code, startdate, enddate)
        
# main
def main():
    path  = define.STOCKS_PATH
    codes = mycom.read_stock_codes(path)
    print(codes)
    for code in codes:
        draw_chart(code)

if __name__ == '__main__':
    main()

