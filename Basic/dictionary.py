# dictionary is a key value pair

{ }

profile = {"Name":"Balu","Age":22,"Gender":"M","isMarried":False}
print(profile)

print("age of",profile["Name"],"is",profile["Age"])

for k in profile.keys():
    print(k)

for v in profile.values():
    print(v)

print("*"*30)
    
for (k,v) in profile.items():
    print(k,"is",v)
print("*"*40)

profile["city"]="pune"
print(profile)

profile["Age"]=23
print(profile)

#to print specific item in list

print(profile.get("Name"))

profile.pop("Name")
print(profile)
profile.popitem()
print(profile.popitem())

profile.clear()
print(profile)
