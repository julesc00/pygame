
# A for loop to print numbers from 0 to 9
# for i in range(10):
#     print(i)
#
# j = 0
# while j < 10:
#     print(j)
#     j += 1


# in reverse
# k = 10
# while k > 0:
#     print(k)
#     k -= 1

# l = 1
# while l <= 2 ** 2:
#     print(l)
#     l *= 2

value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

val = 1
while val < 10:
    print(f"{val:.2e}")
    val += .10
