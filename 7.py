n = int(input("Enter how many element in array = "))
a = []
for i in range(n):
    num = int(input(f"Enter {i+1} element = "))
    a.append(num)
j=0
for i in range(n):
    if (a[i]!=0):
        a[i],a[j]=a[j],a[i]
        j+=1
print(a)