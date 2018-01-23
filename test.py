import xlrd

book = xlrd.open_workbook('data.xlsx')
sheet = book.sheet_by_index(0)

print(sheet.cell(2, 1).value)
print(range(2, sheet.nrows-2))