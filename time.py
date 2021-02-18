#run at python 2.7.16

import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import FormatStrFormatter
from itertools import izip_longest
from distfit import distfit

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


n, bins, patches = plt.hist(x=time, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85) #bin -> x asis time window, n-> number of failure in y-axis
print n, bins
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time  to System Failure (Mins)')
plt.ylabel('Frequency (#)')
plt.text(130, 5, r'$\mu$P' + ' irradiated with '+ r'0.1 $\mu$'+'Ci source') #insert text in fig
plt.savefig('time.png')
plt.savefig('time.pdf')

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
