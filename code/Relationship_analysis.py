'''
Author: Niall Naughton
Date: 19/04/2025

Description:
Display both Scatter plots and Histograms for all 16 Iris feature combinations    

********************************************************************************************************
While this final plot of this script may get quite cluttered ... 
this is really a coding task in managing a large matrix of data and generating required visualizations 
********************************************************************************************************
* Plotting tasks must be broken down into a series of manageable sub-tasks (functions)  
* Iterating thru Data must be carefully managed (splicing/filtering data and how data subsets are passed around to each script function)
* Manage full grid of 4x4 plots that are each a 4x4 grid layout (i.e. managing a 16x16 grid matrix)

'''


#import usual required modules 
import pandas as pd
import numpy as np
from sklearn import datasets as ds
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import stats_util as su


def plotFeatureName(x:int):
    feature = df_iris.columns[x]
    gridoffset = x * 4
    ax_name = plt.subplot(gs[(gridoffset + 1):(gridoffset + 4), (gridoffset + 0):(gridoffset + 3)])
    ax_name.text(0.3, 0.5, feature)
    ax_name.set_xlabel('')
    ax_name.set_xticks([])
    ax_name.set_ylabel('')
    ax_name.set_yticks([])

def generateHisto(feature1:int, feature2:int, ax_x, ax_y, ispecies):
    f1 = df_iris.columns[feature1]
    f2 = df_iris.columns[feature2]
    ax_x.hist(df_iris[df_iris['variety'] == ispecies][f1], bins=20, color=colors[ispecies],edgecolor = 'white', alpha=0.6)
    ax_y.hist(df_iris[df_iris['variety'] == ispecies][f2], bins=20, orientation='horizontal', color=colors[ispecies],edgecolor = 'white', alpha=0.6)
    
    # Remove ticks and labels from histograms... Messy!
    ax_x.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False,
                        left=False, right=False, labelleft=False)
    ax_y.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False,
                        left=False, right=False, labelleft=False)

def generateScatter(feature1:int, feature2:int,ax, ispecies):
    f1 = df_iris.columns[feature1]
    f2 = df_iris.columns[feature2]
    ax.scatter(df_iris[df_iris['variety'] == ispecies][f1],  # Filter feature data by species(x-axis)
                    df_iris[df_iris['variety'] == ispecies][f2],  # Filter feature data by species(y-axis)
                    c=colors[ispecies],  # Color for the species
                    label=ispecies,  # Label for the species
                    alpha=0.7,  # Set transparency
                    marker = '.',  # large marker
                    s=30)  # Size of the points
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    #ax.legend() #Removed ... too much clutter

#Plot a scatter plot and histo at position (xpos, ypos) in the 4x4 grid of plots
def generateGridPlotAtPos(xpos:int, ypos:int):
    #Get offset within the larger 4x4 grid
    x_gridoffset = xpos * 4
    y_gridoffset = ypos * 4
    #Setup Axes that will span across the internal 4x4 grid
    ax_scatter = plt.subplot(gs[(x_gridoffset + 1):(x_gridoffset + 4), (y_gridoffset + 0):(y_gridoffset + 3)])  # Plot spans x grid 1-4 and y grid 0-3 for a 3x3 spanned plot
    ax_xhist = plt.subplot(gs[(x_gridoffset + 0), (y_gridoffset + 0):(y_gridoffset + 3)], sharex=ax_scatter)  # Histogram spans Columns 0-3 at row #0
    ax_yhist = plt.subplot(gs[(x_gridoffset + 1):(x_gridoffset + 4), (y_gridoffset + 3)], sharey=ax_scatter)  # Histogram spans Rows 1-4 at Column #3

    for ispecies in iris_species:
        #Add Scatterplot
        generateScatter(xpos, ypos, ax_scatter, ispecies)

        # Histograms
        generateHisto(xpos, ypos, ax_xhist, ax_yhist, ispecies)

#load local cvs file located in .\resources\iris.data
df_iris = su.load_csv("../resources/iris.csv")

# Define the colors for the species
colors = {'Setosa':'red', 'Versicolor':'green', 'Virginica':'blue'}  # Color for Setosa, Versicolor, and Virginica
iris_species = ('Setosa', 'Versicolor', 'Virginica') #unchangeable tuple

# Set up the grid layout 
fig = plt.figure(figsize=(30, 60), facecolor = 'ivory')
fig.suptitle("Scatter plots and Histograms\n of sepal length and sepal length features\n\n\n", fontweight="bold")
gs = gridspec.GridSpec(16, 16)
for x in range(4):
    for y in range(4):
        if x == y:
            plotFeatureName(x)
        else:
            generateGridPlotAtPos(x,y)
plt.tight_layout()

plt.show()
