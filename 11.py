s=input("Enter a string=")
result=" ".join(word[::-1] for word in s.split())
print(result)
