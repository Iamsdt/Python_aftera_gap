import numpy as np

# 1 d array
arr = np.array([1, 2, 3])
print(arr)
print(arr.shape)
print("Size", arr.size)

print("\n")
# 2 d array
arr2 = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print("2D array")
print(arr2)
print(arr2.shape)
print("Size", arr2.size)

print("\n")
ran = np.random.random((2, 2))
print("Random")
print(ran)
print(ran.shape)
print("Size", ran.size)

print("\n")
x = np.random.random([1, 3])
y = np.random.random([1, 3])
print(x)
print(y)
print(type(x))
