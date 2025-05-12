'''
Author: Niall Naughton
Date: 27/04/2025

Description:
Display Scatter plots and polyfit linear regression lines for all 16 Iris feature combinations    

********************************************************************************************************
* Plotting tasks must be broken down into a series of manageable sub-tasks (functions)  
* Iterating thru Data must be carefully managed (splicing/filtering data and how data subsets are passed around to each script function)
* Plot a histogram at each grid position where feature pairs match
'''


#import usual required modules 
import pandas as pd
import numpy as np
from sklearn import datasets as ds
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


#Load comma separated file with error handling
def load_csv(str_filepath):
    try:
        data_df = pd.read_csv(str_filepath)
        data_df.head()
        #return dataframe
        return data_df
    except FileNotFoundError:
        print(f"The file path '{str_filepath}' does not exist.")
    except pd.errors.EmptyDataError:
        print(f"The file '{str_filepath}' is empty.")
    except pd.errors.ParserError:
        print(f"The file '{str_filepath}' data is not in a valid comma-separated-file format and cannot be read.")
    except PermissionError:
        print(f"Permission denied to Read '{str_filepath}'.")
    except Exception as ex:
        print(f"An unexpected error occurred while loading file {str_filepath} : {ex}")

def plotFeatureName(x:int):
    feature = df_iris.columns[x]
    gridoffset = x * 4
    ax_name = plt.subplot(gs[(gridoffset + 1):(gridoffset + 4), (gridoffset + 0):(gridoffset + 3)])
    ax_name.text(0.3, 0.5, feature)
    ax_name.set_xlabel('')
    ax_name.set_xticks([])
    ax_name.set_ylabel('')
    ax_name.set_yticks([])

def generateHisto(feature:int, ax, ispecies):
    f = df_iris.columns[feature]
    ax.hist(df_iris[df_iris['variety'] == ispecies][f], bins=20, color=colors[ispecies],edgecolor = 'white', alpha=0.6)
    
    # Remove ticks and labels from histograms... Messy!
    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False,
                        left=False, right=False, labelleft=False)
    ax.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False,
                        left=False, right=False, labelleft=False)

def generateScatter(feature1:int, feature2:int,ax, ispecies):
    f1 = df_iris.columns[feature1]
    f2 = df_iris.columns[feature2]
    coefficients = np.polyfit((df_iris[df_iris['variety'] == ispecies][f1]), (df_iris[df_iris['variety'] == ispecies][f2]), 1)
    polynomial = np.poly1d(coefficients)
    x_fit = np.linspace(min(df_iris[df_iris['variety'] == ispecies][f1]), max(df_iris[df_iris['variety'] == ispecies][f1]), 2)
    y_fit = polynomial(x_fit)

    ax.scatter(df_iris[df_iris['variety'] == ispecies][f1],  # Filter feature data by species(x-axis)
                    df_iris[df_iris['variety'] == ispecies][f2],  # Filter feature data by species(y-axis)
                    c=colors[ispecies],  # Color for the species
                    label=ispecies,  # Label for the species
                    alpha=0.7,  # Set transparency
                    marker = 'o',  # large marker
                    s=30)  # Size of the points
    
    # Plot the polynomial fit line
    ax.plot(x_fit, y_fit, color=colors[ispecies], label='Polynomial fit line')
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.legend() 

#Plot a scatter plot or a histo at position (xpos, ypos) in the 4x4 grid of plots
def generateGridPlotAtPos(xpos:int, ypos:int):
    #Get offset within the larger 4x4 grid
    x_gridoffset = xpos * 4
    y_gridoffset = ypos * 4
    ax = axes[xpos, ypos]

    if(xpos != ypos):
        #Add Scatterplot
        for ispecies in iris_species:
            generateScatter(xpos, ypos, ax, ispecies)
    else:
        # Add Histogram
        for ispecies in iris_species:
            generateHisto(xpos, ax, ispecies)




#load local cvs file located in .\resources\iris.data
df_iris = load_csv("../resources/iris.csv")

# Define the colors for the 3 species
colors = {'Setosa':'red', 'Versicolor':'green', 'Virginica':'blue'}  # Color for Setosa, Versicolor, and Virginica
iris_species = ('Setosa', 'Versicolor', 'Virginica') #unchangeable tuple

# Set up the grid layout 
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(30, 30))
fig.suptitle("Scatter plots and Histograms\n of sepal length and sepal length features\n\n\n", fontweight="bold")

#iterate thru 4x4 grid
for x in range(4):
    for y in range(4):
        generateGridPlotAtPos(x,y)
plt.tight_layout()
plt.show()
