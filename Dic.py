counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts: 
        counts[name] = 1
    else :
        counts[name] += 1
print(counts)

a = counts.keys()
b = counts.values()
c = counts.items()
print(a)
print(b)
print(c)