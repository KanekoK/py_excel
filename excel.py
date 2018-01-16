import xlrd

# Excel ファイル（ブック）を読み込み
book = xlrd.open_workbook('data.xlsx')

# ブック内のシート数を取得
num_of_worksheets = book.nsheets
print(num_of_worksheets)

# 全シートの名前を取得
sheet_names = book.sheet_names()
print(sheet_names)
