#calculator
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b


def divide(a,b):
    if b == 0:
        return "undefined"
    return a/b  

flag = "yes"
while flag == "yes":
    sign = input("enter sign (+/-/*/ /): ")
    if sign in ["+","-","*","/"]:
        number1 = int(input("enter 1st value: "))
        number2 = int(input("enter 2nd value: "))
        if sign == "+":
                print(add(number1,number2))

        elif sign == "-":
                print(sub(number1,number2))
        elif sign == "*":
                print(mul(number1,number2))

        elif sign == "/":
                print(divide(number1,number2))

    else :
        print("enter valid sign")
    
    flag = input("do you want to continue (yes/no): ")
    
    

    