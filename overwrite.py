"""x=u= 5
print("x:",x)
print("u:",u)"""
x=7
"""print("after")
print("x:",x)
print("u:",u)"""

def func ():
    global x
    x+=1 # x = x +1
    print(x)


func()

print(x)