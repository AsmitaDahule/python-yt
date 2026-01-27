l = [1,5,8,7,4,9]
print(l)

l.append(99)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(99))
print(l)

# m = l
# m[0] = 100
# print(l)
# print(m)

m = l.copy()
m[0] = 100
print(l)

l.insert(0, 500)
print(l)

m = [10,20,30]
l.extend(m)
print(l)



k = l + m
print(k)