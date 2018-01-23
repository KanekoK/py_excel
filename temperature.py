import xlrd
import os.path
import numpy as np
from scipy import stats
xlfile = "data.xlsx"


if os.path.exists(xlfile):
    xls = xlrd.open_workbook(xlfile)
    sheet1 = xls.sheet_by_index(0)
    nrows = sheet1.nrows-2
    ncols = sheet1.ncols
    # 2次元配列に
    data = np.zeros(ncols*nrows).reshape(nrows, ncols)
    for r in range(2, nrows):
        for c in range(0, ncols):
            print(r, c)
            data[r-1, c] = sheet1.cell(r, c).value
    yamaguchi = data[:, 1].mean()
    tokyo     = data[:, 3].mean()
    print(yamaguchi)
    print(tokyo)
    t,p = stats.ttest_ind(yamaguchi, tokyo, equal_var=False)
    # msg = "p-value: %.5f" % p
    # print(msg)
