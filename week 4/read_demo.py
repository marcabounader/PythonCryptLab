"""with open('example.txt') as f:
    lines = f.readlines()
    for l in lines:
        print(l.strip())"""

"""import os

print(os.path.exists("example.txtt"))"""

"""s = "secret text"

print(s.upper())
print(s.capitalize())
print(s.startswith('s'))
print(s.endswith("t"))"""

import time
start = time.time()
total = sum(range(1,10000))
while total > 0:
    total -= 1000
end = time.time()
print(f"start: {start}, end: {end}")
print(f"duration of this script is: {end-start}")
