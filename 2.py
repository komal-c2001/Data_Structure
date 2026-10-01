n = int(input("Enter how many element in array = "))
a = []
for i in range(n):
    num = int(input(f"Enter {i+1} element = "))
    a.append(num)

max = a[0]
min = a[0]

smax = a[0]
smin = a[0]

for b in a:
    if b > max:
        smax = max
        max =b
    elif b>smax and max!=b:
        smax=b
    if b < min:
        smin = min
        min = b
    elif b<smin and min!=b:
        smin=b

print("Second Largest number in array =", smax)
print("Second smallest number in array =", smin)
print("Largest number in array =", max)
print("Smallest number in array =", min)