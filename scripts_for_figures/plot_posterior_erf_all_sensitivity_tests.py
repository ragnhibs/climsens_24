import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#from dict_for_simulations_old import dict_for_simulations
from dict_for_simulations_all import dict_for_simulations_all

plt.rcParams['font.size'] = 14

def plot_results():
    for sc,scen in enumerate(scen_list):
        filename_posterior = 'summary_rf_posterior_timeseries_'+rf_comp+scen+'.csv'
        posterior_rf=pd.read_csv('results_csv/'+filename_posterior,
                             index_col=0)

        if sc == 0: 
            ax.plot(posterior_rf['Median'],'-',
                    color=colorlist[sc],zorder=10,label=scen_list_out[scen])
        else:
            ax.plot(posterior_rf['Median'],'-',
                    color=colorlist[sc],label=scen_list_out[scen])
        ax.plot(posterior_rf['95perc'],'--',linewidth=0.5,color=colorlist[sc])
        ax.plot(posterior_rf['5perc'],'--',linewidth=0.5,color=colorlist[sc])
    ax.axhline(0.0,linestyle='-',linewidth=0.5,color='lightgray')
    ax.set_xlim([1850,2020])
    ax.set_ylim(ylim)
    ax.set_ylabel('ERF [W m$^{-2}$]')
    

scen_list_out,scen_colorlist =  dict_for_simulations_all()

#Choose component to plot
rf_comp = 'antro' #aero' #antro' 

ylim_dict = {'aero':[-3,0.1],
             'antro':[-0.6,4.0]}
ylim = ylim_dict[rf_comp]


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
                'VOLC_annual':'Volcanic ERF',
                'AEROSOLRI':'Aerosol ERFari',
                'AEROSOLCI':'Aerosol ERFaci',}

fig, axs = plt.subplots(nrows=1,ncols=4,sharex=True,figsize=(20,8))


scen_list = ['OutputAnalyse19NewPrior_W_cpi_2',
             'OutputNewAnalyse05Smooth']
colorlist = ['black','C2','C4']
ax = axs[0]
plot_results()
ax.set_title('a)',loc='left')
scen='OutputAnalyse04'
filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen+'.csv'
prior_rf=pd.read_csv('results_csv/'+filename_prior,
                         index_col=0)
ax.fill_between(prior_rf.index, prior_rf['5perc'],
                prior_rf['95perc'],
                color='black',
                alpha=0.1,label='Prior (Base)')
ax.legend(frameon=False)


scen_list = ['OutputAnalyse19NewPrior_W_cpi_2',
             'OutputNewAnalyse06Linear1750to1900',
             'OutputNewAnalyse07Weaker1900to1950',
             'OutputNewAnalyse08Stronger1900to1950',
             'OutputNewAnalyse09Weaker1950to1980',
             'OutputNewAnalyse10Stronger1950to1980',
             'OutputNewAnalyse12StrongerWeaker1980to2019',
             'OutputNewAnalyse13Stronger1980to2019',
             'OutputNewAnalyse15LinWeaker2014to2019']
colorlist = ['black','C1','C2','C3','C4','C5','C6','C7','C8']


ax = axs[1]
plot_results()
ax.set_title('b)',loc='left')
scen='OutputAnalyse04'
filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen+'.csv'
prior_rf=pd.read_csv('results_csv/'+filename_prior,
                         index_col=0)
ax.fill_between(prior_rf.index, prior_rf['5perc'],
                prior_rf['95perc'],
                color='black',
                alpha=0.1,label='Prior (Base)')
ax.legend(frameon=False)


scen_list = ['OutputNewAnalyse05Smooth',
             'OutputAnalyse24LinredSmoothbase1950to1990',
             'OutputAnalyse25LinredSmoothbase1950to2000',
             'OutputAnalyse26LinredSmoothbase1950to2010',
             'OutputAnalyse27LinredSmoothbase1950to2019']

colorlist = ['black','C1','C2','C3','C4','C5','C6','C7','C8']
ax = axs[2]
plot_results()
ax.set_title('c)',loc='left')
scen='OutputNewAnalyse05Smooth' #'OutputAnalyse04'
filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen+'.csv'
prior_rf=pd.read_csv('results_csv/'+filename_prior,
                         index_col=0)
ax.fill_between(prior_rf.index, prior_rf['5perc'],
                prior_rf['95perc'],
                color='black',
                alpha=0.1,label='Prior (Smooth)')
ax.legend(frameon=False)



scen_list = ['OutputNewAnalyse05Smooth',
             'OutputAnalyse31LinredSmoothbase1950to1980Flat',
             'OutputAnalyse32LinredSmoothbase1950to1990Flat',
             'OutputAnalyse33LinredSmoothbase1950to2000Flat']

             

colorlist = ['black','C1','C2','C3','C4','C5','C6','C7','C8']
ax = axs[3]
plot_results()
ax.set_title('d)',loc='left')
scen='OutputNewAnalyse05Smooth' #'OutputAnalyse04'
filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen+'.csv'
prior_rf=pd.read_csv('results_csv/'+filename_prior,
                         index_col=0)
ax.fill_between(prior_rf.index, prior_rf['5perc'],
                prior_rf['95perc'],
                color='black',
                alpha=0.1,label='Prior (Smooth)')
ax.legend(frameon=False)


plt.suptitle('Posterior: '+rf_list_long[rf_comp])
plt.tight_layout()


plt.savefig('Figures/posterior_rf_sensitivitytests_'+rf_comp+'.png')
plt.show()
