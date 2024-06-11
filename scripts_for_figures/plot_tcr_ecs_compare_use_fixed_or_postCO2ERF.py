import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(15,6))

scen = 'OutputAnalyse30'

filename = scen + '_gaussiankde_ecsinf.csv'
filepath_use_post = 'results_csv_use_postCO2/'
filepath_use_const = 'results_csv_use_constCO2/'



co2_erf = 3.93
fname = filepath_use_const + filename 
gaussian_df = pd.read_csv(fname,index_col=0)
axs[0].plot(gaussian_df,linewidth=1,color='blue',
            label='Base ext. ['+str(co2_erf) + ' W m$^{-2}$]' )

fname = filepath_use_post + filename 
gaussian_df = pd.read_csv(fname,index_col=0)
axs[0].plot(gaussian_df,linewidth=1,color='orange',
            label='Base ext. (post CO2 ERF)')
axs[0].legend(frameon=False)
axs[0].set_xlim([0,5])
axs[0].set_title('a)',loc='left')
axs[0].set_xlabel('ECS$_{inf}$ [$^\circ$C]')


#Plot TCR
filename = scen + '_gaussiankde_tcr_ar6erf.csv'
fname = filepath_use_const + filename 
gaussian_df = pd.read_csv(fname,index_col=0)
axs[1].plot(gaussian_df,linewidth=1,color='blue',
            label='Base ext. ['+str(co2_erf) + ' W m$^{-2}$]' )

#ADD new TCR here
filename = scen + '_gaussiankde_tcr_modified.csv'
fname = filepath_use_post + filename 
gaussian_df = pd.read_csv(fname,index_col=0)
axs[1].plot(gaussian_df,linewidth=1,color='orange',
            label='Base ext. (post CO2 ERF)')

axs[1].legend(frameon=False)
axs[1].set_xlim([0,3])
axs[1].set_title('b)',loc='left')
axs[1].set_xlabel('TCR [$^\circ$C]')


plt.show()
