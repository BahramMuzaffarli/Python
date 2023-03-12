import numpy as np

a = np.array([[1, 0], [0, 1]])
b = np.array([[1, 2], [3, 4]])

# compute the multiplication of the following matrices
print("a * b = ")
# multiply a and b
print(a * b)
print()

# Generate an array of length 3n filled with the cyclic pattern 1, 2, 3.
n = 3
print("np.tile([1, 2, 3], 3) = ")
# call np.tile
print(np.tile([1, 2, 3], n))
print()
# Create a 10×10 matrix of zeros and then "frame" it with a border of ones.
c = np.zeros((10, 10))

# set the border of c to 1
c[0, :] = 1
c[-1, :] = 1
c[:, 0] = 1
c[:, -1] = 1
print("10x10 matrix with border of ones = ")
print(c)
print()

# Create a random 3×5 array using the np.random.rand(3, 5) function and compute: the sum of all the entries, the sum of the rows and the sum of the columns.
print("np.random.rand(3, 5) = ")
# store the random array in d
d = np.random.rand(3, 5)
# print d
print(d)
# print the sum of all the entries
print(d.sum())
# print the sum of the rows
print(d.sum(axis=0))
# print the sum of the columns
print(d.sum(axis=1))
print()


# Given the following arrays representing logical values (0 = False, 1 = True) compute the logical AND and logical OR operations for every pair of values of the two arrays: [1, 1, 0, 0] [1, 0, 1, 0] Hint: you may need to set the data type (dtype) of the array's elements to 'bool'
e = np.array([1, 1, 0, 0], dtype=bool)
f = np.array([1, 0, 1, 0], dtype=bool)

print("Array 1 = ", e)
print("Array 2 = ", f)
print("Logical AND = ")
# print the logical AND
print(np.logical_and(e, f))
print()

# Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]
g = np.array([1, 2, 0, 0, 4, 0])
print("Indices of non-zero elements in [1, 2, 0, 0, 4, 0] =")
# print the indices of non-zero elements
print(np.nonzero(g))
print()

# Create a 8×8 array with random values and find minimum and maximum value
h = np.random.rand(8, 8)
print("8x8 array with random values = ")
print(h)
print("Minimum value:", h.min())
print("Maximum value:", h.max())
print()

# Create a 8×8 array with random natural values from the range (1-100) on the diagonal, other values should be 0. Hint: You can use numpy's 'eye' function.
i = np.eye(8, 8)
# set the diagonal of i to random natural values
i = i * np.random.randint(1, 100, (8, 8))
print("8x8 array with random natural values on the diagonal = ")
print(i)
print()


# Write a function which creates an n×n matrix with (i,j)-entry equal to i+j.



# Write a function which creates an n×n matrix with rows having subsequent values multiplied by the row's number. For example for n = 4:
# [[0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9], [0, 4, 8, 12]]
def create_matrix2(n):
    row = np.array([i for i in range(n)])
    return np.array([row * (i+1) for i in range(n)])


print("n x n matrix with rows having subsequent values multiplied by the row's number = ")
# print the matrix
print(create_matrix2(4))
