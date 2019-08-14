import numpy as np
import matplotlib.pyplot as plt
import math

sampleNo = 1000
mu = 3
sigma = 0.1
np.random.seed(0)
s = np.random.normal(mu,sigma,sampleNo)
plt.subplot(141)
plt.hist(s,30,normed = True)
np.random.seed(0)
s = sigma * np.random.randn(sampleNo) + mu
plt.subplot(142)
plt.hist(s, 30, normed=True)
plt.show()

u = 0
u01 = -2
sig = math.sqrt(0.2)
x = np.linspace(u - 3*sig, u + 3*sig, 50)
y_sig = np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig)
print(x)
print("="*20)
print(y_sig)
plt.plot(x, y_sig, "r-", linewidth=2)
plt.grid(True)
plt.show()