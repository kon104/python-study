import re
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web

def read_stock_codes(path):
    f = open(path, 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    data = re.sub('#[^\n]*\n', '', data)
    codes = data.splitlines()
    return codes

def collect_stock_prices(code, date = None, days = None):
    code_data = str(code) + '.JP'
    data = pd.DataFrame([])
    ed = datetime.date.today()
    st = ed - relativedelta(years=5)
    if (date is not None):
        ed = date
        if (days is not None):
            st = ed - datetime.timedelta(days=days)
        else:
            st = ed - relativedelta(years=5)
    data = web.DataReader(code_data, 'stooq', start=st, end=ed).dropna()
    data = data.sort_index()
    return data

