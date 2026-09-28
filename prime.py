num=int(input("Enter a number="))
flag=False
for i in range(2,num//2):
    if(num%i==0):
        flag=True
        break
if(flag):
    print("Number is not prime")
else:
    print("Number is prime")