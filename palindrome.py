num=int(input("Enter a number="))
rev=0
temp=num
while(num>0):
    rev=(rev*10)+num%10
    num=num//10
if(temp==rev):
    print("Number is palindrome")
else:
     print("Number is not palindrome")
    