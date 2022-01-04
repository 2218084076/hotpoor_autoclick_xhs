import xlrd
import json
filename = r"D:\github\1\hotpoor_autoclick_xhs\费用报销单模板-12月.xls"
filename1=r"D:\github\1\hotpoor_autoclick_xhs\费用报销单模板-12月.xlsx"
# on_demand=True
def reader():
    data = xlrd.open_workbook(filename1,on_demand=True)
    table = data.sheets()[0]
    merged_cells=[]
    for i in table.merged_cells:
        merged_cells.append(list(i))
    company = []
    for i in range(0,table.nrows):
        company.append(table.row_values(i))
        # print(table.row_values(i))
    print(company)
    # print(merged_cells)
reader()
