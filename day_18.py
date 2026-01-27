def avg(a,b):
    print("average is ", (a+b)/2 )
    print(a,b)


avg(b=10, a=5)


def sum(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("sum is ", sum)
    print(type(numbers))

sum(1,2,3,4,5,6,7,8,9,10)