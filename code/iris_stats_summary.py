'''
Author: Niall Naughton
Date: 06/04/2025

Description:
load the Iris datatset and generate a notebook with a full summary
'''

import stats_util as su #
import pandas as pd

'''
#***********************************************************
#           Generate Statistics on Iris dataset
#***********************************************************
input_filepath = "../resources/iris.csv"
output_filepath = "../notebooks/iris_summary.ipynb"
iris_df = su.load_csv(input_filepath) #returns a dataframe
#drop the 'variety' column ... no need for stats on this
my_iris = iris_df.drop('variety', axis=1) 

#get a statistical results for all features and add to a list collection
iris_stats = []
for str_feature in my_iris.columns:
    arr_feature = iris_df[str_feature]
    iris_stats.append(su.getStatistics(str_feature, arr_feature))

#send list to function to generate a markdown formatted notepad
su.outputStatsToNotebook(output_filepath, iris_stats)
'''

#TODO: Try another dataset
#***********************************************************
#    Generate Statistics on Daily Gold Rates dataset
#
#   Testing this code against a large 9669x7 Dataset
#***********************************************************
input_filepath = "../resources/daily_gold_rate.csv"
output_filepath = "../notebooks/gold_rates_summary.ipynb"
gold_df = su.load_csv(input_filepath) #returns a dataframe
#drop the 'variety' column ... no need for stats on this
print(gold_df.shape)

my_gold = gold_df.drop('Date', axis=1) #remove the 'date' column

#get a statistical results for all features and add to a list collection
gold_stats = []
for str_feature in my_gold.columns:
    arr_feature = gold_df[str_feature]
    gold_stats.append(su.getStatistics(str_feature, arr_feature))

#send list to function to generate a markdown formatted notepad
su.outputStatsToNotebook(output_filepath, gold_stats)
