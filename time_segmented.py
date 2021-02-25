#run at python 2.7.16

import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import FormatStrFormatter
# from itertools import izip_longest

#%%
'''plotting properties in this block'''
plt.clf()

plt.style.use('classic')


def param_default():
    params = {
    'legend.fontsize'       : 14        ,
    'font.family'           : 'sans-serif'        ,
#    'mathtext.fontset'      : 'stixsans'      ,
    'figure.figsize'        : (7, 4),
    'axes.labelsize'        : 14        ,
    'axes.titlesize'        : 14        ,
    'axes.labelpad'         : 1         ,
#    'axes.titleweight'      : 'bold'    ,
    'font.size'             : 14            ,
#    'font.weight'           : 'bold'    ,
    'xtick.major.size'      : 1         ,
    'xtick.major.width'     : 1        ,
    'xtick.labelsize'       : 14.0      ,
    'xtick.direction'       : 'out'     ,
    'ytick.major.size'      : 1         ,
    'ytick.major.width'     : 1         ,
    'ytick.labelsize'       : 14.0      ,
    'ytick.direction'       : 'out'     ,
    'xtick.major.pad'       : 2.0         ,
    'xtick.minor.pad'       : 0.0         ,
    'ytick.major.pad'       : 2.0         ,
    'ytick.minor.pad'       : 0.0         ,
#    'savefig.dpi'           : 1040      ,
#    'figure.dpi'            : 300       ,
#    'axes.linewidth'        : 0.5       ,
#    'axes.labelweight'      : 'bold'    ,
    'axes.grid'             : False      ,
    'figure.facecolor': 'white',
    'figure.edgecolor': 'white',
    'lines.linewidth'       : 2.0       ,
#    'text.usetex'           : True     ,
    'text.latex.unicode'    : False     ,
    'legend.framealpha'     : 0.1       ,
    'figure.autolayout'     : True      ,
    'axes.xmargin':0.02,
    'axes.ymargin':0.02,
    }

    plt.rcParams.update(params)

param_default()


time=[254, 11, 4, 3.5, 1.8, 3.6, 4.5, 4.3, 59, 17, 338, 40, 6.85, 58] # time to failure data


# Here is where we plot the different fault types: To do so, add the necessasry numbers to the
# corresponding positions that match the 'time' array above. For example, the first position of each
# 'bars' array (0 1 0) plots the bar on the histogram at time = 254
bars1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 2]
bars2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0]
bars3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1]

# This function is needed for stacking the 3rd on top of the previous w
bars = np.add(bars1, bars2).tolist()

# Bar width: change as desired
rwidth = 30

# ****************************************************************************************************************
# Original Histogram Plot Implementation
# ****************************************************************************************************************
# n, bins, patches = plt.hist(x=time, bins='auto', color='#0504aa',
#                             alpha=0.7, rwidth=0.85) #bin -> x asis time window, n-> number of failure in y-axis

# ****************************************************************************************************************
# Segmented Histogram Plot
# ****************************************************************************************************************

# Below are the functions used to actually create the histogram bars from the arrays above

# Create brown bars
plt.bar(time, bars1, color='#7f6d5f', edgecolor='white', width=rwidth)

# Create green bars (middle), on top of the firs ones
plt.bar(time, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=rwidth)

# Create green bars (top)
plt.bar(time, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=rwidth)


# Rest of labeling. Here is where you could add in a legend to describe the colors
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time  to Failure (Mins)')
plt.ylabel('Fault Count (#)')
plt.text(130, 5, r'$\mu$P' + ' irradiated with '+ r'0.1 $\mu$'+'Ci source') #insert text in fig
plt.xlim(-10,350)
plt.savefig('time.png')
plt.savefig('time.pdf')
plt.show()


# N = 5
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (25, 32, 34, 20, 25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
# ind = np.arange(N)    # the x locations for the groups
# width = 0.35       # the width of the bars: can also be len(x) sequence
#
# p1 = plt.bar(ind, menMeans, width, yerr=menStd)
# p2 = plt.bar(ind, womenMeans, width,
#              bottom=menMeans, yerr=womenStd)
#
# plt.ylabel('Scores')
# plt.title('Scores by group and gender')
# plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('Men', 'Women'))
#
# plt.show()

#Trial Poisson Fit
#def poisson_pmf(k, lam):
#    return (lam**k*np.exp(-lam)) / np.math.factorial(k)
#
#
#
#x_rvs=pd.Series(poisson.rvs(22, size=100000, random_state=2))
#data=x_rvs.value_counts().sort_index().to_dict()
#fig, ax= plt.subplots()
#ax.bar(range(len(data)), list(data.values()), align='center')
#plt.xticks(range(len(data)), list(data.keys()))

plt.show()
