import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 25)

linearSearch = x
jumpSearch = np.sqrt(x)
binarySearch = np.log2(x)
ternarySearch = np.emath.logn(3, x)

plt.plot(x, linearSearch, label="Linear Search", color='blue')
plt.plot(x, jumpSearch, label="Jump Search", color='green')
plt.plot(x, binarySearch, label="Binary Search", color='red')
plt.plot(x, ternarySearch, label="Ternary Search", color='purple')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.show()