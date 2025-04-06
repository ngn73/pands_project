'''
Author: Niall Naughton
Date: 05/04/2025

Description:
Just experimenting with the use of the various collections or iterable datatypes to read the Iris dataset
* numpy arrays
* sklearn Bunches
* seaborn
* dataFrames
* dictionaries
* lists

** 
This does not further analyse the Iris dataset ... 
it is simply an exploration in how to use python and its extended modules to access this Iris dataset
**
'''

#load required modules
import pandas as pd
import numpy as np
import seaborn as sb
from sklearn import datasets as ds  


#use pandas dataframe read_csv()
iris_df = pd.read_csv("resources/iris.csv") #type :' <class 'pandas.core.frame.DataFrame'>
print(iris_df.head()) #view top 5 records
print(iris_df["sepal.width"]) #view all values from second column by name 'sepal.width'
print(iris_df["sepal.width"][2]) #view 3rd value from second column by name 'sepal.width'
print(iris_df.iloc[:, 1])   #view all values from second column by (zero-based) column index 1
print(iris_df.iloc[:, 1][2])    #view 3rd value from second column by (zero-based) column index 1
# ERROR : print(iris_df[3])    #try to view 4th row of iris dataset (need to use the iloc() !)
print(iris_df.iloc[3])    #view 4th row of iris dataset 
print(iris_df.iloc[3, 1])    #use iloc() to view value of (zero-based) column#1 from 4th row of iris dataset 
print(iris_df.loc[3, "sepal.width"])    #use loc() to view value of "sepal.width" from 4th row of iris dataset 



#use seaborn (uses dataframe exactly like above, but feature names a little different)
iris_sb = sb.load_dataset('iris')   # type : <class 'pandas.core.frame.DataFrame'>
print(iris_sb.head()) #view top 5 records
print(iris_sb["sepal_width"]) #view all values from second column by name 'sepal.width'
print(iris_sb["sepal_width"][2]) #view 3rd value from second column by name 'sepal.width'
print(iris_sb.iloc[:, 1])   #view all values from second column by (zero-based) column index 1
print(iris_sb.iloc[:, 1][2])    #view 3rd value from second column by (zero-based) column index 1
# ERROR : print(iris_sb[3])    #try to view 4th row of iris dataset (need to use the iloc() !)
print(iris_sb.iloc[3])    #view 4th row of iris dataset 
print(iris_sb.iloc[3, 1])    #use iloc() to view value of (zero-based) column#1 from 4th row of iris dataset 
print(iris_sb.loc[3, "sepal_width"])    #use loc() to view value of "sepal.width" from 4th row of iris dataset 


#use skelearn Bunch (need to utilize 'data' attribute of Bunch)
iris_sk = ds.load_iris()    # type : <class 'sklearn.utils.Bunch'>`
iris_sk_data = iris_sk.data # type : <class 'numpy.ndarray'>
print(iris_sk_data[:5]) #view top 5 records
#ERROR : print(iris_sk_data["sepal_width"]) #try to view all values from column by name 'sepal width (cm)' (ERROR: Numpy array does not have column names)
idx = iris_sk.feature_names.index('sepal width (cm)')   #get index of feature name
print(iris_sk_data[idx][2]) #view 3rd value from second column by name 'sepal.width'
print(iris_sk_data[:, 1])   #view all values from second column by (zero-based) column index 1
print(iris_sk_data[:, 1][2])    #view 3rd value from second column by (zero-based) column index 1
print(iris_sk_data[3])  #view 4th row of iris dataset


#To use numpy array need to convert from Dataframe
iris_arr = iris_df.to_numpy()   #type : <class 'numpy.ndarray'>
print(iris_arr) #view top 5 records
#ERROR : print(iris_arr["sepal_width"]) #try to view all values from column by name 'sepal width (cm)' (ERROR: Numpy array does not have column names)
print(iris_arr[:, 1])   #view all values from second column by (zero-based) column index 1
print(iris_arr[:, 1][2])    #view 3rd value from second column by (zero-based) column index 1
print(iris_arr[3])  #view 4th row of iris dataset'

#Convert iris to a Dictionary (from the advanced sklearn bunch object)
iris_dict = dict(iris_sk)   #Convert sklearn.bunch to a Dictionary of Lists
print(iris_dict["feature_names"])  #print list of the feature_names 

#Convert iris to different types of Dictionary (from the dataframe object)
print(iris_df.to_dict('list'))    #dictionary where each column is a key, and value is a list
print(iris_df.to_dict('records'))   #list where each value is a dictionary of key/values
print(iris_df.to_dict('index')) #dictionary where rows are indexed by index values


## INTERESTING !! :)
