# %%

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from pprint import pprint

# %%

# creating numpy lists
regular_list = [1, 2, 3, 4, 5, 6]

numpy_array = np.array(regular_list)
pprint(numpy_array)

# changing data types within arrays

float_array = np.array(regular_list, dtype=float)
pprint(float_array)

bool_array = np.array([0, 1, -1, 0, 0], dtype=float)
pprint(bool_array)

two_dimensional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pprint(two_dimensional_array)
# %%

# shape of arrays
pprint(f"shape of numpy array: {numpy_array.shape}")
pprint(f"shape of two dimensional array: {two_dimensional_array.shape} ")

# %%

# Numpy mathmatical operations

pprint(f"Original Array: {numpy_array}")
pprint("Adding 10")
pprint(f"{numpy_array + 10}")
pprint("Subtracting 10")
pprint(f"{numpy_array - 10}")
pprint("multiplying 10")
pprint(f"{numpy_array * 10}")
pprint("dividing 10")
pprint(f"{numpy_array / 10}")
pprint("modulus 3")
pprint(f"{numpy_array % 3}")
pprint("floor division 10")
pprint(f"{numpy_array // 10}")
pprint("squared")
pprint(f"{numpy_array ** 2}")

first_row = two_dimensional_array[0]
second_row = two_dimensional_array[1]
third_row = two_dimensional_array[2]

pprint(f"First row: {first_row}")
pprint(f"Second row: {second_row}")
pprint(f"Third row: {third_row}")

first_column = two_dimensional_array[:, 0]
second_column = two_dimensional_array[:, 1]
third_column = two_dimensional_array[:, 2]

pprint(f"First column: {first_column}")
pprint(f"Second column: {second_column}")
pprint(f"Third column: {third_column}")

pprint(two_dimensional_array)

first_two_rows_and_columns = two_dimensional_array[0:2, 0:2]
pprint(first_two_rows_and_columns)

# Reversing row and columns
pprint(two_dimensional_array[::-1, ::-1])

# %%

## Horitzontal Stack
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

pprint(np_list_one + np_list_two)

pprint(f"Horizontal Append: {np.hstack((np_list_one, np_list_two))} ")
pprint(f"Horizontal Append: {np.vstack((np_list_one, np_list_two))} ")

# Generate a random float  number
random_floats = np.random.random(5)
pprint(random_floats)

random_int = np.random.randint(2, 10, size=4)
pprint(random_int)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2, 10, size=(3, 3))
pprint(random_int)

# np.random.normal(mu (mean), sigma (standard deviation), size)
normal_array = np.random.normal(79, 15, 80)
pprint(normal_array)

# %%

# Plotting
sns.set_theme()
plt.hist(normal_array, color="grey", bins=50)

# creating list using range(starting, stop, step)
lst = np.arange(0, 11, 2)
pprint([l for l in lst])

# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
pprint(np.linspace(1.0, 5.0, num=10, endpoint=True))
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
pprint(np.logspace(1.0, 5.0, num=10, endpoint=True))

# %%

print(two_dimensional_array)
print("Minimum of each column:", np.amin(two_dimensional_array, axis=0))
print("Maximum of each column:", np.amax(two_dimensional_array, axis=0))
print("=== Row ==")
print("Minimum of each row:", np.amin(two_dimensional_array, axis=1))
print("Maximum of each row:", np.amax(two_dimensional_array, axis=1))

# %%

# Repeating sequences
a = [1, 2, 3]

# Repeat whole of 'a' two times
pprint(f"Tile: {np.tile(a, 2)}")

# Repeat each element of 'a' two times
pprint(f"Repeat: {np.repeat(a, 2)}")

# One random number between [0,1)
pprint(np.random.random())

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2, 3])
pprint(r)

pprint(np.random.choice(["a", "e", "i", "o", "u"], size=10))

# Random integers between [0, 10) of shape 2,5
pprint(np.random.randint(0, 10, size=[5, 3]))

# %%

np_normal_dis = np.random.normal(5, 0.5, 1000)
## min, max, mean, median, sd
print("min: ", np.min(np_normal_dis))
print("max: ", np.max(np_normal_dis))
print("mean: ", np.mean(np_normal_dis))
print("median: ", np.median(np_normal_dis))
print("mode: ", stats.mode(np_normal_dis))
print("sd: ", np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

# %%
# LINEAR ALGEBRA
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])

# Dot Product
pprint(np.dot(f, g))

# Matrix Multiplication
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]

### 1*5+2*7 = 19
pprint(np.matmul(h, i))

### 5*8-7*6np.linalg.det(i)
pprint(np.linalg.det(i))

# Plotting Linear Values
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5

plt.plot(temp, pressure)
plt.xlabel("Temperature in oC")
plt.ylabel("Pressure in atm")
plt.title("Temperature vs Pressure")
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# Plotting Gaussian Distribution

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.displot(x)
ax.set(xlabel="x", ylabel="y")
plt.show()
