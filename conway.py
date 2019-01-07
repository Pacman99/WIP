import random

map = []

size = [5,5]
for i in range(size[0]):
    nrow = []
    for n in range(size[1]):
        l = random.randint(1,101)
        if l <= 50:
            nrow.append(False)
        else:
            nrow.append(True)
    map.append(nrow)

while True:
    for l in map:
        for i in map:
           print(l,i)
