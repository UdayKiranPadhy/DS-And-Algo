def plotloglogn():
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    xpoints = np.array([i for i in range(10, 1000)])
    ypoints = np.array([i*i for i in range(10, 1000)])
    plt.plot(xpoints, ypoints)
    plt.show()

plotloglogn()