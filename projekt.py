import numpy as np
import matplotlib.pyplot as plt
import math

X = np.array([[5,3],
    [10,15],
    [15,12],
    [24,10],
    [30,30],
    [85,70],
    [71,80],
    [60,78],
    [70,55],
    [80,91],])


labels = range(1, 11)
plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:,0],X[:,1], label='True Position')

# for label, x, y in zip(labels, X[:, 0], X[:, 1]):
#     plt.annotate(
#         label,
#         xy=(x, y), xytext=(-3, 3),
#         textcoords='offset points', ha='right', va='bottom')
# plt.show()


a = X.__len__()
Y = np.zeros((a,a));
#print(Y)
for i in range(a) :
    print(X[i,0],",", X[i,1])
    for j in range(a):
        print(((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)**0.5)
        Y[i,j] = ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)**0.5
    #print(Y[i,j])
print(Y)