# Slicing Operator ----> strobject[beg : end : step]

s1 = "mysirg"
# print(s1[0:5:1]) # mysir
# print(s1[0:6:1]) # mysirg
# print(s1[0:10:1]) # mysirg (not give error)
# print(s1[0:5:2]) # msr

# print(s1[1:5:3]) # yr
# print(s1[5:1:-1]) # gris


# By default slicing operator
# By default beg

print(s1[ :5:1]) # mysir
print(s1[ :0:-1]) # grisy

# By default end

print(s1[1: :1]) # ysirg
print(s1[5: :-1]) # grisym
print(s1[ : :-1]) # grisym
print(s1[ : : ]) # mysirg

