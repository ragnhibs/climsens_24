#First run read_ecs_inf.py for all simulations.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from dict_for_simulations_all import dict_for_simulations_all


plt.rcParams['font.size'] = 5
plt.rcParams['figure.dpi'] = 300

scen_list_out,scen_colorlist =  dict_for_simulations_all()
antscen = len(scen_list_out)


fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(5,3))


for sc,scen in enumerate(scen_list_out):
   
    if scen[0:5]=='Space':
        axs.text(2.5,antscen-sc,scen_list_out[scen],color='black',weight='bold')
        continue

    if scen == 'OutputAnalyse01':
        summary_tcr = pd.read_csv('results_csv/summary_tcr_'
                                  + scen + '.csv',
                                  index_col=0)
    elif scen == 'OutputAnalyse02':
        summary_tcr = pd.read_csv('results_csv/summary_tcr_'
                                  + scen + '.csv',
                                  index_col=0)
    
    else:
        print(scen)
        summary_tcr = pd.read_csv('results_csv/summary_tcr_ar6erf_'
                                  + scen + '.csv',
                                  index_col=0)

    #For label in legend and initialize summary table:    
    if scen == 'OutputAnalyse01':
        axs.plot(summary_tcr['Mean'],antscen-sc,'o',markersize=3,
                 color=scen_colorlist[scen],label='Mean')
        #axs.plot(summary_tcr['Median'],0.2+0.05*sc,'d',color=colorlist[sc])
        axs.plot([summary_tcr['5perc'],summary_tcr['95perc']],
                 [antscen-sc, antscen-sc],'-',linewidth=1,color=scen_colorlist[scen],
                 label='90% C.I.')
        summary_all = summary_tcr
    else:
        axs.plot(summary_tcr['Mean'],antscen-sc,'o',markersize=3,color=scen_colorlist[scen])
        #axs.plot(summary_tcr['Median'],antscen-sc,'d',color=colorlist[sc])
        axs.plot([summary_tcr['5perc'],summary_tcr['95perc']],
                 [antscen-sc, antscen-sc],'-',linewidth=1,color=scen_colorlist[scen])
    
        summary_all=pd.concat([summary_all,summary_tcr])
    textline = scen_list_out[scen]
    axs.text(2.5,antscen-sc,textline,color='black')#scen_colorlist[scen])

    if scen_list_out[scen]=='Smooth':
        
        axs.axvline(summary_tcr.loc[scen]['Mean'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
        axs.axvline(summary_tcr.loc[scen]['5perc'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
        axs.axvline(summary_tcr.loc[scen]['95perc'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
    
print(summary_all)
pd.options.display.float_format = '{:,.2f}'.format
summary_all = summary_all.rename(index=scen_list_out)
print(summary_all)


print('Tekst to manuscript')
print('mean Base ' + '{:.1f}'.format(summary_all['Mean'].loc['Base']))
print('90th range Base: '+ '{:.1f}'.format(summary_all['5perc'].loc['Base']) +' to ' + '{:.1f}'.format(summary_all['95perc'].loc['Base']))


print('Tekst to manuscript')
print('mean Base Ext ' + '{:.1f}'.format(summary_all['Mean'].loc['Base extended (end year 2022)']))
print('90th range Base Ext: '+ '{:.1f}'.format(summary_all['5perc'].loc['Base extended (end year 2022)']) +' to ' + '{:.1f}'.format(summary_all['95perc'].loc['Base extended (end year 2022)']))


#the_table = axs.table(cellText =np.half(summary_all.values),
#                      rowLabels =summary_all.index,
#                      colLabels=summary_all.columns,
#                      bbox = [0.6, 0.1, 0.35, 0.4],
#                      colWidths=[0.1,0.1,0.1,0.1,0.1])

#the_table.set_fontsize(7)

#print(colorlist)


ipcc_central = 1.8
ipcc_likely = [1.4,2.2]
ipcc_very_likely = [1.2,2.4]

axs.plot(ipcc_central, -1,'s',color='darkgray',linewidth=1,markersize=3,label='TCR IPCC central')
axs.plot(ipcc_likely,[-1,-1], color='darkgray',linewidth=1,label='TCR IPCC likely')
axs.plot(ipcc_very_likely,[-1,-1], linestyle='--',linewidth=1,
         color='darkgray',label='TCR IPCC very likely')

axs.text(2.5,-1.0,'IPCC AR6',color='darkgray')

axs.set_yticks([])
axs.set_xlim(0.5,4.5)
axs.set_xticks([0.5,1,1.5,2,2.5,3])
axs.set_ylim(-2,antscen+1)

axs.set_xlabel('Transient Climate Response (TCR) [K]') 
plt.legend(loc='upper right',frameon=False)
#plt.savefig('Figures/TCR_alt3.png')
plt.show()
