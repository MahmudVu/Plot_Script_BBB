'''
->>>>>  Read from output files and log the time to failure to variable time
->>>>>  The data is manually read for each file without automation since the format varies
->>>>>  Covert register alues to binary format
'''
#%%
import numpy as np
import matplotlib.pylab as plt

plt.style.use('classic')

#%%
print 'test without radiation'
exp_data=np.genfromtxt('results_b4.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,1]
dfsr=exp_data[0:,2]
ifsr=exp_data[0:,3]
actlr=exp_data[0:,4]
cpacr=exp_data[0:,5]
pmcr=exp_data[0:,6]
cache_aux=exp_data[0:,7]
cntrl=exp_data[0:,8]
time=(float(exp_data[0:,9][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data0.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()

#%%
print 'test with alpha source'
exp_data=np.genfromtxt('copy.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data1.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()

#%%
print 'test with alpha source'
exp_data=np.genfromtxt('results_10_28_10_30.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,1]
dfsr=exp_data[0:,2]
ifsr=exp_data[0:,3]
actlr=exp_data[0:,4]
cpacr=exp_data[0:,5]
pmcr=exp_data[0:,6]
cache_aux=exp_data[0:,7]
cntrl=exp_data[0:,8]
time=(float(exp_data[0:,9][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data2.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('results_10_28_10_40.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,1]
dfsr=exp_data[0:,2]
ifsr=exp_data[0:,3]
actlr=exp_data[0:,4]
cpacr=exp_data[0:,5]
pmcr=exp_data[0:,6]
cache_aux=exp_data[0:,7]
cntrl=exp_data[0:,8]
time=(float(exp_data[0:,9][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data3.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('results_2.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,1]
dfsr=exp_data[0:,2]
ifsr=exp_data[0:,3]
actlr=exp_data[0:,4]
cpacr=exp_data[0:,5]
pmcr=exp_data[0:,6]
cache_aux=exp_data[0:,7]
cntrl=exp_data[0:,8]
time=(float(exp_data[0:,9][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data4.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('results_3.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data5.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('result_4_part1.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,1]
dfsr=exp_data[0:,2]
ifsr=exp_data[0:,3]
actlr=exp_data[0:,4]
cpacr=exp_data[0:,5]
pmcr=exp_data[0:,6]
cache_aux=exp_data[0:,7]
cntrl=exp_data[0:,8]
time=(float(exp_data[0:,9][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data6.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('result_4_part3.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,1]
dfsr=exp_data[0:,2]
ifsr=exp_data[0:,3]
actlr=exp_data[0:,4]
cpacr=exp_data[0:,5]
pmcr=exp_data[0:,6]
cache_aux=exp_data[0:,7]
cntrl=exp_data[0:,8]
time=(float(exp_data[0:,9][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data7.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('updated.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data8.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('updated_2.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data9.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('updated_4.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data10.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('updated_5.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data11.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('updated_no_ecc.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data12.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
print 'test with alpha source'
exp_data=np.genfromtxt('updated_no_ecc_2.txt', delimiter='\t', dtype=np.int64, skip_header=1, skip_footer=5)
sum_fib=exp_data[0:,0]
dfsr=exp_data[0:,1]
ifsr=exp_data[0:,2]
actlr=exp_data[0:,3]
cpacr=exp_data[0:,4]
pmcr=exp_data[0:,5]
cache_aux=exp_data[0:,6]
cntrl=exp_data[0:,7]
time=(float(exp_data[0:,8][-1])/60)

print 'sum_fib:\t',(np.unique(sum_fib))
print 'dfsr:\t',(np.unique(dfsr))
print 'ifsr:\t',(np.unique(ifsr))
print 'actlr:\t',(np.unique(actlr))
print 'cpacr:\t',(np.unique(cpacr))
print 'pmcr:\t',(np.unique(pmcr))
print 'cache_aux:\t',(np.unique(cache_aux))
print 'cntrl:\t',(np.unique(cntrl))
print 'max time:\t',(time)

print 'sum_fib:\t',np.binary_repr((np.unique(sum_fib)[-1]))
print 'dfsr:\t',np.binary_repr((np.unique(dfsr)[-1]))
print 'ifsr:\t',np.binary_repr((np.unique(ifsr)[-1]))
print 'actlr:\t',np.binary_repr((np.unique(actlr))[-1])
print 'cpacr:\t',np.binary_repr((np.unique(cpacr))[-1])
print 'pmcr:\t',np.binary_repr((np.unique(pmcr))[-1])
print 'cache_aux:\t',np.binary_repr((np.unique(cache_aux))[-1])
print 'cntrl:\t',np.binary_repr((np.unique(cntrl))[-1])
print 'max time:\t',(time)


file2write=open("data13.txt",'w+')
file2write.write('sum_fib\t'+ np.binary_repr((np.unique(sum_fib)[-1]))+'\n')
file2write.write('dfsr\t'+np.binary_repr((np.unique(dfsr)[-1]))+'\n')
file2write.write('ifsr\t'+np.binary_repr((np.unique(ifsr)[-1]))+'\n')
file2write.write('actlr\t'+np.binary_repr((np.unique(actlr)[-1]))+'\n')
file2write.write('cpacr\t'+np.binary_repr((np.unique(cpacr)[-1]))+'\n')
file2write.write('pmcr\t'+np.binary_repr((np.unique(pmcr)[-1]))+'\n')
file2write.write('cache_aux\t'+np.binary_repr((np.unique(cache_aux)[-1]))+'\n')
file2write.write('cntrl\t'+np.binary_repr((np.unique(cntrl)[-1]))+'\n')
file2write.write('max time\t'+str(time)+'\n')

file2write.close()
#%%%
plt.show()
    
    
    
    
