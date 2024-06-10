import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde



#Sett pattern effect
#See IPCC 7.5.2.1
alpha_list = [0.1,0.3,0.5,1.0]

alpha=1.0


plt.rcParams['font.size'] = 12


filepath = '/div/qbo/utrics/ClimateSensitivity/updateAR6/PostSensitivitetstester4/'

scen ='OutputAnalyse19NewPrior_W_cpi_2'


#Set 2xCO2 ERF
post_co2=pd.read_csv('results_co2_erf/co2_erf_2019_'+scen+'.csv',index_col=0)
#Corresponding 2xCO2 values:
post_2xco2 = post_co2['2019']*3.93/2.1562



filename = 'post_parval.txt'

paralist_short= ['akapa', 'cpi' , 'w', 'rlamdo', 'beto', 'mixed', 'LAMBDA']
paralist = ['Vertical heat diffusivity','Polar parameter','Upwelling velocity',
            'Air-sea heat exchange parameter',
            'Oceanic interhemispheric heat exchange parameter',
            'Mixed layer depth', 'Climate sensitivity']
post_parval= pd.read_csv(filepath+scen+'/'+filename,sep=' ',header=None)
post_parval.columns = paralist 


post_ecs= pd.read_csv(filepath+scen+'/'+filename,sep=' ',header=None)

sens_para =  post_parval['Climate sensitivity']
sens_para_with_pattern = sens_para/(1-sens_para*alpha)
post_ecs = sens_para_with_pattern*post_2xco2


#######################################################
samples = len(post_ecs.index)
bin = (int(samples*0.001))

fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(10,8))

axs.hist(post_ecs,bins=bin,density=True,color='darkgray',label='posteriori ' + scen)
frek, bins = np.histogram(post_ecs,bins=bin,density=True)
axs.plot(bins[0:-1] +((bins[1]-bins[0])/2), frek,color='black')
axs.legend()
axs.set_xlabel('K')
axs.set_title('Equilibrium Climate Sensisitvity')

kde = gaussian_kde(post_ecs)
dist_space = np.linspace(min(post_ecs), min(max(post_ecs),20), 100 )
print(dist_space)


axs.plot(dist_space,kde(dist_space),linewidth=0.5,color='blue',label='gausian_kde')

print(kde(dist_space))
print(dist_space)

#Write to file:
gaussian_df = pd.DataFrame(data=kde(dist_space),index=dist_space,columns=[scen])
print(gaussian_df)
gaussian_df.to_csv('results_csv/'+scen+'_gaussiankde_ecsinf'+'_alpha_'+str(alpha)+'.csv')


ipcc_central = 3.0
ipcc_likely = [2.5,4.0]
ipcc_very_likely = [2.0,5.0]
axs.plot(ipcc_central, 0.1,'o',color='purple',label='IPCC central')
axs.plot(ipcc_likely,[0.1,0.1], color='purple',label='IPCC likely')
axs.plot(ipcc_very_likely,[0.1,0.1], linestyle='--',color='purple',label='IPCC very likely')
    

left, right = axs.get_xlim()
bottom, top= axs.get_ylim()

ecs_mean = np.mean(post_ecs)

axs.text(3.5,0.5*top,'ECS$_{inf}$: '+
         '\nMean:    '+f"{ecs_mean:.3g}" + 
         '\nMedian:  '+f"{np.percentile(post_ecs,50):.3g}"+
         '\n5perc:   '+f"{np.percentile(post_ecs,5):.3g}"+
         '\n95perc:  '+f"{np.percentile(post_ecs,95):.3g}")


#Write to file:
d = {'Mean': ecs_mean,
     'Median': np.percentile(post_ecs,50),
     '5perc':np.percentile(post_ecs,5),
     '95perc':np.percentile(post_ecs,95)}
summary_df = pd.DataFrame(data=d, index=[scen])
summary_df.to_csv('results_csv/summary_ecs_' + scen +'_alpha_'+str(alpha)+'.csv')


axs.legend()
plt.show()
