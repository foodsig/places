from pandas.io.excel import ExcelWriter
import pandas

with ExcelWriter('places.xlsx') as ew:
    pandas.read_csv('places.csv').to_excel(ew, index=False)
