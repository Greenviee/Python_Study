import random
import matplotlib.pyplot as plt

x_list = []
y_list = []
x_circle = []
y_circle = []
n = 100000
for _ in range(n):
    x = random.random()
    y = random.random()
    x_list.append(x)
    y_list.append(y)
    if np.sqrt(x**2 + y**2) <= 1:
        x_circle.append(x)
        y_circle.append(y)
plt.figure(figsize(10, 10))
plt.scatter(x_list, y_list)
plt.show()