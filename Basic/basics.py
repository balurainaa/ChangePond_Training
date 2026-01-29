shape = "Rectangle"
length = 20
width = 14.4
isSquare = True

print(shape,type(shape))
print(length,type(length))
print(width,type(width))
print(isSquare,type(isSquare))


#operators in python

num1 = 10
num2 = 20
total = num1+num2
print(num1 ,"+", num2,"=",total)

temp  = num1
num1 = num2
num2 = temp

print("swapped num",num1,num2)

num1=num1+num2 
num2=num1-num2
num1=num1-num2

print("swapped num",num1,num2)

num1=num1*num2
num2=num1/num2
num1=num1/num2

print("swapped num",int(num1),int(num2))

remainder=10%6 #modulus
print(remainder)

divisible=10//4 #floor division 
print(divisible)

# control flow statement

#string

str="Hello World"

print("original str: ",str)
print("2nd character in str:",str[1])
print("entire string from 3rd char: ",str[3:])
print("entire str till 3rd char :",str[:4])
print("str starts from 3rd position to 7 th position:",str[3:8])
print("reverse str:",str[::-1])
print("find world in str: ",str.find("World"))
print("replace world with universe:",str.replace("World","Universe"))
print("-"*192)
print(str.split(" "))
print("no of in o Sstr:", str.count("o"))
print("length of str:",len(str))
print(" string in various cases",str.upper(),str.lower(),str.capitalize(),str.title())


