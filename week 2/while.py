x = 5
try:
    while x >=0:
        print(x)
        x -=1
    else:
        print(x)
    
except:
    print("error")


try: 
    print(5/0)
except ZeroDivisionError:
    print("i divided by zero")