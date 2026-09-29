
n = int(input("Enter how many element in array = "))
a = []
for i in range(n):
    num = int(input(f"Enter {i+1} element = "))
    a.append(num)
num=int(input("Enter search element="))
flag=0
for i in range(n):
    if(a[i]==num):
        print(f'number is present in the array at position {i}')
        flag=1
        break
if(flag==0):
    print("Number is not present in the array")
    

    
