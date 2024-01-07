# print(5+"5") # Give Error because of different type of data concatenate int + str

print("5"+"5")
print(str(5)+"5")
print(5+int("5"))
print("ABC"+"DEF","\n")

x = 4.5
print(int(x),"\n")

y = 5
print(float(x),"\n")

x = "234"
print(int(x),"\n")

# x = "abc"  # ValueError
# print(int(x))

# x = "2.4"  # ValueError
# print(int(x))

x = "3.4"
print(float(x))
print(complex(x),"\n")
print(bool(x))

x = 5
print(bin(x))
y = bin(x)
print(type(y))
print(oct(x))
print(hex(x),"\n")

print(ord("A"))
print(chr(65))