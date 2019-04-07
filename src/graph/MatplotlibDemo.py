import matplotlib.pyplot as plt

x = list(range(10))
y = list(range(0, 20, 2))
z = list(range(0, 30, 3))

plt.plot(x, y)
plt.plot(x, z)
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend(["Y Value", "Z value"])
plt.title("A simple graph")
plt.show()
