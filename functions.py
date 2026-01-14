def sayHello(name):
    return f"Hello, {name}!"

str = sayHello("asmi")
print(str)  # Output: Hello, asmi!

# arguments
# def sum(num1, num2):
#     sum = num1 + num2
#     print(sum)

# sum(2,3)

# def sum(num1, num2=5):
#     sum = num1 + num2
#     print(sum)

# sum(2)

# def sum(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#     print(sum)

# sum(1,2,3,4)

# def sum(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# sum(name="asmi", age=21, mail="asmi@gmail.in")


# def multi_return(name, city):
#     return name, city

# print(multi_return("asmi", "wani"))
