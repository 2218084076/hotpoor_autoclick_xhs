import xlrd
import json
filename1 = r"C:\Users\Terry\Desktop\SKUs.xls"


def reader():
    data = xlrd.open_workbook(filename1)
    table = data.sheets()[0]
    company = []
    for i in range(0,table.ncols):
        company.append(table.col_values(i))
        # print(table.col_values(i))
    print(company[1])
    # print(merged_cells)
reader()
