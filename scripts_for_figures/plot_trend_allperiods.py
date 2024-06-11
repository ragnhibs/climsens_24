import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


yrlist = np.array([1960,1970,1980,1990,2000,2010])

yr_period = ['1950-1969',
             '1960-1979',
             '1970-1989',
             '1980-1999',
             '1990-2009',
             '2000-2019']

trend_ar6 = pd.DataFrame(data=[],index=yrlist,columns=['aero'])

fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(12,6))

scen_list  =['OutputAnalyse30','OutputAnalyse34']
scen_list_out = {'OutputAnalyse30':'Base extended (end year 2022)',
                 'OutputAnalyse34':'Unc. in 1950 and 2014 independent'}

rf_comp = 'aero' 

colorlist = ['blue','green']
label_prior_median = 'Prior median'
label_post_median = 'Posterior median'
label5_95='5th to 95th percentile'
label30_70='30th to 70th percentile'


for sc,scen in enumerate(scen_list):
    scenlabel = scen_list_out[scen]
    trend_prior = pd.DataFrame(data=[],index=yrlist,
                               columns=['5pc','50pc','95pc','30pc','70pc'])
    trend = pd.DataFrame(data=[],index=yrlist,
                         columns=['5pc','50pc','95pc','30pc','70pc'])

    
    df_trend = pd.read_csv('results_csv_erf_trend/erf'
                           +rf_comp+'_trend_allperiods'
                           '_'+scen+'.csv',index_col=0)
    df_trend_prior = pd.read_csv('results_csv_erf_trend/erf_prior'
                                 +rf_comp+'_trend_allperiods'
                                 +'_'+scen +'.csv',index_col=0)
    
    df_trend = df_trend.multiply(10)
    df_trend_prior = df_trend_prior.multiply(10)

    pc5 = df_trend_prior.quantile(.05)
    pc95 = df_trend_prior.quantile(.95)
    pc50 = df_trend_prior.quantile(.5)

    trend_prior['5pc'] = pc5.values
    trend_prior['50pc'] = pc50.values
    trend_prior['95pc'] = pc95.values
    trend_prior['70pc'] = df_trend_prior.quantile(.70).values
    trend_prior['30pc'] = df_trend_prior.quantile(.30).values

    c5 = df_trend.quantile(.05)
    pc95 = df_trend.quantile(.95)
    pc50 = df_trend.quantile(.5)

    trend['5pc'] = pc5.values
    trend['50pc'] = pc50.values
    trend['95pc'] = pc95.values
    trend['70pc'] = df_trend.quantile(.70).values
    trend['30pc'] = df_trend.quantile(.30).values
        
    
    for yr in yrlist:
        yrix = yr-1.5+sc*2
        axs.plot(yrix,trend_prior['50pc'].loc[yr],'x',markersize=6,
                 color='darkgray',label=label_prior_median)

        label_prior_median = None
        
        axs.plot([yrix,yrix],[trend_prior['5pc'].loc[yr],
                              trend_prior['95pc'].loc[yr]],
                 color='darkgray',label=label5_95)

        axs.plot([yrix,yrix],[trend_prior['30pc'].loc[yr],
                              trend_prior['70pc'].loc[yr]],
                 linewidth=3,color='darkgray',label=label30_70)
       
        label5_95=None
        label30_70=None

        yrix = yr-1.5+sc*2+1
        axs.plot(yrix,trend['50pc'].loc[yr],'s',markersize=6,
                 color=colorlist[sc],label=scenlabel)

        label_post_median = None
        scenlabel = None
        axs.plot([yrix,yrix],[trend['5pc'].loc[yr],trend['95pc'].loc[yr]],
                 color=colorlist[sc],linewidth=1, label=scenlabel)

        scenlabel = None
        axs.plot([yrix,yrix],[trend['30pc'].loc[yr],trend['70pc'].loc[yr]],
                 color=colorlist[sc],linewidth=3, label=scenlabel)
        


# Numbers from Fig 5 in Quaas et al. ACP 2022
#This yields a constrained trend
#of 0.0114 (-0.003 to 0.0274) W m-2 yr-1

yrix = 2014
smith_50pc = 0.0114*10.0
smith_90ci = np.array([-0.003,0.0274])*10.0

axs.plot(yrix,smith_50pc,'o',color='black',
         label='Smith et al., 2021 constrained')
axs.plot([yrix,yrix],smith_90ci,color='black',linewidth=1)


#Their baseline estimate yields a
#mean trend of 0.0047 W m-2 yr-1
#(5-95 confidence iterval of -0.000912 to 0.0106 W m-2 yr-1
yrix = 2015
albright_50pc = 0.0047*10.0
albright_90ci = np.array([-0.000912,0.0106])*10.0

axs.plot(yrix,albright_50pc,'o',color='darkgray',label='Albright et al., 2021')
axs.plot([yrix,yrix],albright_90ci,color='darkgray',linewidth=1)


yrix = 2016
albright_2_50pc = 0.008*10.0
albright_2_90ci = np.array([0.002,0.016])*10.0

axs.plot(yrix,albright_2_50pc,'o',color='gray',
         label='Albright et al., 2021 increased var.')
axs.plot([yrix,yrix],albright_2_90ci,color='gray',linewidth=1)



#Add CMIP6:
labelcmip6='CMIP6 models'
trend_cmip6 = pd.read_csv('results_csv_erf_trend/erf_cmip6_trend_allperiods.csv',index_col=0)
trend_cmip6_raw = pd.read_csv('results_csv_erf_trend/erf_cmip6_raw_trend_allperiods.csv',index_col=0)
print(trend_cmip6)
trend_cmip6=trend_cmip6*10.0
trend_cmip6_raw=trend_cmip6_raw*10.0
for yrix in trend_cmip6.columns:
    for mod in trend_cmip6.index:
        axs.plot(int(yrix)+3,trend_cmip6[yrix].loc[mod],'*',color='gray',label=labelcmip6)
        labelcmip6=None

#for yrix in trend_cmip6_raw.columns:
#    for mod in trend_cmip6_raw.index:
#        axs.plot(int(yrix)+3,trend_cmip6_raw[yrix].loc[mod],'x',color='blue')




axs.axhline(y=0,linestyle='--',linewidth=1,zorder=-1,color='black')
axs.set_ylabel('20 year aerosol ERF linear trend [W m$^{-2}$ decade$^{-1}$]')
axs.legend(ncol=2,frameon=False)

axs.set_xticks([])

axs.set_xticks(yrlist)
axs.set_xticklabels(yr_period)
axs.tick_params(bottom = False) 
#set_xticklabel(yr_period)
#axs.xaxis.set_tick_params(label=yr_period)

print(np.array(yrlist))
print(yr_period)

plt.savefig('Figures/erf_trend_allperiods.png')
plt.show()
