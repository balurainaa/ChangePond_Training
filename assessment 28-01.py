"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).

Write a program which can compute the factorial of a given number

Reverse the given digit for eg:input - 14339 outpu - 93341

For a given string find out the number of vowels and number of consonant
"This is a python programming language it is highlevel"

For a given string count each number of vowels and print it
"This is a python programming language it is highlevel"
for eg: print output as  
a : count of a in string
e : count of e in string`
"""

""" ## 1
print("list of numbers which are divisible by 7 but not by 5")
for num in range(2000,3201):
      if(num%7==0 and num%5!=0):
          print(num)
    """
"""## 2
num=int(input("enter the number :1"))
fact=1
if(num==1 or num==0):
    print(fact,"is factorial of",num)
else:
  temp=num
  while(temp>1):
    fact=fact*temp
    temp=temp-1
  print(fact)
  """
## 3
"""
num=int(input("enter a number: "))
temp=num
rev=0
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp//=10
print(rev,"reversed number of",num)"""

##4

str="This is a python programming language it is highlevel".lower()
count_vowel=0
count_consonant=0
vowel=['a','e','i','o','u']
for i in str:
    if(i!=" "):
        if i in vowel:
            count_vowel+=1
        else:
            count_consonant+=1
print(count_vowel,"num of vowels in str.")
print(count_consonant,"num of consonant in str.")       
