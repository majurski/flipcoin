import random
pol = []
otr = []

for i in random.sample(range(-100000,100000,1),20000):
    if i>=0:
        pol.append(i)
    else:
        otr.append(i)
    

print(len(pol), len(otr))
print(pol)