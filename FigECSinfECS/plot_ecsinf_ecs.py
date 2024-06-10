#Original file :/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/ECSinf_to_ECS/plot_ecs_v2.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scen = 'OutputAnalyse19NewPrior_W_cpi_2'

plt.rcParams['font.size'] = 12

scen_list_out = {'Base':'Base',
                 'Space1':'Temperature definition:',
                 'TEMP_4perc':'4% increase',
                 'TEMP_10perc':'10% increase',
                 'Space2':'Pattern effect:',
                 'alpha_0.1':'$\\alpha\' = $  0.1',  
                 'alpha_0.3':'$\\alpha\' = $  0.3',    
                 'alpha_0.5':'$\\alpha\' = $  0.5',
                 'alpha_1.0':'$\\alpha\' = $  1.0',
                 'Space3':''}

fig, axs = plt.subplot_mosaic(
    [["a","c"],
     ["b","c"]],
    figsize=(12,9)
)

color_dict_pattern = {0.1:'pink',
                      0.3: 'orange',
                      0.5:'red',
                      1.0: 'darkred'}

path_org = '/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/ECSinf_to_ECS/'


summary_all = pd.DataFrame(data=[])


#Use conversion factor from climate sensitivity parameter to ECSinf consistent with
#posteriori estimate of historical CO2 ERF:

filename = '/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/ECS_useCO2ERF/results_csv/'+scen+'_gaussiankde_ecsinf.csv'
gaussian_df = pd.read_csv(filename,index_col=0)

filename_summary = '/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/ECS_useCO2ERF/results_csv/summary_ecs_'+scen+'.csv'
summary_df =  pd.read_csv(filename_summary,index_col=0)
summary_df.index = ['Base'] 
summary_all = summary_all.append(summary_df)



axs["a"].plot(gaussian_df,linewidth=2,
              color='k',label='Base')
axs["b"].plot(gaussian_df,linewidth=2,
              color='k',label='Base')

#Add 4% increase in temperature
axs["a"].plot(gaussian_df.index*1.04,gaussian_df.values,
              linewidth=1,
              color='darkgray',label='4% increase')
#Add 10% increase in temperature
axs["a"].plot(gaussian_df.index*1.1,gaussian_df.values,
              linewidth=1,
              color='gray',label='10% increase')

#Add 4% increase in temperature in the summary file
summary_df =  pd.read_csv(filename_summary,index_col=0)
summary_df_new = summary_df.multiply(1.04)
summary_df_new.index = ['TEMP_4perc']
summary_all = summary_all.append(summary_df_new)

#Add 10% increase in temperature in the summary file
summary_df_new = summary_df.multiply(1.1)
summary_df_new.index = ['TEMP_10perc']
summary_all = summary_all.append(summary_df_new)


#Loop through pattern scale factors        
alpha_list = [0.1,0.3,0.5,1.0]
for alpha in alpha_list:
    filename = 'results_csv/'+scen+'_gaussiankde_ecsinf'+'_alpha_'+str(alpha)+'.csv'
    gaussian_df = pd.read_csv(filename,index_col=0)
    filename_summary = path_org + 'results_csv/summary_ecs_'+scen+'_alpha_'+str(alpha)+'.csv'
    summary_df =  pd.read_csv(filename_summary,index_col=0)
    summary_df.index = ['alpha_'+str(alpha)]
    summary_all = summary_all.append(summary_df)
    if alpha != 1.0:
        axs["b"].plot(gaussian_df,linewidth=1,color=color_dict_pattern[alpha],label='$\\alpha\' = $ '+str(alpha))
print(summary_all)



color_dict = {'Base':'black',
              'CO2ERF_3.93':'black',
              'CO2ERF_4.4': 'brown',
              'CO2ERF_3.46':'brown',
              'CO2ERF_3.71' :'darkgreen',
              'CO2ERF_4.15':'darkblue',
              'alpha_0.1':'pink',
              'alpha_0.3':'orange',
              'alpha_0.5':'red',
              'alpha_1.0':'darkred',
              'TEMP_4perc':'darkgray',
              'TEMP_10perc':'gray',}


#Plot the summary:
antscen = len(scen_list_out)
for sc,scen in enumerate(scen_list_out):
    print(scen)
    if scen[0:5]=='Space':
        axs["c"].text(-2.4,antscen-sc,scen_list_out[scen],color='black',weight='bold')
        continue
    print(scen)

    if scen_list_out[scen] == 'Base':
        axs["c"].axvline(summary_all.loc[scen]['Mean'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
        axs["c"].axvline(summary_all.loc[scen]['5perc'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
        axs["c"].axvline(summary_all.loc[scen]['95perc'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)

    axs["c"].plot(summary_all['Mean'].loc[scen],antscen-sc,'o',color=color_dict[scen])
    axs["c"].plot(summary_all['Median'].loc[scen],antscen-sc,'x',color=color_dict[scen])
    
    axs["c"].plot([summary_all['5perc'].loc[scen],summary_all['95perc'].loc[scen]],
                 [antscen-sc, antscen-sc],'-',linewidth=3,color=color_dict[scen])
    textline = scen_list_out[scen]
    axs["c"].text(-2.4,antscen-sc,textline,color='black')#colorlist[sc])

ipcc_central = 3.0
ipcc_likely = [2.5,4.0]
ipcc_very_likely = [2.0,5.0]

axs["c"].plot(ipcc_central, -0.01,'o',color='purple',label='IPCC central')
axs["c"].plot(ipcc_likely,[-0.01,-0.01], color='purple',linewidth=3,label='IPCC likely')
axs["c"].plot(ipcc_very_likely,[-0.01,-0.01], linestyle='--',linewidth=3,color='purple',label='IPCC very likely')
textline = "IPCC AR6"
axs["c"].text(-2.4,-0.01,textline,color='black')

axs["a"].legend()
axs["b"].legend()

axs["a"].set_xlim([0,5.5])
axs["b"].set_xlim([0,5.5])
axs["c"].set_xlim([-2.5,6.5])

axs["c"].set_yticks([])
axs["c"].set_xticks([1,2,3,4,5,6])


axs["a"].set_title('a) Definition of temperature GMST vs. GSAT',loc='left')
axs["b"].set_title('b) Pattern effect',loc='left')
axs["c"].set_title('c) Summary ECS',loc='left')

axs["b"].set_xlabel('ECS$_{inf}$/ECS [K]') # [$^\circ$C]')
axs["c"].set_xlabel('ECS$_{inf}$/ECS [K]') #'Equilibrium Climate Sensitivity [$^\circ$C]')



print(summary_all)



plt.tight_layout()
plt.savefig('ecs_inf_to_ecs.png')

plt.show()
