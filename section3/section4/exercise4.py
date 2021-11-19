
# reverse countdown

for i in range(10, 0, -1):
    print(i)
print("And lift off!")

for i in [2, 6, 4, 2, 6, 7, 4]:
    print(i)

for i in range(3):
    print("a")
for j in range(3):
    print("b")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("Done")


# # Keep a running total
# total = 0
# for i in range(5):
#     new_num = int(input("Enter a number: "))
#     total += new_num
# print("The total is: ", total)


# # Sum all numbers
sum2 = 0
for i in range(1, 101):
    sum2 += i
print(sum2)


# total of zeros
# def get_total_zeros():
#     totale = 0
#     for item in range(5):
#         new_number = int(input("Enter a number: "))
#         if new_number == 0:
#             totale += 1
#     print("You entered a total of ", totale, "zeros")


# get_total_zeros()

# Value of a
a = 0
for i in range(10):
    a += 1
print(a)

b = 0
for i in range(10):
    b += 1
for j in range(10):
    b += 1
print(f"B times: {b}")

c = 0
for i in range(10):
    c += 1
    for j in range(10):
        c += 1
print(c)

for i in range(10):
    print(i + 1)

# print even numbers
for i in range(2, 12, 2):
    print(i)

# print even numbers
for i in range(5):
    print((i + 1) * 2)

# Count down from 10 down to 1 (not zero)
for i in range(10, 0, -1):
    print(i)

# Print items out of a list
for i in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(i)
