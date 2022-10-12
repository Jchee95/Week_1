import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(5, 15, 11)
b = np.linspace(0, 23, 8, endpoint = False)[1:]

print("Exerise 1", a) # Part 2 exercise 1
print("Exerise 2", b) # Part 2 exercise 2

x = np.arange(-1, 1, 0.5); # Part 2 exercise 3
plt.hist(x, bins = 10)
plt.show() # Part 2 exercise 4

# outputs single integer value in a 1x10 array
c = np.random.randint(1, 100, (1, 10))
# outputs single integer value in a 1x10 array
d = np.random.randint(1, 100, (1, 10)) 

print("Exerise 5.1", c)
print("Exerise 5.2", d)

# subtracting both the vectors and applying linear algebra 
dist = np.linalg.norm(d-c)

# printing Euclidean distance
print("Exerise 5.3", dist)