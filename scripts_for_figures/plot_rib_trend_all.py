import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from datetime import datetime, timedelta


plt.rcParams['font.size'] = 12

def plot_summary():
    for sc,scen in enumerate(scen_list_out):
        if scen[0:5]=='Space':
            ax.text(0.5,antscen-sc-0.15,scen_list_out[scen],
                    color='black',weight='bold')
            continue
        
        rib_trend = rib_trend_all.loc[scen]*10.0 # Per decade
        ax.plot(rib_trend['Mean'],antscen-sc,'o',markersize=10,
                 color=scen_list_colors[scen],label='Mean')
        ax.plot([rib_trend['5perc'],rib_trend['95perc']],
                [antscen-sc, antscen-sc],'-',linewidth=3,
                color=scen_list_colors[scen],
                label='90% C.I.')
        textline = scen_list_out[scen]
        ax.text(0.5,antscen-sc-0.15,textline,color='black')

        if scen_list_out[scen]=='Base':
            ax.axvline(rib_trend.loc['Mean'],linestyle='--',
                       color='darkgray',linewidth=0.5,zorder=0)
            ax.axvline(rib_trend.loc['5perc'],linestyle='--',
                       color='darkgray',linewidth=0.5,zorder=0)
            ax.axvline(rib_trend.loc['95perc'],linestyle='--',
                       color='darkgray',linewidth=0.5,zorder=0)
            
    ax.set_xlim([0,1.4])
    ax.set_yticks([])
    

#Results to be plotted in b)        
scen_list_out = {'OutputAnalyse19NewPrior_W_cpi_2':'Base',
                 'OutputAnalyse30':'Base extended (end year 2022)',
                 'Space0':'',
                 'Space1':'Sensitivity test:',
                 'OutputNewAnalyse05Smooth':'Smooth',
                 'Space2':'',
                 'OutputNewAnalyse12StrongerWeaker1980to2019':'StrongerWeaker1980to2019',
                 'OutputNewAnalyse13Stronger1980to2019':'Stronger1980to2019',
                 'OutputNewAnalyse15LinWeaker2014to2019':'LinWeaker2014to2019',
                 'Space3':'',
                 'OutputAnalyse24LinredSmoothbase1950to1990':'Linred1950to1990',
                 'OutputAnalyse25LinredSmoothbase1950to2000':'Linred1950to2000',
                 'OutputAnalyse26LinredSmoothbase1950to2010':'Linred1950to2010',
                 'OutputAnalyse27LinredSmoothbase1950to2019':'Linred1950to2019',
                 'Space4':'',
                 'OutputAnalyse33LinredSmoothbase1950to2000Flat':'Linred1950to2000 then flat',
                 'Space7':'',
                 'Space8':'ERFaci trend test',
                 'OutputAnalyse34':'Unc. in 1950 and 2014 independent',
                 'Space9':'',}


#Results to be plotted in c)
scen_list_out_c = {'OutputAnalyse19NewPrior_W_cpi_2':'Base',
                   'Space0':'',
                   'Space1':'Sensitivity test:',
                   'Space2':'',
                   'OutputNewAnalyse12StrongerWeaker1980to2019':'StrongerWeaker1980to2019',
                   'OutputNewAnalyse13Stronger1980to2019':'Stronger1980to2019',
                   'OutputNewAnalyse15LinWeaker2014to2019':'LinWeaker2014to2019',
                   'Space3':'',
                   'OutputAnalyse24LinredSmoothbase1950to1990':'Linred1950to1990',
                   'OutputAnalyse27LinredSmoothbase1950to2019':'Linred1950to2019',
                   'Space4':'',
                   'OutputAnalyse33LinredSmoothbase1950to2000Flat':'Linred1950to2000 then flat',
                   'Space5':'',
                   'Space6':'Extend to 2022:',
                   'OutputAnalyse30':'Base extended (end year 2022)',
                   'Space7':'',
                   'Space8':'ERFaci trend test',
                   'OutputAnalyse34':'Unc. in 1950 and 2014 independent'}



scen_list_colors = {'OutputAnalyse19NewPrior_W_cpi_2':'black',
                    'OutputNewAnalyse05Smooth':'C1',
                    'OutputNewAnalyse12StrongerWeaker1980to2019':'C2',
                    'OutputNewAnalyse13Stronger1980to2019':'C3',
                    'OutputNewAnalyse15LinWeaker2014to2019':'C4',
                    'OutputAnalyse24LinredSmoothbase1950to1990':'C5',
                    'OutputAnalyse25LinredSmoothbase1950to2000':'C6',
                    'OutputAnalyse26LinredSmoothbase1950to2010':'C7',
                    'OutputAnalyse27LinredSmoothbase1950to2019':'C8',
                    'OutputAnalyse31LinredSmoothbase1950to1980Flat':'C9',
                    'OutputAnalyse32LinredSmoothbase1950to1990Flat':'C9',
                    'OutputAnalyse33LinredSmoothbase1950to2000Flat':'C9',
                    'OutputAnalyse30':'darkgray',
                    'OutputAnalyse34':'C10'}



filename = 'results_csv_rib/rib_trend_all_2005_2019.csv'

rib_trend_all = pd.read_csv(filename,index_col=0)


fig, axes = plt.subplot_mosaic(
    [["top left",  "right"],
     ["bottom left", "right"]],
    figsize=(14,9)
)

ax = axes["right"]
antscen = len(scen_list_out)


#Plot panel b)
plot_summary()

#mid-2005 to mid-2019 estimates the trend
#for the net CERES TOA energy flux is
#0.50 +- 0.47 W m-2 decade-1 over that
#same time period (Figure 1, dashed lines)
#(Loeb et al., 2021)

ax.plot(0.5,-0.5,'s',color='k',markersize=10)
ax.plot([0.5-0.47,0.5+0.47],
        [-0.5, -0.5],'-',linewidth=3,color='k',
        label=' 90% C.I.')
textline = 'Loeb et al. (2021)' 
ax.text(0.5,-0.05,textline,color='k')




#Plot panel a)
ax = axes["top left"]

scen =  'OutputAnalyse30'
post_rib=pd.read_csv('results_csv_rib/summary_rib_timeseries_' + scen + '.csv',
                     index_col=0)

y = post_rib['Median'].loc[2005:2022]
x = y.index
b, a = np.polyfit(x.values, y.values, deg=1)
xseq = x.values
ax.plot(xseq, a + b * xseq, color="darkgray", lw=0.5,linestyle='-.');
ax.text(2022.5, a + b * 2022, '{:2.2f}'.format(b*10.0)+' Wm$^{-2}$ dec$^{-1}$', color="darkgray",fontsize=10)

ax.fill_between(post_rib.index, post_rib['5perc'],post_rib['95perc'],
                color='darkgray',
                alpha=0.3,zorder=-10,
                label=scen_list_out[scen])
ax.set_xlim([2000,2030])
ax.set_ylim([-0.2,2.0])

print('Forced:')
print('Mean 2006 to 2020')
print(post_rib['Median'].loc[2006:2020].mean())
print('Mean 1971 to 2020')
print(post_rib['Median'].loc[1971:2020].mean())


post_rib=pd.read_csv('results_csv_rib/summary_rib_calc_timeseries_' + scen + '.csv',
                     index_col=0)

y = post_rib['Median'].loc[2005:2022]
x = y.index
b, a = np.polyfit(x.values, y.values, deg=1)
xseq = x.values
ax.plot(xseq, a + b * xseq, color="red", lw=0.5,linestyle='-.');
ax.text(2022.5, (a + b * 2022)-0.1, '{:2.2f}'.format(b*10.0)+' Wm$^{-2}$ dec$^{-1}$',
        color="red",fontsize=10)

ax.fill_between(post_rib.index, post_rib['5perc'],post_rib['95perc'],
                 color='red',
                 alpha=0.3,zorder=-10,label='Include ENSO variability')

ax.set_ylabel('Earth Energy Imbalance [W m$^{-2}$]')

val = 0.76
unc = 0.2
ax.plot([2006,2020],[val,val],'-',zorder=10,color='orange',linewidth = 2,
        label='von Schuckmann et al. (2023)' )
ax.plot([2006,2020],[val+unc,val+unc],'--',zorder=10,color='orange',linewidth = 2)
ax.plot([2006,2020],[val-unc,val-unc],'--',zorder=10,color='orange',linewidth = 2)

print('From the calculated:')
print('Mean 2006 to 2020')
print(post_rib['Median'].loc[2006:2020].mean())
print('Mean 1971 to 2020')
print(post_rib['Median'].loc[1971:2020].mean())



#Add CERES data:
path_orig = '/div/qbo/utrics/ClimateSensitivity/updateAR6/scripts_other/RadiativeImbalance/'
ceres_values =pd.read_csv(path_orig+'DataFromCaroline/EEI_12_month_running_mean_200003_202401.csv',
                          index_col=None)
print(ceres_values['time'].values)
ceres_dates = pd.to_datetime(ceres_values['time'], format='%Y-%m-%d')
print(ceres_dates)

# Calculate the start of the year and the next year
year_start = pd.to_datetime(ceres_dates.dt.year.astype(str) + '-01-01')
next_year_start = pd.to_datetime((ceres_dates.dt.year + 1).astype(str) + '-01-01')
    
# Calculate the number of days in the year
days_in_year = (next_year_start - year_start).dt.days
    
# Calculate the number of days since the start of the year
days_since_start_of_year = (ceres_dates - year_start).dt.days
    
# Calculate the decimal year
decimal_year = ceres_dates.dt.year + days_since_start_of_year / days_in_year

ax.plot(decimal_year,ceres_values['Net_Flux_Rolling'].values,'-',color='blue',linewidth = 1,label='CERES')

ceres_df = pd.DataFrame(data=ceres_values['Net_Flux_Rolling'].values,columns=['net'],index=decimal_year)
y = ceres_df['net'].loc[2005:2022]
x = y.index
print(x)
print(y)

print('Mean CERES net')
print(y.loc[2005:2020].mean())


b, a = np.polyfit(x.values, y.values, deg=1)
xseq = x.values
ax.plot(xseq, a + b * xseq, color="blue",linestyle= '-.',lw=0.5)# ,label = str(b*10.0))
#ax.text(2022.5, a + b * 2022, '{:2.2f}'.format(b*10.0)+' Wm$^{-2}$ dec$^{-1}$', color="blue",fontsize=10)

print('Increase in EEI') 
print(ceres_df['net'].loc[2000:2009].mean())
print(ceres_df['net'].loc[2010:2019].mean())

d0009 = ceres_df['net'].loc[2000:2009].mean()
d1019 = ceres_df['net'].loc[2010:2019].mean()

print((d1019 - d0009)/d0009)
    


ax.legend(loc='upper left',fontsize=9,frameon=False)




ax = axes["bottom left"]
for sc,scen in enumerate(scen_list_out_c):
    if scen[0:5]=='Space':
        continue
    #Forced rib:
    post_rib=pd.read_csv('results_csv_rib/summary_rib_timeseries_' + scen + '.csv',
                         index_col=0)

    ax.plot(post_rib.index, post_rib['Median'],linestyle='--',
            linewidth=0.5,color=scen_list_colors[scen])#,label=scen_list_out[scen])
    y = post_rib['Median'].loc[2005:2019]
    x = y.index
    
    b, a = np.polyfit(x.values, y.values, deg=1)
    xseq = x.values
    print(scen)
    print(scen_list_out[scen])
    print( '{:2.2f}'.format(b*10.0))
    label_text = scen_list_out[scen]+ ' [{:2.2f}]'.format(b*10.0)

    print(label_text)
    ax.plot(xseq, a + b * xseq, color=scen_list_colors[scen],
            linestyle= '-',lw=2,label=label_text)




ax.set_xlim([2000,2023])
ax.set_ylim([0.2,1.1])   
ax.legend(ncol=1,fontsize=8,frameon=False)
ax.set_ylabel('Earth Energy Imbalance [W m$^{-2}$]')





axes["right"].set_xlabel('Earth Energy Imbalance trend [(W m$^{-2}$) dec$^{-1}$]')

axes["top left"].set_title('a) Earth Energy Imbalance',loc='left')
axes["right"].set_title('b) Forced Earth Energy Imbalance trend 2005-2019 ',loc='left')
axes["bottom left"].set_title('c) Forced Earth Energy Imbalance',loc='left')


plt.savefig('Figures/rib_fig.png')
plt.show()
