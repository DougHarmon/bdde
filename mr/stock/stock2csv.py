import stock_formatter
import stock_mapper

if __name__ == '__main__':
    formatter = stock_formatter.FormatCsv('AAPL_Mar26_U.cvs')
    stock_mapper.read_from_original('AAPL_Mar26.csv', formatter)
    formatter.flush()
