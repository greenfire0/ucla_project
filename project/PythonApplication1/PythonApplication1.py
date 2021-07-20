import json



#data  = json.loads(games)
f = open("test.json")

try:
    data = json.load(f)
    print("hi")
except Exception as e:
    print('error:', e)
    print("hi")
    



#print(data['games'])

yo = []
print(list(data.keys())[0])
for pizza in data["games"]:
    print(pizza.get("drop_coordinates"),pizza.get("key"))
print(yo)