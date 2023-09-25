def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

for i in range(1,11):
    print(factorial(i))