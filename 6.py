n = int(input("Enter how many element in array = "))
a = []
b=[]
for i in range(n):
    num = int(input(f"Enter {i+1} element = "))
    a.append(num)
for x in a:
    if x not in b:
        b.append(x)
print(b)

