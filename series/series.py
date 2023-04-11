def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    

def sum_series(n, n0=0, n1=1):
    if n < 0:
        return None
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)