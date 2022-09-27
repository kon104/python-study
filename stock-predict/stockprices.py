import mycommon as mycom
import os

def save_csv(code, data):
    newdir = './data/csv/'
    os.makedirs(newdir, exist_ok=True)
    filename = newdir + str(code) + '.csv'
    data.to_csv(filename, sep=',')

# main
def main():
    path  = './stocks.txt'
    codes = mycom.read_stock_codes(path)
    print(codes)
    for code in codes:
        data = mycom.collect_stock_prices(code)
        save_csv(code, data)

if __name__ == '__main__':
    main()

