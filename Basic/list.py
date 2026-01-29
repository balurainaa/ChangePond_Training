# list is an array [ ]


cities=["chennai","Mumbai"]
cities.append("Goa")
print(cities)
cities.insert(1,"Banglore")
print(cities)
other_cities=["kochi","Trichy"]
#cities.extend(other_cities)
cities.extend(["kochi","Trichy"])
print(cities)
print("*"*10)

for c in cities:
    print(c)
cities.pop(2)
print(cities)

cities.sort()#default reverse=false
print(cities)
print("*"*10)
#cities.reverse()

for c in cities:
    print(c)
print("trichy is on",cities.index("Trichy")+1,
      "in the list")
print(len(cities))
print(cities.count("chennai"))
print(cities.remove("Trichy"))
      
print(cities.clear())
print(cities)
