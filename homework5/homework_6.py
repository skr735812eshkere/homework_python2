import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# гистограмма
# rng = np.random.default_rng(1)
# data = rng.normal(size = 1000)

# plt.hist(data,
#          bins = 30,
#          density=True,
#          alpha=0.5,
#          histtype='step',
#          edgecolor = 'red'
#          )
# plt.show()


# rng = np.random.default_rng(1)
# data = rng.normal(size = 1000)
#
# x1 = rng.normal(0, 0.8, 1000)
# x2 = rng.normal(-2, 1, 1000)
# x3 = rng.normal(3, 2, 1000)
#
# args = dict(alpha = 0.3, bins = 40)
# plt.hist(x1, **args)
# plt.hist(x2, **args)
# plt.hist(x3, **args)
#
# plt.show()

# rng = np.random.default_rng(1)
# data = rng.normal(size = 1000)
#
# x1 = rng.normal(0, 0.8, 1000)
# x2 = rng.normal(-2, 1, 1000)
# x3 = rng.normal(3, 2, 1000)
#
# print(np.histogram(x1, bins = 1))
# print(np.histogram(x1, bins = 2))
# print(np.histogram(x1, bins = 40))

# Двумерные гистограммы

# rng = np.random.default_rng(1)
#
# mean = [0,0]
# cov = [[1,1], [1,2]]
#
# x,y = rng.multivariate_normal(mean, cov, 10000).T
#
#
# plt.hist2d(x, y, bins = 30)
# cb = plt.colorbar()
# cb.set_label('point in interval')

# print(np.histogram2d(x, y, bins = 1))
# print(np.histogram2d(x, y, bins = 10))

# plt.show()

# Легенда

x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()

y = np.sin(x[:,np.newaxis] + np.pi * np.arange(0, 2 , 0.5))

plt.plot(x,y)

# ax.plot(x, np.sin(x), label='синус')
# ax.plot(x, np.cos(x), label='косинус')
# ax.plot(x, np.cos(x) + 2, label='косинус')
# ax.axis('equal')
# ax.legend(
#     frameon=True,
#     fancybox=True,
#     shadow=True
# )


plt.show()

