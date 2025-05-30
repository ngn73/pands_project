
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# Need for global varibale
#Need for lamda


from pathlib import Path
import app_logger as logger
import app_config as config
import tkinter as tk
from tkinter import ttk 
import random
import os

import datasets as ds
import plots as pt

#Logger to use
mylogger = logger.app_logger(__name__)
DEFAULT_SELECTION = "Select Dataset"

class dataForm:     #Define form as a Class, so you can control access to various form elements (using self) ... Better!

    def __init__(self, window):
        self.ds_files = ds.datasets()
        self.window = window
        self.defineForm()
        self.feedback_id = None
        self.csv_data_file = None   #The selected dataframe for data file to use
        self.csv_data_filename = None   #The selected name of data file to use
        self.data_attribute = None  #The selected name of data attribute to use

    def defineForm(self):
        #Main Window Canvas
        self.main_canvas = tk.Canvas(
            self.window,
            bg = "#BBDAF2",
            height = 400,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.defineLeftPanel()
        self.defineTopRightPanel()
        self.defineLowerRightPanel()
        self.defineGenerateButton()

    def defineLeftPanel(self):
        #Left-hand panel/canvas
        self.main_canvas.place(x = 0, y = 0)
        self.main_canvas.create_rectangle(
            24.0,
            20.0,
            224.0,
            380.0,
            fill="#3D95CC",
            outline="")

        #Add Data Analytics image
        global image_image_1  # Need global ... Once the function finishes executing, Python deletes the image :(
        image_image_1 = tk.PhotoImage(file="images/course_image.png")
        image_1 = self.main_canvas.create_image(
            123.0,
            92.0,
            image=image_image_1
        )
        form_cfg = config.app_config()
        form_config = form_cfg.getFormSettings()
        #Add Text #1
        self.main_canvas.create_text(
            42.0,
            177.0,
            anchor="nw",
            text=form_config['form_header'],
            fill="#FFFFFF",
            font=("Inter ExtraBold", 24 * -1)
        )

        #Add Text #2
        self.main_canvas.create_text(
            36.0,
            300.0,
            anchor="nw",
            text=form_config['form_footer'],
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

    def defineTopRightPanel(self):
        #Small White Panel/Canvas
        top_canvas = tk.Canvas(self.window, width=333, height=48, bg="white", highlightthickness=0)
        self.main_canvas.create_window(246, 20, window=top_canvas, anchor="nw")

        # Create a dropdown (Combobox)
        self.combo = ttk.Combobox(self.window, values=self.getDataFiles(), width=35) #populate with all available csv filenames
        self.combo.set(DEFAULT_SELECTION)
        top_canvas.create_window(10,20, window=self.combo, anchor="w")  

        # Create a 'Load Data' button
        button = tk.Button(self.window, text="Load Data", command=lambda: self.onDatasetSelect(self.combo))  #note command : lamda call "onDatasetSelect"
        top_canvas.create_window(320, 20, window=button, anchor="e")  

    def defineLowerRightPanel(self):
        #Large White Panel/Canvas
        bottom_canvas = tk.Canvas(self.window, width=333, height=240, bg="white", highlightthickness=0)
        self.main_canvas.create_window(246, 86, window=bottom_canvas, anchor="nw")

        #Create a ListBox
        # Create a frame to hold the Listbox and a scrollbar
        list_frame = tk.Frame(self.window)
        self.lb_attr = tk.Listbox(list_frame, width=20, height=13)
        # Bind selection event
        self.lb_attr.bind("<<ListboxSelect>>", self.on_lb_select)

        self.populateListbox()
        self.lb_attr.pack(side="left", fill="y")
        bottom_canvas.create_window(150, 120, window=list_frame, anchor="e")

        # Add a scrollbar
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.lb_attr.yview)
        scrollbar.pack(side="right", fill="y")
        self.lb_attr.config(yscrollcommand=scrollbar.set)
        
        #add a feedback label
        self.CV_feedback = tk.Canvas(self.window, width=160, height=60, bg="white")
        bottom_canvas.create_window(160,45, window=self.CV_feedback, anchor="w") 

        #add a group of checkboxes to a canvas 
        self.CV_analyis_type = tk.Canvas(self.window, width=160, height=135, bg="white")
        bottom_canvas.create_window(160,155, window=self.CV_analyis_type, anchor="w") 
        self.check_stats = tk.BooleanVar()
        self.check_histo = tk.BooleanVar()
        self.check_boxplot = tk.BooleanVar()
        cb_analyis_stats = tk.Checkbutton(self.window, text="Statistics", variable=self.check_stats, bg="white")
        cb_analyis_histo = tk.Checkbutton(self.window, text="Histogram", variable=self.check_histo, bg="white")
        cb_analyis_boxplot = tk.Checkbutton(self.window, text="Boxplot", variable=self.check_boxplot, bg="white")

        bottom_canvas.create_window(200, 120, window=cb_analyis_stats, anchor="nw")
        bottom_canvas.create_window(200, 150, window=cb_analyis_histo, anchor="nw")
        bottom_canvas.create_window(200, 180, window=cb_analyis_boxplot, anchor="nw")


    def defineGenerateButton(self):
        #Add 'Generate' Button
        #self.button_image_1   #Need global ... Once the function finishes executing, Python deletes the image :(
        self.button_image_1 = tk.PhotoImage(file="images/generate_button.png")
        generate_button = tk.Button(
            image=self.button_image_1,
            text="Generate",
            compound="center",  # Center the text over the image
            font=("Inter", 16, "bold"),
            fg="white",         # Text color
            borderwidth=0,
            highlightthickness=0,
            command=self.generate_button_click,
            relief="raised"
        )
        generate_button.place(
            x=246.0,
            y=340.0,
            width=333.0,
            height=35.0
        )

    def generate_button_click(self):
        if((self.csv_data_filename is not None) and (self.csv_data_file is not None) and (self.data_attribute is not None)):
            print(f"Attribute {self.data_attribute} of dataset {self.csv_data_filename} selected")
            mylogger.logInfoMessage(f"Generating Histo for: {self.data_attribute} attribute")
            myplot = pt.plots(self.csv_data_filename, self.csv_data_file, useStats=self.check_stats.get(), useHisto=self.check_histo.get(), useBoxPlot=self.check_boxplot.get())
            myplot.generateNotebook(self.getNotebookFileName(), self.data_attribute)

    #generate filename and full path of jupyter notebook
    def getNotebookFileName(self):
        myconfig = config.app_config()
        ipynb_settings = myconfig.getNotebookSettings()
        ipynb_folder = ipynb_settings['folder']
        ipynb_filename = ipynb_settings['filename']
        ipynb_filename = ipynb_filename.replace('[id]', f"{random.randint(1, 999999) : 06d}")

        return os.path.join(ipynb_folder, ipynb_filename)

    #ListBox Item selected
    def on_lb_select(self, event):
        widget = event.widget
    
        selection = widget.curselection()
        
        #clear feedback canvas Text
        if(self.feedback_id):
            self.CV_feedback.delete(self.feedback_id)
            #self.lb_attr.delete(0, tk.END)  #Clear List
            self.data_attribute = None

        #Add feedback canvas Text
        if (len(selection) > 0):
            self.data_attribute = widget.get(selection[0])
            self.feedback_id = self.CV_feedback.create_text(
                5, 0,  # x, y coordinates
                anchor="nw",
                text = f"You selected attribute:\n{self.data_attribute}\nfrom the source datafile:\n{self.csv_data_filename}",
                font=("Arial", 8),
                fill="blue"
            )


    def populateListbox(self):
        csv_file = self.combo.get()
        self.lb_attr.delete(0, tk.END)  #Clear List
        if(csv_file == DEFAULT_SELECTION):
            self.lb_attr.config(state="disabled")
        else:
            #Populate list with attributes of selected dataset
            self.csv_data_file = self.ds_files.load_csv(csv_file)
            df_attr = self.csv_data_file.columns.tolist()
            self.lb_attr.config(state="normal")
            for item in df_attr:
                if(not item == 'rownames'):     #remove this default column
                    self.lb_attr.insert(tk.END, item)

    def getDataFiles(self):
        csv_list = self.ds_files.getCSVFileNames()
        #TODO: Error handle!
        return csv_list

    def onDatasetSelect(self, cb: ttk.Combobox):
        self.populateListbox()
        self.csv_data_filename = cb.get()
        if(not self.csv_data_filename == DEFAULT_SELECTION):
            mylogger.logInfoMessage(f"Loaded Dataset file {self.csv_data_filename}")



#Main Application Function
def main():

    #Load "Data" form
    mylogger.logInfoMessage("Starting GUI App")
    winform = tk.Tk()
    winform.title("Data Analysis GUI")
    winform.geometry("600x400")
    winform.configure(bg = "#BBDAF2")
    winform.resizable(False, False)
    app = dataForm(winform)
    winform.mainloop()


#Run code if called directly
if __name__ == "__main__":
    main()