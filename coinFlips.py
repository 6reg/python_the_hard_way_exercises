import random
results = []
hstreak = 0
tstreak = 0
totalstreak = 0

for i in range(10000):
    results = []

    for k in range(100):
        if random.randint(0,1) == 0:
            results += ['t']
        else:
            results += ['h']

for c in range(100):
    if results[c] == 't':
        #hstreak = 0
        tstreak += 1

        if tstreak == 6:
            totalstreak += 1
            tstreak = 0

    if results[c] == 'h':
        #tstreak = 0
        hstreak += 1

        if hstreak == 6:
            totalstreak += 1
            hstreak = 0

print('Chance of streak: %s%%' % (totalstreak / 100))
