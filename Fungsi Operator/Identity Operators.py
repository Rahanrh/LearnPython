l1 = [1, 2, 3]

l2 = l1

print(l1 is l2)  # return true because both are refer same object

l3 = [1, 2, 3]

print(l1 is l3)  # return False because lists are mutable in Python
print(l1 is not l2)
