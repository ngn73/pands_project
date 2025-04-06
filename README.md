# Programming and Scripting Project 2025
This a file repository for the final project in module 4122 : programming and scripting for year 2025

> Author: Niall Naughton  
> Email : G00473476@atu.ie  
> Course : 4122 : programming and scripting  
> Lecturer : Andrew Beatty (andrew.beatty@atu.ie)  
> Date : March 2025  
***
# Project Description:  
## Exploring the Iris dataset  
   
![alt text](images\iris-machinelearning.png)
  
https://en.wikipedia.org/wiki/Iris_flower_data_set  
https://archive.ics.uci.edu/dataset/53/iris


The Iris dataset is earliest and the most famous dataset used in machine learning today for the purpose of classification.
The dataset was originally created by British mathematician Ronald Fisher in his 1936 paper : 
> The use of multiple measurements in taxonomic problems  
https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x

  

  The CSV file containing the datset can be downloaded from the UC Irvine Machine Learning Repository:
  https://archive.ics.uci.edu/dataset/53/iris  
  
  Alternatively, you can load this dataset directly within Python by importing the scikit-learn module  
https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html  

```
from sklearn import datasets  
iris = datasets.load_iris()
```

***
### The several stages of analysis for this dataset are organized into a series of jupyter notebooks: 

[**Stage 1** : First look at new dataset ](notebooks/exploring_the_iris_dataset_1.ipynb)   
Opening up dataset for first time. Reviewing the raw data, the different approaches for extracting this data, and managing the different Data types within returned objects  
[(Extra) : Code Exploring the various approaches to reading data in iris dataset ](code/iterable_collections.py)  

[**Stage 2** : Statistical Summary of data values ](notebooks/iris_statistical_summary.ipynb)   
Exploring a statistical summary of each of iris dataset's fields/features independently  
Sending results to a markdown formatted **jupyter notebook** for a structured/presentable format  
[Code generating statistical results for iris dataset and outputting to notepad ](code/iris_stats_summary.py)   
[Notebook for Statistical Analysis on Iris Dataset](notebooks/iris_summary.ipynb)   
[Notebook for Statistical Analysis on Daily Gold Rate (across currencies) Dataset](notebooks/gold_rates_summary.ipynb)   