# Has the same id
a = [1, 2, 3]
c = a
print(id(a), id(c))

# Has a different id
b = 42
print(id(b))
b = '42'
print(id(b))
