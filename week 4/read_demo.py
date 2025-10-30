with open('example.txt') as f:
    lines = f.readlines()
    for l in lines:
        print(l.strip())