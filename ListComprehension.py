"""
# List Comprehension
x = 2
y = 2
z = 2
n = 2

l = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if ((i+j+k)!=n)]

print(l)
"""


"""
arr = [2, 3, 4, 66, 5, 7, 66, 7]
arr.sort()
b = []
for i in arr:
    if i not in b:
        b.append(i)

print(b[-2])
"""


