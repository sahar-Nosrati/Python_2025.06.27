import sys
from datetime import datetime
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# import camelcase


# xpoints = np.array([5,10,15,20,25])
# ypoints = np.array([0,10,15,20,25])
# # plt.plot(xpoints, ypoints, color = "#ab1465", linewidth = "2")
# plt.subplot(1,2 , 1)

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}


# plt.xlabel("Uv index")
# plt.ylabel("Time of day")
# plt.title("UV degree", fontdict= font1, loc="left")
# plt.grid(color="red", linestyle = "--")
# plt.plot(xpoints,ypoints)


# xpoints = np.array ([5,10,15,20,25])
# ypoints = np.array ([15,20,25,35,45])

# plt.subplot(1, 2, 2)

# plt.xlabel("Uv index")
# plt.ylabel("Time of day")
# plt.title("UV degree", fontdict= font1, loc="left")
# plt.grid(color="red", linestyle = "--")
# plt.plot(xpoints,ypoints)

# plt.suptitle("Annual UV index")
# plt.show()


xpoints = np.array([0,5,10,15,20])
ypoints = np.array([20,30,40,50,60])
plt.scatter(xpoints, ypoints)


xpoints = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
ypoints = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([100, 110, 120, 130, 140, 145, 150, 155, 160, 170, 180, 190, 200])
sizes = np.array([20, 5, 120, 80, 90, 100, 50, 500, 200, 60, 120, 10, 90])
# plt.scatter(xpoints, ypoints, color="#83e118")
plt.scatter(xpoints, ypoints, c=colors, cmap= "rainbow", s=sizes, alpha=0.5)
plt.colorbar()

plt.show()