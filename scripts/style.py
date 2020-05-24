import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (5, 5),
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.style.use('dark_background')

np.set_printoptions(precision=2, suppress=True)