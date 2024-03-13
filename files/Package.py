import matplotlib.pyplot as plt
import numpy as np


# x=[1,3,18]
# y=[1,4,7]
# plt.plot(x,y)
# plt.show()

x = np.arange(0,10,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.title("Sin(x)")
plt.show()