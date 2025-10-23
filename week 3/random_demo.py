import random
"""for i in range(1,10000):
    random.seed(i)
    print(random.randint(1,100))
"""

l = [1,2,3,4]
l2 = ["hello","yay","ok"]

print(l.insert(1,'2'))

print(l.append(l2))
print(l[-1][0])

print(l)
print(random.shuffle(l))
print(l)