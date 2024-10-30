# Project template creation

import os
from pathlib import Path # this is used to fix the forward  slash issue on Windows

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# Using logging helps people who make programs understand what’s happening inside their program. If something goes wrong, they can look at their notes (logs) to see what happened and when!
# So, in short, this line sets up a special notebook for your program to keep track of important events with timestamps!

project_name = "textSummarizer"

# mentioning files and folders that will be created
list_of_files = [
    ".github/workflows/.gitkeep",  # this will be used for ci/cd deployment, CI/CD using yml file (as soon as you do the commit it will take the code from github and take it to cloud deployment )
    # creating a .gitkeep (hidden file) , so that empty folder won't be uploaded on github (we must have some filed in the folder), :ater we will delete it when we create our yml file.
    f"src/{project_name}/__init__.py",   # creating project  folder and creating a constructor file
    # constructor file - cuz  we are creating a local python package , we will use it to import something from other folders (from textSummarizer import *)
    # to do this kind of import operations you need to install this folder as local packag.
    # so when ever you will be doing installation of your local package it will look for this constructor file. Whenever this constructor file is present , that folder will be considered as my local package. (init file is important)
     
    f"src/{project_name}/components/__init__.py", # one more constructor file in  components folder, means components will be another one of our local package 

    
    f"src/{project_name}/utils/__init__.py",  # making  another constructor file in utils folder, means utils will be another one of our local package 
    f"src/{project_name}/utils/common.py",  # will write all my utilities here
    
    
    f"src/{project_name}/logging/__init__.py",
    
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",  
    
    # these all files will be created automatically in once
    "config/config.yaml",  
    "params.yaml", #  this will be used for hyperparameter tuning

    "app.py",  #  main file of the project

    "main.py",  #  this will be the entry point of our project

    "Dockerfile",  #  this file is used to create a docker image

    "requirements.txt", #  this file will be used to install all the packages that we are using in our project

    "setup.py",         #  this file is used to install the package
    "research/trails.ipynb" #  this is used for data analysis and data exploration

]


# Now creating logic to execute

for filepath in list_of_files: 
    filepath = Path(filepath)  # based on operating system Path will provide the path
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":  #  if filedir is not empty then create the directory

        os.makedirs(filedir,exist_ok=True) #  exist_ok=True means if the directory is already present then it will not give any error
        logging.info(f"creating directory: {filedir} for the file {filename}") #   logging.info 
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #   if file is not present or file is empty/no-size then create the file
        with open(filepath, 'w') as f:
            pass
            
        logging.info(f"Creating empty file: {filepath}")
    else:
        
        logging.info(f"{filename} already exists")
        

        

    
    

    

