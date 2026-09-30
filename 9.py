s=input("Enter a string=")
v=0
c=0
d=0
sc=0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v+=1
        else:
            c+=1
    elif ch.isdigit():
        d+=1
    else:
        sc+=1
print("Vowels=",v)
print("Consonants=",c)
print("Digits=",d)
print("Special Characters=",sc)