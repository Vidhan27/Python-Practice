a=2
b=3
c=4

s=(a+b+c)/2 #s is the semiperimeter
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("The area of the triangle is %0.2f" %area)