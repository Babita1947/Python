# Write a python script to print two given words in dictionary order.

# print("Enter two numbers : ")
# x,y = input(),input()

# if x<y :
#     print(x,y)
# else :
#     print(y,x)

# For three words

print("Enter three numbers : ")
a,b,c = input(),input(),input()

if a<b<c :
    print(a,b,c)
elif a<c<b :
    print(a,c,b)
elif b<a<c :
    print(b,a,c)
elif b<c<a :
    print(b,c,a)
elif c<a<b :
    print(c,a,b)
else:
    print(c,b,a)
