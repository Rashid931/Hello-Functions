def factorial (n):
    """
    n: Any integer
    return factorial
    """
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial (n-1)

n = 6
print (f"The factorial of {n} is {factorial(n)}")

help (factorial)
