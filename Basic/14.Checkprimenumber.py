num = 29

flag = False

if num==1:
    print("1 is neither prime nor composite")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            flag = True
            break

if flag:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")