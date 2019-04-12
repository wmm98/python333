import matplotlib.pyplot as plt
# plt.xlim(xmax=6, xmin=0)
# plt.ylim(ymax=7, ymin=0)
plt.yticks([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])
plt.xticks([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
plt.xlabel("x")
plt.ylabel("y")
plt.plot([1, 2, 3, 4, 5], [2, 3.1, 3.8, 5.1, 6], 'ro')
plt.show()
