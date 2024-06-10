import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

def dict_for_simulations_all():

    print('Hei')
    scen_list_out = {'OutputAnalyse01':'Skeie18, AR5 prior',
                     'OutputAnalyse02':'Update obs. end year 2014',
                     'OutputAnalyse03':'Replace AR5 prior with AR6',
                     'OutputAnalyse04':'End year 2019',
                     'OutputAnalyse19NewPrior_W_cpi_2':'Base',
                     'Space0':'',
                     'Space6':'Extend to 2022',
                     'OutputAnalyse28':'Replace AR6 prior with AR6 extended',
                     'OutputAnalyse29':'Update obs. end year 2019',
                     'OutputAnalyse30':'Base extended (end year 2022)',
                     'Space7':'',
                     'Space1':'Sensitivity test:',
                     'OutputNewAnalyse05Smooth':'Smooth',
                     'Space2':'',
                     'OutputNewAnalyse06Linear1750to1900':'Linear1750to1900',
                     'OutputNewAnalyse07Weaker1900to1950':'Weaker1900to1950',
                     'OutputNewAnalyse08Stronger1900to1950':'Stronger1900to1950',
                     'OutputNewAnalyse09Weaker1950to1980':'Weaker1950to1980',
                     'OutputNewAnalyse10Stronger1950to1980':'Stronger1950to1980',
                     'OutputNewAnalyse12StrongerWeaker1980to2019':'StrongerWeaker1980to2019',
                     'OutputNewAnalyse13Stronger1980to2019':'Stronger1980to2019',
                     'OutputNewAnalyse15LinWeaker2014to2019':'LinWeaker2014to2019',
                     'Space3':'',
                     'OutputAnalyse24LinredSmoothbase1950to1990':'Linear1950to1990',
                     'OutputAnalyse25LinredSmoothbase1950to2000':'Linear1950to2000',
                     'OutputAnalyse26LinredSmoothbase1950to2010':'Linear1950to2010',
                     'OutputAnalyse27LinredSmoothbase1950to2019':'Linear1950to2019',
                     'Space4':'',
                     'OutputAnalyse31LinredSmoothbase1950to1980Flat':'Linear1950to1980 then flat',
                     'OutputAnalyse32LinredSmoothbase1950to1990Flat':'Linear1950to1990 then flat',
                     'OutputAnalyse33LinredSmoothbase1950to2000Flat':'Linear1950to2000 then flat',
                     'Space5':'',
                     'Space8':'ERFaci trend test',
                     'OutputAnalyse34':'Unc. in 1950 and 2014 independent'}
                     
    
    antscen = len(scen_list_out)

    antcolors = 8
    colorlist_org = cm.terrain(np.linspace(0,0.8,antcolors))
    colorlist = cm.terrain(np.linspace(0,0.9,7))
    colorlist = colorlist_org
    #colorlist[0] = colorlist_org[0]
    #colorlist[1] = colorlist_org[1]
    #colorlist[2] = colorlist_org[2]
    #colorlist[3] = colorlist_org[3]
    #colorlist[4] = colorlist_org[4]
    #colorlist[5] = colorlist_org[5]
    #colorlist[6] = colorlist_org[6]
    
    scen_colorlist = {'OutputAnalyse01':colorlist[0],
                      'OutputAnalyse02':colorlist[0],
                      'OutputAnalyse03':colorlist[0],
                      'OutputAnalyse04':colorlist[0],
                      'OutputAnalyse19NewPrior_W_cpi_2':colorlist[0],
                      'OutputNewAnalyse05Smooth':colorlist[1],
                      'OutputNewAnalyse06Linear1750to1900':colorlist[2],
                      'OutputNewAnalyse07Weaker1900to1950':colorlist[2],
                      'OutputNewAnalyse08Stronger1900to1950':colorlist[2],
                      'OutputNewAnalyse09Weaker1950to1980':colorlist[2],
                      'OutputNewAnalyse10Stronger1950to1980':colorlist[2],
                      'OutputNewAnalyse12StrongerWeaker1980to2019':colorlist[2],
                      'OutputNewAnalyse13Stronger1980to2019':colorlist[2],
                      'OutputNewAnalyse15LinWeaker2014to2019':colorlist[2],
                      'OutputAnalyse24LinredSmoothbase1950to1990':colorlist[3],
                      'OutputAnalyse25LinredSmoothbase1950to2000':colorlist[3],
                      'OutputAnalyse26LinredSmoothbase1950to2010':colorlist[3],
                      'OutputAnalyse27LinredSmoothbase1950to2019':colorlist[3],
                      'OutputAnalyse31LinredSmoothbase1950to1980Flat':colorlist[4],
                      'OutputAnalyse32LinredSmoothbase1950to1990Flat':colorlist[4],
                      'OutputAnalyse33LinredSmoothbase1950to2000Flat':colorlist[4],
                      'OutputAnalyse28':colorlist[5],
                      'OutputAnalyse29':colorlist[5],
                      'OutputAnalyse30':colorlist[5],
                      'OutputAnalyse34':colorlist[6],
                      'OutputAnalyse34withFewerSeries':colorlist[6]}

    return scen_list_out, scen_colorlist
