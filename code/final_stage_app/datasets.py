'''
Author: Niall Naughton
07/05/2025
------------------------------------------------------------------
Description:
Utility Class "datasets" for loading/processing comma separated value data
------------------------------------------------------------------
'''
import os       #needed for path processing
import pandas as pd
import app_logger as logger
import app_config as config

class datasets:
    
    def __init__(self):
        self.mylogger = logger.app_logger(__name__)
        self.myConfig = config.app_config()
        self.data_df = None

    #Load comma separated file with error handling
    def load_csv(self, filename) -> pd.DataFrame:
        try:
            csv_settings = self.myConfig.getCSVSettings()
            filelocation = csv_settings["filelocation"]
            csv_filepath = filelocation + filename
            self.data_df = pd.read_csv(csv_filepath)
        except FileNotFoundError:
            self.mylogger.logErrorMessage(f"The file path '{filename}' does not exist.")
            self.data_df = None
        except pd.errors.EmptyDataError:
            self.mylogger.logErrorMessage(f"The file '{filename}' is empty.")
            self.data_df = None
        except pd.errors.ParserError:
            self.mylogger.logErrorMessage(f"The file '{filename}' data is not in a valid comma-separated-file format and cannot be read.")
            self.data_df = None
        except PermissionError:
            self.mylogger.logErrorMessage(f"Permission denied to Read '{filename}'.")
            self.data_df = None
        except Exception as ex:
            self.mylogger.logErrorMessage(f"An unexpected error occurred while loading file {filename} : {ex}")
            self.data_df = None
        finally:
            return self.data_df

    #List All .png Files in a Folder
    def getCSVFileNames(self) -> list:
        self.csvFiles = []
        # Set the folder path and desired extension
        csv_settings = self.myConfig.getCSVSettings()
        folder_path = csv_settings["filelocation"]
        extension = ".csv"  # Change this to whatever you need
        # List all csv files
        self.csvFiles = [f for f in os.listdir(folder_path) if f.endswith(extension)]
        return self.csvFiles