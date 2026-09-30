s=input("Enter a string=")
sub=input("Enter a substring=")
count=0
for i in range((len(s)-len(sub)+1)):
    if s[i:i+len(sub)]==sub:
        count+=1
print("Total substring in given string=",count)