#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:25:57 2022

@author: savard
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pyPLUTO as pypl
import pyPLUTO.pload as pp
import gc
import matplotlib.font_manager as fm
#matplotlib.use('Agg') # for avoiding memory leak


sys.path.append("$PLUTO_DIR/Tools/pyPLUTO/pyPLUTO/")

def set_plot_defaults():
    """
    assign default plot settings
    """
    ## FIGURE
    #plt.rcParams["text.usetex"] = "True"

    ## FONTplut 
    #plt.rcParams['font.serif']=['cm']
    #plt.rcParams['font.family']='serif'
    # plt.rcParams['font.serif']=['cm']
    plt.rcParams['text.latex.preamble']=r'\usepackage{amsmath}'

    plt.rcParams['font.size']=18
    plt.rcParams['xtick.labelsize']=15
    plt.rcParams['ytick.labelsize']=15
    plt.rcParams['legend.fontsize']=14
    plt.rcParams['axes.titlesize']=16
    plt.rcParams['axes.labelsize']=16
    plt.rcParams['axes.linewidth']=2
    plt.rcParams["lines.linewidth"] = 2.2
    ## TICKS
    plt.rcParams['xtick.top']='True'
    plt.rcParams['xtick.bottom']='True'
    plt.rcParams['xtick.minor.visible']='True'
    plt.rcParams['xtick.direction']='out'
    plt.rcParams['ytick.left']='True'
    plt.rcParams['ytick.right']='True'
    plt.rcParams['ytick.minor.visible']='True'
    plt.rcParams['ytick.direction']='out'
    plt.rcParams['xtick.major.width']=1.5
    plt.rcParams['xtick.minor.width']=1
    plt.rcParams['xtick.major.size']=4
    plt.rcParams['xtick.minor.size']=3
    plt.rcParams['ytick.major.width']=1.5
    plt.rcParams['ytick.minor.width']=1
    plt.rcParams['ytick.major.size']=4
    plt.rcParams['ytick.minor.size']=3

def save_list(d,folder,name):
    """ saves a np array into a given location
    """
    if not os.path.isdir(folder):
        os.mkdir(folder)
    file = folder+'/'+name+'.npy'
    np.save(file,d)

def load_list(folder, name):
    """loads a numpy array from a given location
    """
    file = folder+'/'+name+'.npy'
    arr = np.load(file,allow_pickle=True)
    return arr

def save_fig(dir_title,fig_title,overwrite=False):
    """saves a figure to a given location. includes a switch to 
    check if you want to overwrite the figure if it already exists. 
    """
    if not os.path.isdir(dir_title):
        os.mkdir(dir_title)
    if os.path.exists(dir_title+"/"+fig_title+".jpg"):
        if overwrite==True:
            print("Overwriting existing figure!!!")
            print('high dpi')
            plt.savefig(dir_title+"/"+fig_title+'.jpg',bbox_inches='tight',dpi=400)
        else:
            print("Not overwriting existing figure!!!!")
    else:
        print("saving new figure!!")
        plt.savefig(dir_title+"/"+fig_title+'.jpg',bbox_inches='tight',dpi=400)

def load_data_obj(wdir_in_PLUTO, num=-1, data_type='dbl'):
    """
    Function to load a .dbl file into an object ad a corresponding image

    Parameters
    ----------
    wdir_in_PLUTO : string
        name of local directory in $PLUTO_DIRs
    num : int
        timestep to load, default is the last timestep, or else specify between zero and last step

    Returns
    -------
    D : Data object
        pyPLUTO data object with all attributes from .dbl file
    I : Image object
        pyPLUTO image object made from Data object 

    """
    plutodir = os.environ['PLUTO_DIR']
    wdir = plutodir+wdir_in_PLUTO
    if num==-1:
        nlinf = pypl.nlast_info(w_dir=wdir)
        try:
            D = pp.pload(nlinf['nlast'],w_dir=wdir,datatype=data_type) # Loading the data into a pload object D.
        except:
            print('float type data')            
            D = pp.pload(nlinf['nlast'],w_dir=wdir,datatype='flt')
    else: 
        try:
            D = pp.pload(num,w_dir=wdir,datatype=data_type) # Loading the data into a pload object D.
        except:
            print('float type data') 
            D = pp.pload(num,w_dir=wdir,datatype='flt')
    return D

def plot_cmesh(ax1,ax2,var,title,figsize,vmin=0,vmax=0):
    """
    Plotting function for 2D colorplot

    Parameters
    ----------
    ax1 : 1D array
        x-axis
    ax2 : 1D array
        y-axis
    var : 2D array
        variable to be plotted
    title : string
        plot title
    figsize : [int,int]
        matplotlib figure dimensions

    Returns
    -------
    Quadmesh object (matplotlib object)

    """
    plt.figure(figsize=figsize)
    plt.title(title)
    if vmin==0 and vmax==0:
        plt.pcolormesh(ax1,ax2,var.T,shading='auto')
        plt.pcolormesh(-ax1,ax2,var.T,shading='auto')
        plt.tight_layout()
    else:
        plt.pcolormesh(ax1,ax2,var.T,vmin=vmin,vmax=vmax,shading='auto')
        plt.pcolormesh(-ax1,ax2,var.T,vmin=vmin,vmax=vmax,shading='auto')
        plt.tight_layout()
    plt.colorbar()
 



def get_max_step(local_wdir):
    """_summary_

    Args:
        local_wdir (_type_): _description_

    Returns:
        _type_: _description_
    """
    plutodir = os.environ['PLUTO_DIR']
    full_wdir = plutodir+local_wdir
    try:
        nlinf = pypl.nlast_info(w_dir=full_wdir,datatype='dbl')
    except:
        nlinf = pypl.nlast_info(w_dir=full_wdir,datatype='flt')
    max_step = nlinf['nlast']
    return max_step
