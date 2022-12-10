import re
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web
import os

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

def build_stock_csv_path(dir, code):
    path = dir + str(code) + '.csv'
    return path

def save_stock_csv(dir, code, data):
    os.makedirs(dir, exist_ok=True)
    filename = build_stock_csv_path(dir, code)
    data.to_csv(filename, sep=',')

def load_stock_csv(dir, code):
    filename = build_stock_csv_path(dir, code)
    csv = pd.read_csv(filename, index_col=0, parse_dates=True)
    return csv


