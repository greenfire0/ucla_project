import json



##this takes 2 files and adds them together

f = open("super.json")
c = open("art3yy.json")
try:
    data = json.load(f)
    print("hi")
except Exception as e:
    print('error:', e)
    print("hi")
try:
    data2 = json.load(c)
    print("hi")
except Exception as e:
    print('error:', e)
    print("hi")
    



for a in data2['games']:
    data['games'].append(a)


print(data)


with open("out.json", "w") as outfile:
    json.dump(data, outfile)

#print(data['games'])

#yo = []
#print(list(data.keys())[0])
#for pizza in data["games"]:
#    yo.append(pizza.get("drop_coordinates"))
#print(yo)