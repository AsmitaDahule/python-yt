def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
    
res = factorial(5)
print(res)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fib = fibonacci(10)
print(fib)


n = 10
for i in range(n):
    print(fibonacci(i), end=" ")
