# ********* set comprehension ***********
# s  = input("Enter a string : ")
# s1 = {e for e in s if e in "aeiou"}
# print(s1)


# or 
s2 = set()
for e in (input("Enter a string : ")):
   
    if e in "aeiou":
        s2.add(e)
print(s2)