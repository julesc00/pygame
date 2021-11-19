
# reverse countdown

# for i in range(10, 0, -1):
#     print(i)
# print("And lift off!")

# for i in [2, 6, 4, 2, 6, 7, 4]:
#     print(i)
#
# for i in range(3):
#     print("a")
# for j in range(3):
#     print("b")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("Done")


# Keep a running total
total = 0
for i in range(5):
    new_num = int(input("Enter a number: "))
    total += new_num
print("The total is: ", total)
