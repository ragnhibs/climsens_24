import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from dict_for_simulations import dict_for_simulations

plt.rcParams['font.size'] = 6
plt.rcParams['figure.dpi'] = 300

def plot_heatmap():

    
    #Read data climate sensitivity:
    path_ecs = '/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/ECS_useCO2ERF/results_csv/'
    filename = 'post_ecs_inf_'+scen+'.csv'
    post_ecs = pd.read_csv(path_ecs+filename,index_col=0)
    post_ecs = post_ecs['0']
    print(post_ecs)

    #Read data on ERF in end year.
    path_erf = '/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/ERFtrend/results_csv/'
    filename = 'rf_posterior_timeseriesaero'+scen+'.csv'
    post_erf = pd.read_csv(path_erf+filename,index_col=0)
    post_erf = post_erf.loc[year_end]
    print(post_erf)
    
    
    
    #######################################################
    samples = len(post_ecs.index)
    print(samples)
    bin = (int(samples*0.001))
    print(bin)

        
    N_bins = bin #(int(samples*0.001))
    
    yval = post_erf.values #post_rf_glob.values.T
    xval = post_ecs.values #.T
    

    # Construct 2D histogram from data using the 'plasma' colormap
    h=ax.hist2d(xval, yval, bins=N_bins, cmap='plasma',cmin=1,vmax=400)

    # Plot a colorbar with label.
    cb = plt.colorbar(h[3],ax=ax)
    cb.set_label('Number of entries')

    # Add title and labels to plot.
    ax.set_title(letter + scen_list_out[scen],loc='left')
    ax.set_xlabel('Inferred Effective Climate Sensitivity [K]')
    ax.set_ylabel('Aerosol ERF [W m$^{-1}$] in '+ str(year_end))


    ##############Original prior file
    path = '/div/qbo/utrics/RadiativeForcing/AR6_extended_2022/'
    filename = 'ERF_p05_aggregates_1750-2022.csv'
    rf_ar6_perc05 = pd.read_csv(path+filename,index_col=0)
    
    filename = 'ERF_p95_aggregates_1750-2022.csv'
    rf_ar6_perc95 = pd.read_csv(path+filename,index_col=0)
    
    
    ax.axhline(rf_ar6_perc05['aerosol'].loc[year_end+0.5],linestyle='--',color='gray')
    ax.axhline(rf_ar6_perc95['aerosol'].loc[year_end+0.5],linestyle='--',color='gray')
    
    ax.set_xlim([0,7])
    ax.set_ylim([-2.5,1])



print('Start')
#fig, axs = plt.subplots(nrows=2,ncols=4,sharex=True,figsize=(20,8))
scen_list_out,scen_colorlist =  dict_for_simulations()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9/1.5,4/1.75)) 

year_end = 2022
letter = 'a) '
ax=axs[0]
scen = 'OutputAnalyse30'
plot_heatmap()

letter = 'b) '
ax=axs[1]
scen = 'OutputAnalyse34'
plot_heatmap()

plt.tight_layout()
plt.savefig('Figures/erf_ecs_distr.png')


#plt.show()
exit()

#filepath = '/div/qbo/utrics/ClimateSensitivity/updateAR6/'
#scen = 'OutputAnalyse02'
#year_end = 2014

#filepath = '/div/qbo/utrics/ClimateSensitivity/updateAR6/TwoIndepCompAerosolCloudInt/'
#
filepath = '/div/qbo/utrics/ClimateSensitivity/updateAR6/PostSensitivitetstester4/'
scen = 'OutputAnalyse19NewPrior_W_cpi_2'
year_end = 2019


ax = axs[0,0]
print(ax)

plot_heatmap()

# Show the plot.
plt.show()
