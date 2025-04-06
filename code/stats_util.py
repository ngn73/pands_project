'''
Author: Niall Naughton
Date: 06/04/2025

Description:
A program with several utility functions for 
* reading csv file into a dataframe
* generating statistical data (from a array of data)
* outputting to a jupyter notepad

Called by another python program that load the Iris datatset
(This utility should independent of dataset be able to process most dataframe-based datasets) 
'''

import numpy as np
import pandas as pd
import scipy.stats as ss
import nbformat as nbf

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

#function to return a full range of statistics on a given feature_name
# Explicitly declare a string and a numpy.ndarray as input and return a dictionary with the full set of the results 
def getStatistics(feature_name:str, feature_arr: np.ndarray):
    fname = feature_name
    mean = np.mean(feature_arr)
    median = np.median(feature_arr)
    std = np.std(feature_arr)
    var = np.var(feature_arr)
    min = np.min(feature_arr)
    max = np.max(feature_arr)
    skewness = ss.skew(feature_arr)
    kurt = ss.kurtosis(feature_arr)
    q1 = np.percentile(feature_arr, 25)
    q3 = np.percentile(feature_arr, 75)
    dict_stats = {
        "feature" : fname,
        "mean" : mean,
        "median" : median,
        "std" : std,
        "var" : var,
        "min" : min,
        "max" : max,
        "skewness" : skewness,
        "kurt" : kurt,
        "q1" : q1,
        "q3" : q3
    }

    return dict_stats


def outputStatsToNotebook(file_name: str, arr_stats:list):
    # Create a new notebook object
    nb = nbf.v4.new_notebook()
    # Create the first header cell
    text = "# <font color='sky blue'>Statistical Summary of dataset</font>    \nThese are the statistical insights into each feature of dataset."""
    header_cell = nbf.v4.new_markdown_cell(text)
    nb['cells'].append(header_cell)

    try:
        with open(file_name, 'w') as f:
            # Open the file in write mode. If the file doesn't exist, it will be created.
            feature_text = ''
            for feature_stats_dict in arr_stats:
                
                feature_text += f"**Feature : <font color='crimson'>{feature_stats_dict["feature"]}</font>**   \n"
                feature_text += f"Mean : {feature_stats_dict["mean"]:.3f}  \n"
                feature_text += f"Median : {feature_stats_dict["median"]:.3f}  \n"
                feature_text += f"Standard Deviation : {feature_stats_dict["std"]:.3f}  \n"
                feature_text += f"Variance : {feature_stats_dict["var"]:.3f}  \n"
                feature_text += f"Minimum : {feature_stats_dict["min"]:.3f}  \n"
                feature_text += f"Maximum : {feature_stats_dict["max"]:.3f}  \n"
                feature_text += f"Skewness : {feature_stats_dict["skewness"]:.3f}  \n"
                feature_text += f"Kurtosis  : {feature_stats_dict["kurt"]:.3f}  \n"
                feature_text += f"Interquartile Range  75th percentile(Q3) : {feature_stats_dict["q1"]:.3f}  \n"
                feature_text += f"Interquartile Range  25th percentile(Q1) : {feature_stats_dict["q3"]:.3f}  \n  \n"
            feature_cell = nbf.v4.new_markdown_cell(feature_text)
            nb['cells'].append(feature_cell)
            nbf.write(nb, f)
        print(f"Statistical Results successfully written to notebook {file_name}")
    except FileNotFoundError:
        # This occurs if the file path is invalid or directory is not found 
        # ... but file will be created if initially it does not exist
        print(f"The file path '{file_name}' was not found.")
    except PermissionError:
        # This occurs if the user has no write permission on the file
        print(f"Permission denied to write to '{file_name}'.")
    except IOError as e:
        # This catches any other IO-related errors (e.g., disk full, etc.)
        print(f"IOError occurred: {e}")
    except Exception as e:
        # Catch any other unforeseen exceptions
        print(f"An unexpected error occurred: {e}")
