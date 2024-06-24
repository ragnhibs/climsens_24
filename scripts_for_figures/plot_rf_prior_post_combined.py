#Plot RF timeseries and pdf for selected components, prior and post
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from dict_for_simulations import dict_for_simulations

plt.rcParams['font.size'] = 4
plt.rcParams['figure.dpi'] = 300



def plot_pdf_posterior():
    for sc,scen in enumerate(scen_list):
        if scen == 'OutputAnalyse19NewPrior_W_cpi_2':
            filename = scen + '_gaussiankde_posterior_rf_'+ rf_comp+'_2014.csv'
            print('Filename:')
            print(filename)
        else:
            filename = scen + '_gaussiankde_posterior_rf_'+ rf_comp+'.csv'
            print('Filename:')
            print(filename)

            
        post_rf=pd.read_csv('results_csv/'+filename,
                            index_col=0)
         
        ax.plot(post_rf.index,post_rf.values,
                linewidth=0.8,color=colorlist[sc],
                label='Posterior '+ scen_list_out[scen])
        
def plot_pdf_prior():
    for sc,scen in enumerate(scen_list):
        if scen == 'OutputAnalyse19NewPrior_W_cpi_2':
            filename = scen + '_gaussiankde_prior_rf_'+ rf_comp+'_2014.csv'
            print('Filename:')
            print(filename)
        else:
            filename = scen + '_gaussiankde_prior_rf_'+ rf_comp+'.csv'
            print('Filename:')
            print(filename)
            
        prior_rf=pd.read_csv('results_csv/'+filename,
                            index_col=0)
         
        ax.plot(prior_rf.index,prior_rf.values,'--',
                linewidth=0.8,color=colorlist[sc],
                label=scen_list_out_prior[scen])
        

def plot_summary():
    #summary_all = []
    list_text = rf_list_text[rf_comp]

    label_mean = 'Posterior mean'
    label_prior = 'Prior mean'
    label_ci = '90% C.I.'
    
    for sc,scen in enumerate(scen_list_out):
        if scen[0:5]=='Space':
            ax.text(list_text,antscen-sc-0.15,scen_list_out[scen],color='black',weight='bold')
            continue

        if scen == 'OutputAnalyse01':
            summary_erf_prior = pd.read_csv('results_csv/summary_prior_rf_'
                                            +scen+str(scen_end_yr[scen])+ '_allcomp.csv',index_col=0)
            
            summary_erf_prior = summary_erf_prior.loc[rf_comp]
            ax.plot(summary_erf_prior['mean'],antscen-sc+0.50,'s',markersize=3,
                    color='gray',label=label_prior)
            ax.plot([summary_erf_prior['5perc'],summary_erf_prior['95perc']],
                    [antscen-sc+0.50, antscen-sc+0.50],'--',linewidth=1,color='gray')#,
                    #label='90% C.I.')
            textline = 'AR5 prior 2014'
            ax.text(list_text,antscen-sc+0.35,textline,color='gray')
            summary_erf_prior.name = textline
            summary_all_prior = summary_erf_prior.T

        
        summary_erf = pd.read_csv('results_csv/summary_posterior_rf_'+scen+str(scen_end_yr[scen])+ '_allcomp.csv',
                                  index_col=0)
        summary_erf = summary_erf.loc[rf_comp]

        if scen == 'OutputAnalyse01':
        #    print(summary_erf)
        #    exit()
            summary_erf.name = scen_list_out[scen]
        #    print('Her')
        #    summary_all=summary_erf
        else:
            summary_erf.name = scen_list_out[scen]
        #    summary_all=pd.concat([summary_all,summary_erf])

        if scen_list_out[scen] == 'Base':
            print(summary_erf)
        if scen_list_out[scen] == 'Base extended (end year 2022)':
            print(summary_erf)

            
        ax.plot(summary_erf['mean'],antscen-sc,'o',markersize=3,
                 color=scen_colorlist[scen],label=label_mean)
        ax.plot([summary_erf['5perc'],summary_erf['95perc']],
                 [antscen-sc, antscen-sc],'-',linewidth=1,color=scen_colorlist[scen],
                 label=label_ci)
        textline = scen_list_out[scen]
        ax.text(list_text,antscen-sc-0.15,textline,color='black') #scen_colorlist[scen])

        label_mean = None
        label_ci = None
        label_prior = None
        

        if scen == 'OutputAnalyse03':
            summary_erf_prior = pd.read_csv('results_csv/summary_prior_rf_'+scen+str(scen_end_yr[scen])+ '_allcomp.csv',index_col=0)
            
            summary_erf_prior = summary_erf_prior.loc[rf_comp]
            ax.plot(summary_erf_prior['mean'],antscen-sc+0.50,'s',markersize=3,
                 color='gray') #,label='Mean')
            ax.plot([summary_erf_prior['5perc'],summary_erf_prior['95perc']],
                    [antscen-sc+0.50, antscen-sc+0.50],'--',linewidth=1,color='gray')
                    #label='90% C.I.')
            textline = 'AR6 prior 2014'
            ax.text(list_text,antscen-sc+0.35,textline,color='gray')

            summary_erf_prior.name = textline
            summary_all_prior = pd.concat([summary_all_prior,summary_erf_prior],axis=1)
            
        if scen == 'OutputAnalyse19NewPrior_W_cpi_2':
            scen_prior = 'OutputAnalyse04'
            summary_erf_prior = pd.read_csv('results_csv/summary_prior_rf_'+scen_prior+str(scen_end_yr[scen])+ '_allcomp.csv',index_col=0)
            
            summary_erf_prior = summary_erf_prior.loc[rf_comp]
            ax.plot(summary_erf_prior['mean'],antscen-sc+0.50,'s',markersize=3,
                 color='gray')#,label='Mean')
            ax.plot([summary_erf_prior['5perc'],summary_erf_prior['95perc']],
                    [antscen-sc+0.50, antscen-sc+0.50],'--',linewidth=1,color='gray')
#                    label='90% C.I.')
            textline = 'AR6 prior 2019'
            ax.text(list_text,antscen-sc+0.35,textline,color='gray')

            print('Prior:'+scen)
            print(summary_erf_prior)

            summary_erf_prior.name = textline
            summary_all_prior = pd.concat([summary_all_prior,summary_erf_prior],axis=1)
            
        if scen == 'OutputAnalyse28':
            summary_erf_prior = pd.read_csv('results_csv/summary_prior_rf_'+scen+str(scen_end_yr[scen])+ '_allcomp.csv',index_col=0)
            
            summary_erf_prior = summary_erf_prior.loc[rf_comp]
            ax.plot(summary_erf_prior['mean'],antscen-sc+0.50,'s',markersize=3,
                 color='gray')#,label='Mean')
            ax.plot([summary_erf_prior['5perc'],summary_erf_prior['95perc']],
                    [antscen-sc+0.50, antscen-sc+0.50],'--',linewidth=1,color='gray')
                    #label='90% C.I.')
            textline = 'AR6 extended prior 2019'
            ax.text(list_text,antscen-sc+0.35,textline,color='gray')

            summary_erf_prior.name = textline
            summary_all_prior = pd.concat([summary_all_prior,summary_erf_prior],axis=1)
            
        if scen == 'OutputAnalyse30':
            summary_erf_prior = pd.read_csv('results_csv/summary_prior_rf_'+scen+str(scen_end_yr[scen])+ '_allcomp.csv',index_col=0)
            
            summary_erf_prior = summary_erf_prior.loc[rf_comp]
            ax.plot(summary_erf_prior['mean'],antscen-sc+0.50,'s',markersize=3,
                 color='gray')#,label='Mean')
            ax.plot([summary_erf_prior['5perc'],summary_erf_prior['95perc']],
                    [antscen-sc+0.50, antscen-sc+0.50],'--',linewidth=1,color='gray')
                    #label='90% C.I.')
            textline = 'AR6 extended prior 2022'
            ax.text(list_text,antscen-sc+0.35,textline,color='gray')    

            summary_erf_prior.name = textline
            summary_all_prior = pd.concat([summary_all_prior,summary_erf_prior],axis=1)
            
        if scen_list_out[scen]=='Smooth':
            ax.axvline(summary_erf.loc['mean'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
            ax.axvline(summary_erf.loc['5perc'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)
            ax.axvline(summary_erf.loc['95perc'],linestyle='--',color='darkgray',linewidth=0.5,zorder=0)


        #print(summary_erf)
        #print(summary_all)
        #print(scen)
        #exit()
        if scen == 'OutputAnalyse01':
            summary_all = summary_erf.T
        else:
            summary_all = pd.concat([summary_all,summary_erf],axis=1)
    
    
    pd.options.display.float_format = '{:,.2f}'.format
    print('Prior')
    #summary_all_prior = summary_all_prior.rename(index=scen_list_out)
    print(summary_all_prior.transpose())       

    print('Posterior')
    #print(summary_all.transpose())
    
    #summary_all = summary_all.rename(index=scen_list_out)
    print(summary_all.transpose())
    
def plot_results_timeseries_posteriori():
    for sc,scen in enumerate(scen_list):
        filename_posterior = 'summary_rf_posterior_timeseries_'+rf_comp+scen+'.csv'
        posterior_rf=pd.read_csv('results_csv/'+filename_posterior,
                             index_col=0)
        ax.fill_between(posterior_rf.index, posterior_rf['5perc'],
                        posterior_rf['95perc'],
                        color=colorlist[sc],edgecolor=None,
                        alpha=0.3,
                        label='Posterior 90% C.I. ' + scen_list_out[scen])
       
        ax.plot(posterior_rf['Median'],'-',linewidth=0.5,
                color=colorlist[sc],zorder=10,
                label='Posterior median '+ scen_list_out[scen])
        
    ax.axhline(0.0,linestyle='-',linewidth=0.5,color='lightgray')
        

def plot_results_timeseries_prior():
    for sc,scen in enumerate(scen_list):
        filename_prior = 'summary_rf_prior_timeseries_'+rf_comp+scen+'.csv'
        prior_rf=pd.read_csv('results_csv/'+filename_prior,
                             index_col=0)
        ax.plot(prior_rf['Median'],'--',linewidth=0.5,
                color=colorlist[sc],zorder=10,
                label='Prior median '+scen_list_out_prior[scen])
        ax.plot(prior_rf['95perc'],':',linewidth=0.5,color=colorlist[sc])
        ax.plot(prior_rf['5perc'],':',linewidth=0.5,color=colorlist[sc],
                label='Prior 90% C.I. '+scen_list_out_prior[scen])



#Start here

summary_all = pd.DataFrame([])
print(summary_all)


scen_list_out_prior = {'OutputAnalyse04':'AR6 prior',        
                       'OutputAnalyse01':'AR5 prior',
                       'OutputAnalyse30':'AR6 ext. prior',
                       'OutputAnalyse19NewPrior_W_cpi_2':'AR6 prior' }

scen_end_yr = {'OutputAnalyse01':2014,
               'OutputAnalyse02':2014,
               'OutputAnalyse03':2014,
               'OutputAnalyse04':2019,
               'OutputAnalyse19NewPrior_W_cpi_2':2019,
               'OutputNewAnalyse05Smooth':2019,
               'OutputNewAnalyse06Linear1750to1900':2019,
               'OutputNewAnalyse07Weaker1900to1950':2019,
               'OutputNewAnalyse08Stronger1900to1950':2019,
               'OutputNewAnalyse09Weaker1950to1980':2019,
               'OutputNewAnalyse10Stronger1950to1980':2019,
               'OutputNewAnalyse12StrongerWeaker1980to2019':2019,
               'OutputNewAnalyse13Stronger1980to2019':2019,
               'OutputNewAnalyse15LinWeaker2014to2019':2019,
               'OutputAnalyse24LinredSmoothbase1950to1990':2019,
               'OutputAnalyse25LinredSmoothbase1950to2000':2019,
               'OutputAnalyse26LinredSmoothbase1950to2010':2019,
               'OutputAnalyse27LinredSmoothbase1950to2019':2019,
               'OutputAnalyse31LinredSmoothbase1950to1980Flat':2019,
               'OutputAnalyse32LinredSmoothbase1950to1990Flat':2019,
               'OutputAnalyse33LinredSmoothbase1950to2000Flat':2019,
               'OutputAnalyse28':2019,
               'OutputAnalyse29':2019,
               'OutputAnalyse30':2022,
               'OutputAnalyse34':2022}

scen_list_out,scen_colorlist =  dict_for_simulations()
antscen = len(scen_list_out)

rf_comp = 'antro' #'antro' #aero' #antro' #'aero' #antro' #'aero' #antro' #'Tot' #'antro' #'aero' #'antro' #'aero'

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
                'AEROSOLCI':'Aerosol ERFaci'}

rf_list_text = {'Tot':-0.5,
                'antro':-0.5,
                'aero':0.1,
                'LLGHG':-0.5,
                'O3': 3,
                'LANDUSE':3,
                'CONTRAILS':3,           
                'STRATH2O': 3,           
                'SNOWALBEDO': 3,
                'SUN': 3,
                'VOLC_annual':3,
                'AEROSOLRI':0.1,
                'AEROSOLCI':0.1}

rf_list_xlim = {'Tot':[-1,4],
                'antro':[-1,5.5],
                'aero':[-2,2.5],
                'LLGHG':[-1,5],
                'O3': 3,
                'LANDUSE':3,
                'CONTRAILS':3,           
                'STRATH2O': 3,           
                'SNOWALBEDO': 3,
                'SUN': 3,
                'VOLC_annual':3,
                'AEROSOLRI':[-2,2.1],
                'AEROSOLCI':[-2,2.1]}


fig, axes = plt.subplot_mosaic(
    [["top left",  "right"],
     ["bottom left", "right"]],
    figsize=(7,3.7)
)



ax = axes["bottom left"]
scen_list = ['OutputAnalyse01','OutputAnalyse19NewPrior_W_cpi_2']
colorlist = ['C2','black']
#colorlist = [scen_colorlist[scen_list[0]],scen_colorlist[scen_list[1]]]
plot_results_timeseries_posteriori()

ax = axes["top left"]
plot_pdf_posterior()




ax = axes["bottom left"]
scen_list = ['OutputAnalyse01','OutputAnalyse04']
colorlist = ['C2','black'] #['darkgray','black']
plot_results_timeseries_prior()



#get handles and labels
handles, labels = plt.gca().get_legend_handles_labels()
#specify order of items in legend
order = [4,5,1,0,6,7,3,2]
#add legend to plot
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],frameon=False)

#ax.legend(frameon=False)

ax = axes["top left"]
scen_list = ['OutputAnalyse01','OutputAnalyse19NewPrior_W_cpi_2']
plot_pdf_prior()

ax.legend(frameon=False)

ax = axes["right"]
antscen = len(scen_list_out)
colorlist = scen_colorlist #cm.terrain(np.linspace(0,0.9,antscen))


#print(antscen)
#colorlist[7] = colorlist[4]
#colorlist[1:5]=colorlist[0]
#colorlist[18:22]=colorlist[20]
#colorlist[-4:]=colorlist[25]
#colorlist[8:18]=colorlist[5]


plot_summary()
ax.set_xlim(rf_list_xlim[rf_comp])
ax.set_yticks([])
ax.legend(frameon=False,loc='upper right')

#plt.suptitle(rf_list_long[rf_comp])
axes["top left"].set_xlabel('ERF [W m$^{-2}$]')
axes["top left"].set_ylabel('Probability density')
axes["bottom left"].set_ylabel('ERF [W m$^{-2}$]')
axes["bottom left"].set_xlabel('Year')
axes["right"].set_xlabel('ERF [W m$^{-2}$]')



axes["top left"].set_title('a) '+ rf_list_long[rf_comp] + ' in 2014' ,loc='left')
axes["right"].set_title('b) '+ rf_list_long[rf_comp] + ' at end year',loc='left')
axes["bottom left"].set_title('c) '+ rf_list_long[rf_comp] + ' time evolution',loc='left')





plt.tight_layout()
plt.savefig('Figures/'+rf_comp+'ERF_alt2.png')





plt.show()
