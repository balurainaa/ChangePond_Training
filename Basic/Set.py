temp_mon={99.6,101.5,"balu",100,99.7,101}
print(temp_mon)

temp_tue={99.6,101.5,98.6,100,95.6}

print(temp_mon.union(temp_tue))

print(temp_mon.intersection(temp_tue))

temp_mon.add(7)
print(temp_mon)

print(temp_mon-temp_tue)
print(temp_tue-temp_mon)
