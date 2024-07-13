num = 7

factorial = 1

if num<0:
    print("Factorial does not exist for negative numbers")

elif  num == 0:
    print("The factorial of 0 is 1")

else:
    for i in range(1,num+1):
        factorial = factorial*i

    print("The factorial of",num,"is",factorial)

## Recursion

def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

n = 7

result = recur_factorial(n)
print("Recursion Factorial",result)