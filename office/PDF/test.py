from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFTextExtractionNotAllowed,PDFPage
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.converter import PDFPageAggregator
import os

path = 'test2.pdf'
open_pdf = open(path,'rb')
pdf_file = PDFParser(open_pdf)
#1、PermissionError: [Errno 13] Permission denied: 'F:\\新建文件夹'——
# 2、误产生的原因是文件无法打开，可能产生的原因是文件找不到，或者被占用，或者无权限访问，或者打开的不是文件，而是一个目录。
doc = PDFDocument(pdf_file)
#print(type(doc))<class 'pdfminer.pdfparser.PDFDocument'
#print(type(pdf_file))<class 'pdfminer.pdfparser.PDFParser'>
'''可能是需要将文件转入包分析内格式'''
# 检测文档是否提供txt转换，不提供就忽略

    # 创建pdf资源管理器 来管理共享资源（字体的导入）
srcmgr = PDFResourceManager()
    # 创建一个pdf设备对象
device = PDFPageAggregator(srcmgr, laparams=LAParams())#聚合器
    # 创建一个pdf解释器对象
interpreter = PDFPageInterpreter(srcmgr, device)
#print(doc.get_outlines())

#print(PDFPage.get_pages(doc))# 获取page列表
    # 循环遍历列表，每次处理一个page的内容
for page in PDFPage.create_pages(doc):
    #print(page)
    interpreter.process_page(page)
    #之前就是为了为这个解析提供工具
#print(type(page))

# 接受该页面的LTPage对象 #这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
    layout = device.get_result()#页面中的结果
#print(layout)
    #print(x)
    for x in layout:
        if hasattr(x, 'get_text'):#进行if判断是为了剔除非文字
            with open('pdfduqu.txt', 'a+', encoding='utf-8') as f:
                results = x.get_text()
                f.write(results + '\n')
            '''只有最后一页'''

        # 最后关闭原始pdf文件
open_pdf.close()
'''太复杂了'''
#layout 在interpreter下面就有三页，可能是由于不在下面，面对的是最后一页的解析
#WARNING:root:GBK-EUC-H  缺失中文解码字体

