import requests
import json
import xlwt

excel = xlwt.Workbook(encoding='utf-8',style_compression=0)
table = excel.add_sheet('1',cell_overwrite_ok=True)
table.write(0,0,"序号")
table.write(0,1,"品牌")
table.write(0,2,"商品名称")
table.write(0,3,"商品编码")
table.write(0,4,"商品价格")
table.write(0,5,"商品促销")
table.write(0,6,"规格")
table.write(0,7,"商品详情数据")


urls=[
    # ["科颜氏","https://www.qianshanghua.com/api/page/comment/load?chat_id=4bb29d5be86d4a10a8cb94088e32ec87&comment_id="],
    # ["阿玛尼美妆","https://www.qianshanghua.com/api/page/comment/load?chat_id=2dc14ecbafe644a7affb555f0a61506a&comment_id="],
    # ["圣罗兰美妆","https://www.qianshanghua.com/api/page/comment/load?chat_id=5502c02efe2a45df9201b26350abc53c&comment_id="],
    # ["Margiela","https://www.qianshanghua.com/api/page/comment/load?chat_id=734f8d15323c423a9e4bc7869f92da11&comment_id="],
    # ["欧珑","https://www.qianshanghua.com/api/page/comment/load?chat_id=a6c2c271c1564a22be5fa3a2899eda81&comment_id="],
    # ["赫莲娜","https://www.qianshanghua.com/api/page/comment/load?chat_id=ecc1a5470a7443debbb3857842056191&comment_id="],
    # ["欧莱雅","https://www.qianshanghua.com/api/page/comment/load?chat_id=12089cab3040428bb3e1bf93c119cf3c&comment_id="],
    # ["薇姿","https://www.qianshanghua.com/api/page/comment/load?chat_id=303a1fa548124ef5a42a40eece25d678&comment_id="],
    # ["碧欧泉","https://www.qianshanghua.com/api/page/comment/load?chat_id=961f3c3dcffa4a009cfc5198aa7f3a41&comment_id="],
    # ["理肤泉","https://www.qianshanghua.com/api/page/comment/load?chat_id=bedb20a59a2e4c16a0c31f7ef3bbf153&comment_id="],
    # ["植村秀_new","https://www.qianshanghua.com/api/page/comment/load?chat_id=20499812e7ad4b87bdc219f9a623f57a&comment_id="],
    # ["圣罗兰","https://www.qianshanghua.com/api/page/comment/load?chat_id=73ce8eed412148b1a809ff7d58cddd24&comment_id="]
    # ["HR","https://www.qianshanghua.com/api/page/comment/load?chat_id=1058990d047144128384142bfe7e586e&comment_id="]
    ["植村秀_new","https://www.qianshanghua.com/api/page/comment/load?chat_id=f92416aca50f47e5be2085c9140c448b&comment_id="]
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
        table.write(base_i+i,1,l[i]["detail-box-title"])

        table.write(base_i+i,2,l[i]["product-name"])
        table.write(base_i+i,3,l[i]["product-code-value"])
        table.write(base_i+i,4,l[i]["price-now"])
        table.write(base_i+i,5,l[i]["promotion-item"])
        table.write(base_i+i,6,str(l[i]["property-item"].get("规格","")))
        table.write(base_i+i,7,str(l[i]["property-item"]))
        excel.save("植村秀_new.xls")
        print(i,l[i]["detail-box-title"])
    base_i=base_i+len(l)


