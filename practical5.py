import random

# 1. Create an Array
arr = [1, 2, 3, 4, 5]
print("Array:", arr)


# 2. Zeros, Ones, Full and Random

zeros = [[0 for j in range(2)] for i in range(2)]
ones = [[1 for j in range(3)] for i in range(3)]
full = [[7 for j in range(2)] for i in range(2)]
random_arr = [[random.random() for j in range(2)] for i in range(2)]

print("\nZeros:\n", zeros)
print("Ones:\n", ones)
print("Full:\n", full)
print("Random:\n", random_arr)


# 3. Indexing, Slicing and Reshaping

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print("\nElement:", arr[1][2])

print("Slice:", [row[1:3] for row in arr[0:2]])

new_arr = [item for row in arr for item in row]
print("Reshaped:", [new_arr])


# 4. Addition, Multiplication, Mean and Sum

a = [1, 2, 3]
b = [4, 5, 6]

addition = [a[i] + b[i] for i in range(len(a))]
multiplication = [a[i] * b[i] for i in range(len(a))]
mean = sum(a) / len(a)
total = sum(b)

print("\nAddition:", addition)
print("Multiplication:", multiplication)
print("Mean:", mean)
print("Sum:", total)
