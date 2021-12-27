import json
with open('doudian_user_ids(1).json','r',encoding='utf8')as f:
    json_data = json.load(f)
    print(json_data)