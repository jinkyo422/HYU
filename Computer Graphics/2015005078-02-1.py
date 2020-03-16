import numpy as np

a = np.arange(2, 27)
print(a)
print()

a = a.reshape(5,5)
print(a)
print()

a[1:4, 1:4] = 0

print(a)
print()
    
b = a@a
print(b)
print()

b = b[0, :]
b = b*b
x = 0
for i in range(0,5):
    x += b[i]

x = np.sqrt(x)
print(x)
