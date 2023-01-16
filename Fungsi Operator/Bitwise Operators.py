# OR
a = 2  # in binary 2 = 1 0
b = 3  # in binary 3 = 1 1
c = a | b  # perform OR-> 1 1 (any one value is one then output is one)

print("OR", c)  # output: 1 1 (in binary) which is equal to 3


# AND
d = a & b

# 2    # 1 0
# 3    # 1 1
# AND   1 0  (in AND operation output is one if and only if both the value is 1)
print("AND", d)


# XOR
# (if one input is one thne output is one)

e = a ^ b
# 1 0
# 1 1
# 0 1
print("XOR", e)
