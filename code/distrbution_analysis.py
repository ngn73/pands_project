'''
Author: Niall Naughton
Date: 13/04/2025

Description:
A program that generates visual plots of
* Histograms
* Boxplots
... for all iris features and all species

a full record of my exploration of matplotlib and my approach to this task is recorded in notebooks : 
* visualizing_distributions.ipynb
* exploring_matplotlib_layouts.ipynb
'''

#import required modules 
import pandas as pd
import numpy as np
from sklearn import datasets as ds
import matplotlib.pyplot as plt

import stats_util as st #module from stage 3

#build a block of text with statistical info
def get_stats_summary(feature_name:str,species_feature_data:np.ndarray):
    my_stats = st.getFeatureStatistics(feature_name, species_feature_data)
    feature_stats = f"Size : {my_stats["fsize"]}  \n"
    feature_stats += f"Mean : {my_stats["mean"]:.3f}  \n"
    feature_stats += f"Median : {my_stats["median"]:.3f}  \n"
    feature_stats += f"Standard Deviation : {my_stats["std"]:.3f}  \n"
    feature_stats += f"Variance : {my_stats["var"]:.3f}  \n"
    feature_stats += f"Minimum : {my_stats["min"]:.3f}  \n"
    feature_stats += f"Maximum : {my_stats["max"]:.3f}  \n"
    feature_stats += f"Skewness : {my_stats["skewness"]:.3f}  \n"
    feature_stats += f"Kurtosis  : {my_stats["kurt"]:.3f}  \n"
    return feature_stats

#plot the Boxplots
def plot_boxplot(feature_name:str, df_data:pd.Series, ax):
    #add a boxplot for data series
    ax.boxplot(df_data, vert=False, patch_artist=True, boxprops=dict(facecolor='orange', color='blue'),
        whiskerprops=dict(color='blue'), flierprops=dict(markerfacecolor='red', marker='o', markersize=6),
        medianprops=dict(color='green'))
    ax.set_title(f'{feature_name} distribution')
    ax.set_xlabel('Value')
    ax.set_yticks([]) #remove the tick for boxplot (pointless)
    #no need for legend

#plot the histogram
def plot_histo(feature_name:str, df_data:pd.Series, ax):
    ax.hist(species_feature_data, bins=21, color='skyblue', edgecolor='black', alpha=0.6, density=True)
    ax.set_ylabel('Density / Frequency')

#plot the text block
def plot_text(feature_name:str, df_data:pd.Series, ax):
    txt_summary = get_stats_summary(feature_name, df_data)
    ax.text(0.02, 0.98, txt_summary, transform = ax.transAxes, fontsize=8, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))  


#load local cvs file located in ./resources/iris.csv
iris = st.load_csv("../resources/iris.csv") #use my custom load_CSV() with error handling
iris_species = ['Setosa','Versicolor','Virginica']
for ispecies in iris_species:
    #plot a grid of 2 x 2 plots in a 1000 x 1000 canvas (figure) for each species
    fig, ax = plt.subplots(2,2, tight_layout = True, figsize=(10,10), facecolor='ivory') 
    #add a super title main figure
    fig.suptitle(f"Distribution Analysis of each Iris Feature in {ispecies} species", fontweight='bold')
    #iterate thru feature data and plot each series
    feature_names = iris.columns
    for i in range(2):
        for j in range(2):
            #get required data
            idx = j+(i*2)
            feature_name = feature_names[idx]
            species_feature_data = iris[iris['variety'] == ispecies][feature_name]
            
            #plot data
            plot_boxplot(feature_name, species_feature_data,ax[i,j] )
            plot_histo(feature_name, species_feature_data, ax[i,j].twinx() )
            plot_text(feature_name, species_feature_data, ax[i,j] )
            
    plt.tight_layout()
plt.show()