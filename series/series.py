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
    

def sum_series(n, val0=0 ,val1=1):

    if (val0==0 and val1==1):
        return fibonacci(n)

    else :
        return lucas(n)
    