num1=int(input())
num2=int(input())
opr =input("Choose a math operation (+, -, *, /, %, //): ")
def given_num(num1,num2,opr):
    if opr=="-":
        print (num1 - num2)
    if opr=="+":
        print (num1 + num2)
    if opr=="/":
        print (num1 / num2)
    if opr=="*":
        print (num1 * num2)
    if opr=="%":
        print (num1 % num2)
    else:
        print("Please enter a right operation")


    
given_num(num1,num2,opr)