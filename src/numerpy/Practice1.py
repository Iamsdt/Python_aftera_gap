import numpy as np

# print version and config
# print(str(np.__version__))
# np.show_config()

# Create a null vector of size 10
b = np.zeros(10)
# print(b)

# change the fifth as 5
b[4] = 5
# print(b)

# Create vector 10 49
v = np.arange(10, 50)
# print(v)

# reverse a vector
b = np.arange(10, 18)
# print(b)
b = b[::-1]
# print(b)

#  Create a 3x3 matrix with values ranging from 0 to 8
z = np.arange(9).reshape(3, 3)
# print(z)

# Find indices of non­zero elements from [1,2,0,0,4,0]
nz = np.nonzero([1, 2, 0, 0, 4, 0])
# print(nz)

# Create 3 x 3 identity matrix
z = np.eye(3)
# print(z)

# Create a 3x3x3 array with random values
z = np.random.random((3, 2, 2))
# print(z)

# 12 Create a 10x10 array with random values and find the minimum and maximum values
z = np.random.random((10, 10))
min, max = z.min(), z.max()
# print(min, max)

# 13 Create a random vector of size 30 and find the mean value
z = np.random.random(30)
m = z.mean()
print(m)

# 14 Create a 2d array with 1 on the border and 0 inside
z = np.ones((10, 10))
z[1:-1, 1:-1] = 0
print(z)
print(type(z))
