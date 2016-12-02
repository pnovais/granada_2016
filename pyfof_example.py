import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pyfof

npts = 10000
data = np.vstack((np.random.normal(-1,0.2,(npts/2,2)),\
np.random.normal(1,0.2,(npts/2,2))))

groups = pyfof.friends_of_friends(data, 0.4)

colors = cm.rainbow(np.linspace(0, 1, len(groups)))
for g,c in zip(groups, colors):
    plt.scatter(data[g,0], data[g,1], color=c, s=3)

plt.show()
