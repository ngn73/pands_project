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
   
![alt text](iris-machinelearning.png)
  
https://en.wikipedia.org/wiki/Iris_flower_data_set  
https://archive.ics.uci.edu/dataset/53/iris


The Iris dataset is earliest and the most famous dataset used in machine learning today for the purpose of classification.
The dataset was originally created by British mathematician Ronald Fisher in his 1936 paper : 
> The use of multiple measurements in taxonomic problems  
https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x

  In order to get underway the analysis on this dataset and start this project, it is assumed that I have no prior knowledge of this dataset (_While I have encountered this dataset in other coursework modules this semester_).

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

[Stage 1 : Opening new dataset ](exploring_the_iris_dataset_1.ipynb)