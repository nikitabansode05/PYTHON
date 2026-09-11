import json 

f=open('data.json')
data=json.load(f)
for i in data['user_details']:
    print(i)
    
f.close()