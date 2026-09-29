n = int(input("Enter how many element in array = "))
a = []
for i in range(n):
    num = int(input(f"Enter {i+1} element = "))
    a.append(num)
ecount=0
ocount=0
for b in a:
    if(b%2==0):
        ecount+=1
    else:
        ocount+=1
print("Count even numbers in array=",ecount)
print("Count odd number in array=",ocount)
