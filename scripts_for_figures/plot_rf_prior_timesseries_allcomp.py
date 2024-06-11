import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


plt.rcParams['font.size'] = 12

#Only present results from 2000 and onwards.
short = False


scen_list = ['OutputAnalyse30',
             'OutputAnalyse04',
             'OutputAnalyse02']
             

colorlist = ['C2','C1','C0']

rf_list = ['Tot',
           'antro',
           'aero',
           'LLGHG',
           'O3',
           'LANDUSE',
           'CONTRAILS',           
           'STRATH2O',           
           'SNOWALBEDO',
           'SUN',
           'VOLC_annual']

rf_list_long = {'Tot':'Total ERF',
                'antro':'Anthropogenic ERF',
                'aero':'Total aerosol ERF',
                'LLGHG':'Long lived GHGs ERF',
                'O3': 'Ozone ERF',
                'LANDUSE':'Landuse ERF',
                'CONTRAILS':'Contrail ERF',           
                'STRATH2O': 'Stratospheric H$_2$O ERF',           
                'SNOWALBEDO': 'Snow albedo ERF',
                'SUN': 'Solar ERF',
                'VOLC_annual':'Volcanic ERF'}

fig, axs = plt.subplots(nrows=4,ncols=3,sharex=False,figsize=(14,12))
axs=axs.flatten()
for sc,scen in enumerate(scen_list):
    for rf,rf_comp in enumerate(rf_list):
        filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen+'.csv'
        prior_rf=pd.read_csv('results_csv/'+filename_prior,
                            index_col=0)
        
        if short:
            prior_rf = prior_rf.loc[2000:]
            
        axs[rf].fill_between(prior_rf.index, prior_rf['5perc'],
                             prior_rf['95perc'],
                             color=colorlist[sc],
                             alpha=0.3)
        axs[rf].plot(prior_rf['Median'],'-',color=colorlist[sc])
        axs[rf].plot(prior_rf['95perc'],'--',color=colorlist[sc])
        axs[rf].plot(prior_rf['5perc'],'--',color=colorlist[sc])
        axs[rf].set_title(rf_list_long[rf_comp])
        axs[rf].set_ylabel('ERF [W m$^{-2}$]')
            
        

#Defining some legend looks:
prior_legend_ar5 = mpatches.Patch(facecolor=colorlist[2],
                                  alpha=0.3,label='AR5 prior')
prior_legend_ar6 = mpatches.Patch(facecolor=colorlist[1],
                                  alpha=0.3,label='AR6 prior')
prior_legend_ar6_ext = mpatches.Patch(facecolor=colorlist[0],
                                      alpha=0.3,label='AR6 ext. prior')
line1, = axs[rf+1].plot(2000,np.nan, color='black',label='Median')
line2, = axs[rf+1].plot(2000,np.nan,'--', color='black',
                        label='5 and 95 percentiles')

        
axs[rf+1].axis('off')
axs[rf+1].legend(loc='center',
                 handles = [prior_legend_ar5, prior_legend_ar6,
                            prior_legend_ar6_ext,line1,line2],
                 frameon=False,
                 fontsize=14)  


plt.tight_layout()

if short:
    plt.savefig('Figures/prior_rf_allcomp_short.png')
else:
    plt.savefig('Figures/prior_rf_allcomp.png')

plt.show()
