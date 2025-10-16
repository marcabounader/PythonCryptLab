a = 10
b = 10

print(f"a = b? {a == b}")
print(f"a >= b? {a >= b}")
print(f"a <= b? {a <= b}")
print(f"a != b? {a != b}")


age = int(input("enter your age:\n"))
print("age ",str(age+1))

if age < a:
    print(f"{age} is smaller than {a}")
elif age > a:
    print(f"{age} is bigger than {a}")
else:
    print(f"{age} is equal than {a}")