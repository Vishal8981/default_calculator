# list=[5,6,7,10]
# if 15 not in list:
#     print("no it is not in list")
#
# age=int(input("Enter the age of person"))
# if(age>18 or age==15):
#     print("they can vote")
# elif(age<18 ):
#     print("they cannot vote")
# else:
#     print("they are still cannot vote")

age=int(input("Enter the age of person"))
if(age>7 and age<100):
    if (age > 18 or age == 15):
        print("they can vote")
    elif(age<18 ):
        print("they cannot vote")

else:
    print("wrong input")
# default calculator
a=int(input("enter the first number:\n"))
b=int(input("second number:\n"))
c=input("Enter the sign among this +,/,*,- :\n")

if(a==5 and b== 6 and c=="*"):
    print("5*6=",31)
elif(a==10 and b==5 and c=="+"):
    print(" 10+5=16")
elif(c=="+"):
    print("sum of the two number",a+b)
elif(a==49 and b==7 and c=="/" ):
    print("49/7=",10)