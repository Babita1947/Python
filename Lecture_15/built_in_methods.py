s1 = {40, 10, 20, 30}
print(s1)

# The add method modifies s1 in place and returns None
s1.add(60) # add(int)
print(s1)

s1.add((11,22,33)) # add(iterable)
print(s1)

s1.update([1,2,3])  # update(iterable)
print(s1)

s2 = {'babita',19,11,2002,}
s2.update('XYZ','RWS')
print(s2)