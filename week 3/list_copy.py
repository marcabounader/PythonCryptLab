import copy

l = [1,2,3,4]
l2 = l
l2[0] = "jp"

print(f"l2: {l2}")
print(f"l: {l}")

l3 = copy.deepcopy(l2)
l3[0] = "miguel"
print(f"l2: {l2}")
print(f"l2: {l3}")

print(id(l))
print(id(l2))
print(id(l3))