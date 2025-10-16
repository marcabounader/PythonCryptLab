y=7
def func (x):
    global y
    y += 1
    print(x)
    print(y)
    def func2 ():
        global y
        y += 1
        print(y)
    func2()


func(4)

print(y)