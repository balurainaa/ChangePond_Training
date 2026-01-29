"""
1.leap year program
*year should be divisible by 400

* year should be divisible 4 but not by 100
"""

year=2026

"""if(year % 400  == 0):
    print(year,"is leap year")
else:
    if(year %100!= 0):
        if(year%4 ==0):
            print(year,"is leap year")
        else:
            print(year,"is not leap year")
            """
"""
if(year%400==0):
    print(year,"is leap year")

elif(year%100!=0 and year%4==0):
    print(year,"ia leap year")
else:
    print(year,"is not leap year")

 """
"""
if(year%400==0 or (year%100!=0 and year%4==0)):
    print(year,"is leap year")
else:
    print(year,"is not leap year")

"""

start_y = int(input("enter the starting year:"))
end_y= int(input("enter the ending year:"))
print("list of leap year")
for year in range(start_y,end_y):
          if(year%400==0 or (year%100!=0 and year%4==0)):
            print(year)
