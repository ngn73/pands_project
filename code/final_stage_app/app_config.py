import configparser
class app_config:
    def __init__(self):
        try:
            self.config_file = 'app_settings.ini'     #Hardcoded ... should not change!
            # Create a ConfigParser object
            self.config = configparser.ConfigParser()
            # Read the configuration file
            self.config.read(self.config_file)
        except FileNotFoundError as e:
            print(f"Error: Cannot find config file {self.config_file} :{e}")
        except configparser.ParsingError as e:
            print(f"Config file {self.config_file} is badly formatted: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during loading config file {self.config_file}:", e)

    def getLoggingSettings(self):
        # Logging values from the configuration file
        try:
            logging_active = self.config.getboolean('Logging', 'log_active')
            logging_filename = self.config.get('Logging', 'log_filename')
            logging_level = self.config.get('Logging', 'log_level')
            logging_settings = {
                'active': logging_active,
                'filename': logging_filename,
                'level': logging_level
                }
            return logging_settings
        except configparser.NoSectionError as e:
            print(f"Missing section in config: {e}")
        except configparser.NoOptionError as e:
            print(f"Missing option in config: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during loading config Logging section in file: {self.config_file}: {e}")

    def getCSVSettings(self):
        #Settings for loading CSV files
            csv_filelocation = self.config.get('CSV', 'csv_filelocation')
            cvs_settings = {
                'filelocation': csv_filelocation,
                }
            return cvs_settings

    def getHistoSettings(self):
        #Settings for plotting Histogram
        histo_bins = int(self.config.get('Histogram', 'bins'))
        histo_color = self.config.get('Histogram', 'color')
        histo_edgecolor = self.config.get('Histogram', 'edgecolor')
        histo_alpha = float(self.config.get('Histogram', 'alpha'))
        
        histo_settings = {
            'bins': histo_bins,
            'color': histo_color,
            'edgecolor': histo_edgecolor,
            'alpha': histo_alpha
            }
        return histo_settings
    
    def getBoxplotSettings(self):
        #Settings for plotting Boxplot
        boxplot_facecolor = self.config.get('Boxplot', 'facecolor')
        boxplot_color = self.config.get('Boxplot', 'color')
        boxplot_whisker_color = self.config.get('Boxplot', 'whisker_color')
        boxplot_flier_facecolor = self.config.get('Boxplot', 'flier_facecolor')
        boxplot_flier_marker = self.config.get('Boxplot', 'flier_marker')
        boxplot_flier_markersize = int(self.config.get('Boxplot', 'flier_markersize'))
        boxplot_median_color = self.config.get('Boxplot', 'median_color')
        
        boxplot_settings = {
            'facecolor': boxplot_facecolor,
            'color' :  boxplot_color,
            'whisker_color' : boxplot_whisker_color,
            'flier_facecolor' :  boxplot_flier_facecolor,
            'flier_marker' :  boxplot_flier_marker,
            'flier_markersize' : boxplot_flier_markersize,
            'median_color' : boxplot_median_color
            }
        return boxplot_settings        
    
    def getFormSettings(self):
        #Settings for Form Text
        form_header = self.config.get('General', 'form_header').replace("\\n", "\n")
        form_footer = self.config.get('General', 'form_footer').replace("\\n", "\n")

        form_settings = {
            'form_header': form_header,
            'form_footer': form_footer,
            }
        return form_settings

    def getNotebookSettings(self):
        #Settings for Notebooks
        ipynb_filename = self.config.get('Notebook', 'notebook_filename')
        ipynb_folder = self.config.get('Notebook', 'notebook_folder')

        ipynb_settings = {
            'filename': ipynb_filename,
            'folder': ipynb_folder,
            }
        return ipynb_settings

    def getAllSettings(self):
        # Return a dictionary of dictionaries (with the retrieved values)
        logging_settings = self.getLoggingSettings()
        mysql_settings = self.getLoggingSettings()
        neo4j_settings = self.getNeo4JSettings()
        config_settings = {'logging':logging_settings, 'mySql':mysql_settings, 'neo4j':neo4j_settings}
        return config_settings
    


