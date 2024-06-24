#Original path: /div/qbo/utrics/ClimateSensitivity/updateAR6/script
#First run read_ecs_inf.py for all simulations. For the first three here, the others here:/scripts_other/ECS_useCO2ERF/

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from dict_for_simulations import dict_for_simulations

plt.rcParams['font.size'] = 5
plt.rcParams['figure.dpi'] = 300


scen_list_out,scen_colorlist =  dict_for_simulations()
antscen = len(scen_list_out)


fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(5,3))

for sc,scen in enumerate(scen_list_out):
    print(scen)
    if scen[0:5]=='Space':
        axs.text(4,antscen-sc,scen_list_out[scen],color='black',weight='bold')
        continue

    if scen == 'OutputAnalyse01':
        print(1)
        summary_ecs = pd.read_csv('results_csv/summary_ecs_'
                                  + scen + '.csv',
                                  index_col=0)
    elif scen == 'OutputAnalyse02':
        print(1)
        summary_ecs = pd.read_csv('results_csv/summary_ecs_'
                                  + scen + '.csv',
                                  index_col=0)
    else:
        print(2)
        summary_ecs = pd.read_csv('results_csv_use_postCO2/summary_ecs_'
                                  + scen + '.csv',
                                  index_col=0)
    
    #For label in legend and initialize summary table:
    if scen == 'OutputAnalyse01':
        axs.plot(summary_ecs['Mean'],antscen-sc,'o',markersize=3,
                 color=scen_colorlist[scen],label='Mean')
        axs.plot([summary_ecs['5perc'],summary_ecs['95perc']],
                 [antscen-sc, antscen-sc],'-',linewidth=1,color=scen_colorlist[scen],
                 label='90% C.I.')
        summary_all = summary_ecs
    else:
        axs.plot(summary_ecs['Mean'],antscen-sc,'o',markersize=3,color=scen_colorlist[scen])
        axs.plot([summary_ecs['5perc'],summary_ecs['95perc']],
                 [antscen-sc, antscen-sc],'-',linewidth=1,color=scen_colorlist[scen])
        summary_all=pd.concat([summary_all,summary_ecs])

    textline = scen_list_out[scen]
    axs.text(4,antscen-sc,textline,color='black')

    #Vertical lines indication baseline results
    if scen_list_out[scen]=='Smooth':
        axs.axvline(summary_ecs.loc[scen]['Mean'],linestyle='--',
                    color='darkgray',linewidth=0.5,zorder=0)
        axs.axvline(summary_ecs.loc[scen]['5perc'],linestyle='--',
                    color='darkgray',linewidth=0.5,zorder=0)
        axs.axvline(summary_ecs.loc[scen]['95perc'],linestyle='--',
                    color='darkgray',linewidth=0.5,zorder=0)

pd.options.display.float_format = '{:,.2f}'.format    
summary_all = summary_all.rename(index=scen_list_out)
print(summary_all)


print('Tekst to manuscript')
print('mean Base ' + '{:.1f}'.format(summary_all['Mean'].loc['Base (end year 2019)']))
print('90th range Base: '+ '{:.1f}'.format(summary_all['5perc'].loc['Base (end year 2019)']) +' to ' + '{:.1f}'.format(summary_all['95perc'].loc['Base (end year 2019)']))

temp = summary_all['Mean'].loc['Base (end year 2019)'] - summary_all['Mean'].loc['Skeie18 (end year 2014)']
print('diff Base and Skeie et al 2018: '  + '{:.1f}'.format(temp))

"""
print('Tekst to manuscript')
print('Difference 95th percentile in the two test adjusting the ERF 1950-1980')
value = summary_all['95perc'].loc['Weaker1950to1980'] - summary_all['95perc'].loc['Stronger1950to1980']
print(value)

print('Tekst to manuscript')
print('Difference 95th percentile in the two test adjusting the ERF 1980-2019')
value = summary_all['95perc'].loc['Stronger1980to2019'] - summary_all['95perc'].loc['StrongerWeaker1980to2019']
print(value)
"""   

print('Tekst to manuscript')
print('mean Base extended ' + '{:.1f}'.format(summary_all['Mean'].loc['Base extended (end year 2022)']))
print('90th range Base extended: '+ '{:.1f}'.format(summary_all['5perc'].loc['Base extended (end year 2022)']) +' to ' + '{:.1f}'.format(summary_all['95perc'].loc['Base extended (end year 2022)']))


print('Tekst to manuscript')
name = 'Unc. in 1950 and 2014 independent'
print('mean ACI test ' + '{:.1f}'.format(summary_all['Mean'].loc[name]))
print('90th range ACI test: '+ '{:.1f}'.format(summary_all['5perc'].loc[name]) +' to ' + '{:.1f}'.format(summary_all['95perc'].loc[name]))

number = summary_all['Mean'].loc[name] - summary_all['Mean'].loc['Base extended (end year 2022)']
print('the mean ECSinf increased by {:.1f}'.format(number))


#the_table = axs.table(cellText =np.half(summary_all.values),
#                      rowLabels =summary_all.index,
#                      colLabels=summary_all.columns,
#                      bbox = [0.6, 0.1, 0.35, 0.4],
#                      colWidths=[0.1,0.1,0.1,0.1,0.1])

#the_table.set_fontsize(7)


axs.set_yticks([])
axs.set_xlim(0,7)
axs.set_ylim(0,antscen+1)

axs.set_xlabel('Inferred Effective Climate Sensitivity (ECS$_{inf}$) [K]') 
plt.legend( loc='upper right',frameon=False)
plt.savefig('Figures/ECSinf_alt4.png')
plt.show()
