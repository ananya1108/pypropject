a=54
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("CALCULATOR")
print("Choose operation")
print("1)Addition\n"
      "2)Subtraction\n"
      "3)Multiplication\n"
      "4)Division\n")
select=input("choose from 1,2,3,4\n")
num1 = int(input("first number="))
num2 = int(input("second number="))
if select=="1":
    print(num1, "+", num2, "=", add(num1, num2))
elif select=="2":
    print(num1,"-",num2,"=",sub(num1,num2))
elif select=="3":
    print(num1,"*",num2,"=",mul(num1,num2))
elif select=="4":
    print(num1,'/',num2,'=',div(num1,num2))
else:
    print("invalid input")


