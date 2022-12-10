import define
import mycommon as mycom

# main
def main():
    path  = define.STOCKS_PATH
    codes = mycom.read_stock_codes(path)
    print(codes)
    for code in codes:
        data = mycom.collect_stock_prices(code)
        dir = define.CSV_DIR
        mycom.save_stock_csv(dir, code, data)

if __name__ == '__main__':
    main()

