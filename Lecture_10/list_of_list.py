l1 = [[3,4,6],[10,20],[5,6,7]]
# print(l1[0])
# print(l1[1])

# print(l1[0][0])
# print(l1[1][1])
# print(l1[1][2]) #give error beacause of not exiting that index

for i in l1:
    for j in range(len(i)):
        print(i[j], end=" ")
    print("\n")


