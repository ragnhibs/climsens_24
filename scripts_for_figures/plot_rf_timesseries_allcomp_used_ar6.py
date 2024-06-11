import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams['font.size'] = 10


scen_list = ['OutputAnalyse19NewPrior_W_cpi_2']
scen_list_prior = {'OutputAnalyse19NewPrior_W_cpi_2':'OutputAnalyse04'}

scen_list_out = {'OutputAnalyse19NewPrior_W_cpi_2':'Base'}
                 
colorlist = ['C0','C1','C2','C3']

rf_list = ['AEROSOLCI','AEROSOLRI','CO2','N2O','CH4','OtherWMGHG',
           'O3','LANDUSE','CONTRAILS','STRATH2O',
           'SNOWALBEDO','SUN','VOLC_annual','aero','antro']
           

rf_list_long = {'Tot':'Total ERF',
                'antro':'Anthropogenic ERF',
                'aero':'Total aerosol ERF',
                'LLGHG':'Long lived GHGs ERF',
                'CO2':'CO2',
                'N2O':'N2O',
                'CH4':'CH4',
                'OtherWMGHG':'OtherWMGHG',
                'O3': 'Ozone ERF',
                'LANDUSE':'Landuse ERF',
                'CONTRAILS':'Contrail ERF',           
                'STRATH2O': 'Stratospheric H$_2$O ERF',           
                'SNOWALBEDO': 'Snow albedo ERF',
                'SUN': 'Solar ERF',
                'VOLC_annual':'Volcanic ERF',
                'AEROSOLRI':'Aerosol ERFari',
                'AEROSOLCI':'Aerosol ERFaci'}


fig, axs = plt.subplots(nrows=4,ncols=4,sharex=False,figsize=(14,12))
axs=axs.flatten()
for sc,scen in enumerate(scen_list):
    for rf,rf_comp in enumerate(rf_list):
        filename = 'summary_rf_posterior_timeseries_'+rf_comp+scen+'.csv'
        filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen_list_prior[scen]+'.csv'
        post_rf=pd.read_csv('results_csv/'+filename,
                            index_col=0)
        prior_rf=pd.read_csv('results_csv/'+filename_prior,
                            index_col=0)
        axs[rf].plot(post_rf['Median'],color=colorlist[sc],label=scen)
        axs[rf].fill_between(post_rf.index, post_rf['5perc'],
                             post_rf['95perc'],
                             color=colorlist[sc],
                             alpha=0.3)
        axs[rf].plot(prior_rf['Median'],'--',color=colorlist[sc])
        axs[rf].plot(prior_rf['95perc'],':',color=colorlist[sc])
        axs[rf].plot(prior_rf['5perc'],':',color=colorlist[sc])
        axs[rf].set_title(rf_list_long[rf_comp])
        axs[rf].set_ylabel('ERF [W m$^{-2}$]')
        
#Defining some legend looks:
#prior_legend_ar5 = mpatches.Patch(facecolor=colorlist[0],alpha=0.3,label='AR5 prior')
post_legend_ar6 = mpatches.Patch(facecolor=colorlist[0],alpha=0.3,label= scen_list_out[scen_list[0]] + ' posterior')
line1, = axs[rf+1].plot(2000,np.nan, '--',color='black',label='Prior Median')
line2, = axs[rf+1].plot(2000,np.nan,'-', color='black',label='Posterior Median')
line3, = axs[rf+1].plot(2000,np.nan,':', color='black',label='Prior 5 and 95 percentiles')

axs[rf+1].axis('off')
axs[rf+1].legend(loc='center',
                 handles = [ post_legend_ar6,line2,line1,line3],
                 frameon=False,
                 fontsize=14)



plt.tight_layout()
plt.savefig('Figures/posterior_rf_allcomp.png')

plt.show()
