cpdef saludo():
    print( "testiiiing")

def fib(n):

    a, b = 0, 1
    while b < n:
        a, b = b, a + b

    print(b,a)