n = int(input("Enter how many element in array = "))
a = []
for i in range(n):
    num = int(input(f"Enter {i+1} element = "))
    a.append(num)

for i in range(n-1,-1,-1):
    print(a[i])
