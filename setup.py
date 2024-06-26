# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:08:26 2024

@author: joedw
"""

#####################################################
### SETTING UP WORKING DIRECTORY AND CONFIG FILES ###
#####################################################
# Ensure you save the code to a desired file directory as all folders and outputs are created/outputed relative to this path.
# Save metadata to this working directory (wd). Follow the template csv (ensure the excel sheet is saved as a comma delimited file).


# Importing modules
import os
from configparser import RawConfigParser
import pandas as pd

# Some definitions
nld = RawConfigParser()
current_directory = os.getcwd()
wd = current_directory

# Setting up working directory
def initial(wd):
    
    ''' Creates files 
    
    Parameters:
    -----------
    
    wd : string
        current working directory
    
    '''
    try:
        os.mkdir(wd+"/config_files/")
    except:
        print("Folder already exists, skipping.")
        pass
    
    try:
        os.mkdir(wd+"/outputs/")
    except:
        print("Folder already exists, skipping.")
        pass
    
    try:
        os.mkdir(wd+"/outputs/figures/")
    except:
        print("Folder already exists, skipping.")
        pass

    try:
        os.mkdir(wd+"/outputs/data/")
    except:
        print("Folder already exists, skipping.")
        pass

# Creating config file
def create_config_file(wd):  
    
    ''' Creates config file which is a namelist of general and metadata (site) variables. 
        Searches for a metadata file in the current working directory saved as either metadata.csv or metadata.txt.
    
    Parameters:
    -----------
    
    wd : string
        current working directory
    
    '''
    
    config_directory = wd
    config_object = nld
    
    def write_config_file():
        
        ''' Writes config file.
            Combines user inputed metadata file with a list of general variables created in the function.
        
        '''
        nld['general'] = {
            "noval" : "-999",
            "jung_ref":"159",
            "defaultbd":"1.43",
            "cdtformat":"%d/%m/%Y",
            ";accuracy is for n0 calibration":"",
            "accuracy":"0.01",
            ";QA values are percentages (e.g. below 30% N0)":"",
            "belowN0":"30",
            "timestepdiff":"20",
            ";density=density of quartz":"",
            "density":"2.65",
            "smwindow":"12",
            "pv0":"0",
            "a0":"0.0808",
            "a1":"0.372",
            "a2":"0.115",
        }
        
        config_dict = md.set_index('variable').to_dict()['value']
        config_directory = wd+"/config_files/"
        nld['metadata'] = config_dict 
        
        config_file_path = os.path.join(config_directory, 'config.ini')
        
        raw_data_filepath = nld['metadata']['raw_data_filepath']    
        del nld['metadata']['raw_data_filepath']
        nld.add_section('filepaths')
        nld['filepaths']['raw_data_filepath'] = raw_data_filepath
        nld.set('filepaths', 'default_dir', wd)
        
        with open(config_file_path,'w') as conf:
            config_object.write(conf)
    
    md_file_path_csv = "metadata.csv"
    md_file_path_txt = "metadata.txt"
    
    if os.path.exists(md_file_path_csv):
        md = pd.read_csv(md_file_path_csv)  #reading csv
        md = pd.melt(md)    #switching columns to rows
        md = md.drop_duplicates()  #removing any duplicated rows/columns
        md_file_path_txt = "metadata.txt" #output path
        md.to_csv(md_file_path_txt, sep=' ', index=False)   #converts metadata file to a textfile 
        write_config_file()
        print("metadata.csv file detected. Writing config file...")
    
    elif os.path.exists(md_file_path_txt):
        md = pd.read_csv(md_file_path_txt, sep=' ')
        md.to_csv(md_file_path_txt, sep=' ', index=False)
        write_config_file()
        print("metadata.txt file detected. Writing config file...")
        
    else:
        print("Error: Please ensure metadata file is named 'metadata' and is saved as a '.csv' or '.txt' file in the current wd.")
        print("Also ensure file is correctly formatted as per the template.")

##########################
### CALLING FUNCTIONS  ###
##########################

initial(wd)
create_config_file(wd)

'''
     Please note some general definitions may need adjusting in the config file:
     
         jung_ref : currently set at 159 for Junfraujoch station. 
         
'''       










