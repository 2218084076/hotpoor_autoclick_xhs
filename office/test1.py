import xlrd
import json
filename = r"D:\github\1\hotpoor_autoclick_xhs\费用报销单模板-12月.xls"
sheet_path = xlrd.open_workbook(r"C:\Users\Terry\Desktop\SKUs.xls")
sheet_all_name = sheet_path.sheet_names()
print(sheet_all_name)
