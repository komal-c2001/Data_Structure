n=9
for i in range(n):
    for j in range(n):
        if i+j==4 or j-i==4 or i-j==4 or i+j==12:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()