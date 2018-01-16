import xlrd

# Excel ファイル（ブック）を読み込み
book = xlrd.open_workbook('data.xlsx')


# ブック内のシート数を取得
num_of_worksheets = book.nsheets
print(num_of_worksheets)


# 全シートの名前を取得
sheet_names = book.sheet_names()
print(sheet_names)


# 各シートのシート名、行数、列数の取得
for i in range(book.nsheets):
    sheet = book.sheet_by_index(i)
    print('{} has {} rows and {} cols'.format(sheet.name, sheet.nrows, sheet.ncols))


# シート内の各セルの値を取得
sheet = book.sheet_by_index(0)

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        val = sheet.cell_value(rowx = row_index, colx = col_index)
        print('cell[{}, {}] = {}'.format(row_index, col_index, val))


# 一行分の xlrd.sheet.Cell のリスト
for row_index in range(sheet.nrows):
    row = sheet.row(row_index)  
    print(row)