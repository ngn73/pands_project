import io
import base64
import matplotlib.pyplot as plt
import pandas as pd
import app_logger as logger
import app_config as config
import nbformat as nbf

class plots: 
    def __init__(self, data_set_name:str, data_set:pd.DataFrame, useStats:bool=False, useHisto:bool=False, useBoxPlot:bool=False ):
        self.mylogger = logger.app_logger(__name__)
        self.myConfig = config.app_config()
        self.displayStats = useStats
        self.displayHisto = useHisto
        self.displayBoxplot = useBoxPlot
        self.dataset_name = data_set_name
        self.dataset = data_set



    #function to return a full range of statistics on a given feature_name
    # Explicitly declare a string and a dataframe as input and return a dictionary with the full set of the results 
    def getFeatureStatistics(self, feature_name:str):
        fname = feature_name
        fsize = self.dataset[feature_name].size
        #nanValues = self.dataset[feature_name].isnull()
        nanValues = 0
        mean = self.dataset[feature_name].mean()
        median = self.dataset[feature_name].median()
        std = self.dataset[feature_name].std()
        var = self.dataset[feature_name].var()
        min = self.dataset[feature_name].min()
        max = self.dataset[feature_name].max()
        skewness = self.dataset[feature_name].skew()
        kurt = self.dataset[feature_name].kurt()
        q1 = self.dataset[feature_name].quantile(0.25)
        q3 = self.dataset[feature_name].quantile(0.75)
        dict_stats = {
            "feature" : fname,
            "fsize" : fsize,
            "nan_values" : nanValues,
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

    #plot the Boxplot
    def plot_boxplot(self, feature_name:str):
        #add a boxplot for data series
        img_base64 = None
        self.mylogger.logInfoMessage(f"Staring Boxplot Plot of {feature_name}.")
        image_filename = f"images/plot.png"
        try:
            df_data = self.dataset[feature_name]
            fig, ax = plt.subplots(tight_layout = True, figsize=(10,10), facecolor='ivory') 
            fig.suptitle(f"Boxplot Distribution Analysis of {feature_name} attribute of {self.dataset_name} dataset", fontweight='bold')
            boxplot_settings = self.myConfig.getBoxplotSettings()

            ax.boxplot(df_data, vert=False, patch_artist=True, boxprops=dict(facecolor=boxplot_settings['facecolor'], color=boxplot_settings['color']),
                whiskerprops=dict(color=boxplot_settings['whisker_color']), flierprops=dict(markerfacecolor=boxplot_settings['flier_facecolor'], marker=boxplot_settings['flier_marker'], markersize=boxplot_settings['flier_markersize']),
                medianprops=dict(color=boxplot_settings['median_color']))
            ax.set_title(f'{feature_name} distribution')
            ax.set_xlabel('Value')
            ax.set_yticks([]) #remove the tick for boxplot (pointless)
            
            plt.tight_layout()
            plt.savefig(image_filename)
            plt.close()

            #Save boxplot image to a buffer instead of a file
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)     
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            self.mylogger.logInfoMessage(f"Completed Boxplot Plot of {feature_name} as returned as utf-8 buffer.")
        except FileNotFoundError:
            # This occurs if the file path is invalid or directory is not found 
            # ... but file will be created if initially it does not exist
            img_base64 = None
            self.mylogger.logErrorMessage(f"The file path '{file_name}' was not found.")
        except PermissionError:
            # This occurs if the user has no write permission on the file
            img_base64 = None
            self.mylogger.logErrorMessage(f"Permission denied to write to '{file_name}'.")
        except IOError as e:
            # This catches any other IO-related errors (e.g., disk full, etc.)
            img_base64 = None
            self.mylogger.logErrorMessage(f"IOError occurred: {e}")
        except Exception as e:
            # Catch any other unforeseen exceptions
            img_base64 = None
            self.mylogger.logErrorMessage(f"An unexpected error occurred: {e}")
        return img_base64
    
    #plot the histogram
    def plot_histo(self, feature_name:str):
        img_base64 = None
        self.mylogger.logInfoMessage(f"Staring Histo Plot of {feature_name}.")
        image_filename = f"images/plot.png"
        try:
            df_data = self.dataset[feature_name]
            fig, ax = plt.subplots(tight_layout = True, figsize=(10,10), facecolor='ivory') 
            fig.suptitle(f"Histogram Distribution Analysis of {feature_name} attribute of {self.dataset_name} dataset", fontweight='bold')
            histo_settings = self.myConfig.getHistoSettings()
            ax.hist(df_data, bins=21, color=histo_settings['color'], edgecolor=histo_settings['edgecolor'], alpha=histo_settings['alpha'], density=True)
            ax.set_xlabel(feature_name)
            ax.set_ylabel('Density / Frequency')
            ax.legend()

            plt.tight_layout()
            plt.savefig(image_filename)
            plt.close()

            #Save histo image to a buffer instead of a file
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)     
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            self.mylogger.logInfoMessage(f"Completed Histo Plot of {feature_name} as return as utf-8 buffer.")
        except FileNotFoundError:
            # This occurs if the file path is invalid or directory is not found 
            # ... but file will be created if initially it does not exist
            img_base64 = None
            self.mylogger.logErrorMessage(f"The file path '{file_name}' was not found.")
        except PermissionError:
            # This occurs if the user has no write permission on the file
            img_base64 = None
            self.mylogger.logErrorMessage(f"Permission denied to write to '{file_name}'.")
        except IOError as e:
            # This catches any other IO-related errors (e.g., disk full, etc.)
            img_base64 = None
            self.mylogger.logErrorMessage(f"IOError occurred: {e}")
        except Exception as e:
            # Catch any other unforeseen exceptions
            img_base64 = None
            self.mylogger.logErrorMessage(f"An unexpected error occurred: {e}")
        return img_base64


    def generateNotebook(self, file_name: str, feature_name:str):
        # Create a new notebook object
        self.mylogger.logInfoMessage(f"Staring Create a new notebook object.")
        nb = nbf.v4.new_notebook()
        # Create the first header cell
        text = f"# <font color='sky blue'>Analysis Summary of attribute {feature_name}</font>    \nThese are the analysis insights into feature selected on Application form.\n  DateFile : {file_name}\n  Attribute : {feature_name}  \n*Notebook autogenerated with python code*  \n"""
        header_cell = nbf.v4.new_markdown_cell(text)
        nb['cells'].append(header_cell)
        try:
            if(self.displayStats):
                self.mylogger.logInfoMessage(f"Creating Markdown Cell for of Statistical Summary.")
                feature_stats_dict = self.getFeatureStatistics(feature_name) #Extract stats
                stats_text = ''                    
                stats_text += f"**Feature : <font color='crimson'>{feature_stats_dict["feature"]}</font>**  \n"
                stats_text += f"Count : {feature_stats_dict["fsize"]}  \n"
                stats_text += f"NAN Count : {feature_stats_dict["nan_values"]}  \n"
                stats_text += f"Mean : {feature_stats_dict["mean"]:.3f}  \n"
                stats_text += f"Median : {feature_stats_dict["median"]:.3f}  \n"
                stats_text += f"Standard Deviation : {feature_stats_dict["std"]:.3f}  \n"
                stats_text += f"Variance : {feature_stats_dict["var"]:.3f}  \n"
                stats_text += f"Minimum : {feature_stats_dict["min"]:.3f}  \n"
                stats_text += f"Maximum : {feature_stats_dict["max"]:.3f}  \n"
                stats_text += f"Skewness : {feature_stats_dict["skewness"]:.3f}  \n"
                stats_text += f"Kurtosis  : {feature_stats_dict["kurt"]:.3f}  \n"
                stats_text += f"Interquartile Range  75th percentile(Q3) : {feature_stats_dict["q1"]:.3f}  \n"
                stats_text += f"Interquartile Range  25th percentile(Q1) : {feature_stats_dict["q3"]:.3f}  \n  \n"
                stats_cell = nbf.v4.new_markdown_cell(stats_text)
                nb['cells'].append(stats_cell)

            if(self.displayHisto):
                self.mylogger.logInfoMessage(f"Creating Markdown Cell for of Histogram Image.")
                img_buffer = self.plot_histo(feature_name)
                # 4. Create Markdown with embedded image
                markdown_img = f"![Plot](data:image/png;base64,{img_buffer})"
                histo_cell = nbf.v4.new_markdown_cell(markdown_img)
                nb['cells'].append(histo_cell)

            if(self.displayBoxplot):
                self.mylogger.logInfoMessage(f"Creating Markdown Cell for of Boxplot Image.")
                img_buffer = self.plot_boxplot(feature_name)
                # 4. Create Markdown with embedded image
                markdown_img = f"![Plot](data:image/png;base64,{img_buffer})"
                boxplot_cell = nbf.v4.new_markdown_cell(markdown_img)
                nb['cells'].append(boxplot_cell)
                
            # Open the notebook file in write mode. If the file doesn't exist, it will be created.
            with open(file_name, 'w') as f:
                nbf.write(nb, f)
            print(f"Analysis Results successfully written to notebook {file_name}")
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

