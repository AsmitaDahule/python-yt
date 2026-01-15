# a = 21 #global variable
# def age(a):
#     a=10  #local variable
#     print(a)

# age(a)


a = 2
def display():
    global a
    a = a+2
    print(a)

display()

print(a)