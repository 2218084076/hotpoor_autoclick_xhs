import requests
import json
import xlwt

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
table.write(0,0,"序号")
table.write(0,1,"店铺名")
table.write(0,2,"星级")
table.write(0,3,"评论数")
table.write(0,4,"人均消费")
table.write(0,5,"联系电话")
table.write(0,6,"地址")
table.write(0,7,"位置坐标")
table.write(0,8,"img_url")

urls = [
    ["page1","https://www.qianshanghua.com/api/page/comment/load?chat_id=e1f7ece99ebb482ebd32c7dcf108b127&comment_id=3663345b66dc4971a478f560b87ccec4"],
    ["page2","https://www.qianshanghua.com/api/page/comment/load?chat_id=e1f7ece99ebb482ebd32c7dcf108b127&comment_id=36ae6a9b9f424c1fbaec590e12998f6c"],
    ["page3","https://www.qianshanghua.com/api/page/comment/load?chat_id=e1f7ece99ebb482ebd32c7dcf108b127&comment_id=718354d50f494c81b5dd9f3d56022b59"],
    ["page4","https://www.qianshanghua.com/api/page/comment/load?chat_id=e1f7ece99ebb482ebd32c7dcf108b127&comment_id=71ef9d083b0348208cf9d5ff5c28c849"],
    ["page5","https://www.qianshanghua.com/api/page/comment/load?chat_id=e1f7ece99ebb482ebd32c7dcf108b127&comment_id="]
]

base_i=1
for url in urls:
    a = requests.get(url[1])
    a = a.text
    b = json.loads(a)
    l=[]
    for comment in b["comments"]:
        try:
            a_json = json.loads(comment[4])
        except:
            print("error:",url[0],comment[0])
            continue
        l.append(a_json)

    for i in range(0,len(l)):
        table.write(base_i+i,0,i)
        table.write(base_i+i,1,l[i]["shop-name"].split("\n")[0])
        table.write(base_i+i,2,l[i]["star"])
        table.write(base_i+i,3,l[i]["comment"])
        table.write(base_i+i,4,l[i]["consume"])
        table.write(base_i+i,5,l[i]["tel"])
        table.write(base_i+i,6,l[i]["address"])
        try:
            table.write(base_i+i,7,l[i]["coordinate"])
        except:
            table.write(base_i+i,7," ")
        try:
            table.write(base_i+i,8,l[i]["img"])
        except:
            table.write(base_i+i,8," ")
        excel.save("街舞.xls")
        print(i,l[i]["shop-name"])
    base_i=base_i+len(l)