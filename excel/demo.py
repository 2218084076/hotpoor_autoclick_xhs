import xlrd
import json
from openpyxl import Workbook


filename = r"D:\github\1\hotpoor_autoclick_xhs\费用报销单模板-12月.xls"
filename1=r"D:\github\1\hotpoor_autoclick_xhs\费用报销单模板-12月.xlsx"
book = xlrd.open_workbook(filename, formatting_info=True)
sheet_1 = book.sheet_by_index(0)
rowNum = sheet_1.nrows  # sheet行数
colNum = sheet_1.ncols  # sheet列数
print(rowNum,colNum)

def getBGColor(book, sheet, row, col):
    xfx = sheet.cell_xf_index(row, col)
    xf = book.xf_list[xfx]
    bgx = xf.background.pattern_colour_index
    pattern_colour = book.colour_map[bgx]

    #Actually, despite the name, the background colour is not the background colour.
    #background_colour_index = xf.background.background_colour_index
    #background_colour = book.colour_map[background_colour_index]

    return pattern_colour

def get_front_color(book,sheet,row,col):
    xfx = sheet.cell_xf_index(row,col)
    xf = book.xf_list[xfx]
    bgx = xf.font_index.pattern_color_index
    pattern_color = book.color_map[bgx]
    return pattern_color

BG_list=[]
font_list=[]
bg_index=[]

'''
for i in range(0,rowNum):
    for j in range(0,colNum):
        if getBGColor(book,sheet_1,i,j) == None:
            print('')
        else:
            data_json = {
                "row":i,
                "col":j,
                "rgb":list(getBGColor(book,sheet_1,i,j))
            }
            BG_list.append(data_json)

        # print(f'x{i},y{j}',getBGColor(book,sheet_1,i,j))
print(BG_list)
'''



xf_list = book.xf_list
print(xf_list)

# book = xlrd.open_workbook(filename, formatting_info=True)
# sheet_1 = book.sheet_by_index(0)
# xf_list = book.xf_list
# cell_xf_index = sheet_1.cell_xf_index(2,1)
# print(cell_xf_index)
# cell_xf = xf_list[cell_xf_index]
# print(cell_xf)
# background = cell_xf.background
# print(background.fill_pattern,
#       ',',background.background_colour_index,
#       ',',background.pattern_colour_index)

