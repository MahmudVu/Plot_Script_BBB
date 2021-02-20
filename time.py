#run at python 2.7.16

import numpy as np
import matplotlib.pylab as plt
from scipy.stats import norm
from scipy.stats import poisson
from scipy.optimize import curve_fit
from scipy.special import gammaln # x! = Gamma(x+1)
from scipy.special import factorial
from matplotlib.ticker import FormatStrFormatter

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

# Main data array
time=[254, 11, 4, 3.5, 1.8, 3.6, 4.5, 4.3, 59, 17, 338, 40, 6.85, 58] # time to failure data


# Below are the 2 implementations of poisson/histogram fit generation


# ***************************************************************************************************************************
# VERSION 1
# ***************************************************************************************************************************
#
# This is the best version I have been able to come up with. The plot uses the original x-axis but normalized the y-axis
# or frequency axis to scale from 0-0.1, rather than 0-10 (this can be changed if desired)
#
# This implementation also includes plots of both normal and poisson distributions on the data given in the histogram.
# This is the best fit I have been able to achieve thus far

# Perform jacobian transformation computation for poisson
def transformation_and_jacobian(x):
    return 1./x, 1./x**2.

# Generate normal distribution from data
def tfm_normal_pdf(x, lam):
    y, J = transformation_and_jacobian(x)
    return norm.pdf(y, lam, np.sqrt(lam)) * J

# Generate poisson distribution from data
def tfm_poisson_pdf(x, mu):
    y, J = transformation_and_jacobian(x)
    return np.exp(y * np.log(mu) - mu - gammaln(y + 1.)) * J

# Call histogram plot on data
hist, bins = np.histogram(time, bins=50, density=True)

# Generate width and center values, normalize dataset as needed for normal dist
# Note that this normalization is done for the normal distribution: if only poisson is desired,
# you can remove this
width = 0.8*(bins[1]-bins[0])
center = (bins[:-1]+bins[1:])/2
plt.bar(center, hist, align='center', width=width, label = 'Normalised data')

# Choose starting point for normal dist
p0 = 1 / np.mean(time)

# Fit the fitted versions of the normal and poisson distributions onto the histogram
norm_opt, _ = curve_fit(tfm_normal_pdf, center, hist, p0=p0)
pois_opt, _ = curve_fit(tfm_poisson_pdf, center, hist, p0=p0)

# Plot everything together
plt.plot(center, tfm_normal_pdf(center, *norm_opt), 'g--', label='Normal Fit (post-transformation)')
plt.plot(center, tfm_poisson_pdf(center, *pois_opt), 'r--', label='Poisson Fit (post-transformation)')

plt.legend()
plt.show()

# ***************************************************************************************************************************
# VERSION 2
# ***************************************************************************************************************************
#
# This is a poisson attempt on the original plot of data. The only things plotted is the histogram
# and the originally given histogram. The y-axis is on a scale of 0-10 for frequency

#
# entries, bin_edges, patches = plt.hist(x=time, bins='auto', color='#0504aa',
#                             alpha=0.7, rwidth=0.85) #bin -> x asis time window, n-> number of failure in y-axis
# print(entries, bin_edges)
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('Time  to System Failure (Mins)')
# plt.ylabel('Frequency (#)')
# plt.text(130, 5, r'$\mu$P' + ' irradiated with '+ r'0.1 $\mu$'+'Ci source') #insert text in fig
# plt.savefig('time.png')
# plt.savefig('time.pdf')
#
#
# # # the bins should be of integer width, because poisson is an integer distribution
# # bins = np.arange(11) - 0.5
# # entries, bin_edges, patches = plt.hist(time, bins=bins, density=True, label='Data')
#
# # calculate bin centres
# bin_middles = 0.5 * (bin_edges[1:] + bin_edges[:-1])
#
#
# def fit_function(k, lamb):
#     '''poisson function, parameter lamb is the fit parameter'''
#     return poisson.pmf(k, lamb)
#
# def transformation_and_jacobian(x):
#     return 1./x, 1./x**2.
#
# def tfm_poisson_pdf(x, mu):
#     y, J = transformation_and_jacobian(x)
#     # For numerical stability, compute exp(log(f(x)))
#     return np.exp(y * np.log(mu) - mu - gammaln(y + 1.)) * J
#
#
# # fit with curve_fit
# parameters, cov_matrix = curve_fit(fit_function, bin_middles, entries)
#
# # plot poisson-deviation with fitted parameter
# x_plot = np.arange(0, 350)
#
# plt.plot(
#     x_plot,
#     fit_function(x_plot, *parameters),
#     marker='o', linestyle='',
#     label='Fit result',
# )
# plt.legend()
# plt.show()
