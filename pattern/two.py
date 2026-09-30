n=5
for i in range(n):
    for j in range(n):
        if i+j==j or i+j==i or i==n-1 or j==n-1:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()