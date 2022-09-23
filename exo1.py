a = []
seq = "JDFCERTGHREDA"

a.append(5)
a.append(15)
a.append(2)
a.append(-6)
print(a)
a.remove(15)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

for base in seq:
    a.append(base)

print(a)
