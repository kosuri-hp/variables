#1
num=int(input("Enter a number:"))
if num>0:
    print("postive")
elif num==0:
    print("Zero")
else:
    print("Negative")
# 2nd
num1=18
if num1%2==0:
    print("positive")
else:
    print("Negative")
#3rd
age=18
if age >= 18:
    print("eligible to vote")
else:
    print("Not eligible to vote")
# 4th
num4=int(input("Enter a number:"))
num5=int(input("Enter a number:"))
if num4 > num5:
    print("The greatest number is num4:",num4)
elif num5 > num4:
    print("The greatest number is num5:",num5)
# 5th
num6=int(input("Enter a number:"))
if num6 > 40:
    print("He is pass")
else:
    print("He is fail")
# 6th
num7=int(input("enter a number:"))
if num7==1:
    print("Monday")
elif num7==2:
    print("Tuesday")
elif num7==3:
    print("wednesday")
elif num7==4:
    print("Thursday")
elif num7==5:
    print("friday") 
elif num7==6:
    print("saturday")   
elif num7==6:
    print("sunday")   
else:
    print("Invalid input")
#7th
num=18
output="nvvu undu " if num >= 18  else "nuvu vellu"
print(output)
# 8th
operation=input("Enter a operation:").lower()
num=15
num2=20
if operation =="add":
      print(num+num2)
elif operation =="sub":
      print(num-num2)
elif operation =="mul":
      print(num*num2)
elif operation =="div":
      if num==0:
            print("Divisible not possible") #edge cases
      else:
            print(num/num2)  