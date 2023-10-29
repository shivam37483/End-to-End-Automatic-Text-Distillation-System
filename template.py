import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: [%(message)s]:')

project_name = "Text-Summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",       #.github -> used for cicd deployment; workflows cannot be empty -> .gitkeep hidden file which will later be replaced by .yml file
    f"src/{project_name}/__init__.py",  #__init__.py -> used to mark directories on disk as Python package directories so they can be used as local packages
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py",         #common.py -> will contain all utilities
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py",  
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",               
    "params.yaml",                      #params.yaml -> will contain all the parameters
    "app.py",                           #app.py -> will contain all the code for the application
    "main.py",
    "Dockerfile",               #we will build docker image of source code and do the deployment
    "requirements.txt",         #requirements.txt -> will contain all the dependencies
    "setup.py",
    "research/trials.ipynb",                #trials.ipynb -> will contain all notebook expereiments
]

for file_path in list_of_files:
    file_path = Path(file_path)            #Path() -> will resolve path issue for different OS
    file_dir, filename = os.path.split(file_path)

    if file_dir != "":                  #folder creation
        os.makedirs(file_dir, exist_ok=True)      #os.makedirs() -> will create directory if it doesn't exist; exist_ok=True -> will not throw error if directory already exists
        logging.info(f"Created directory at {file_dir}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):       #file creation
        with open(file_path, "w") as f:            #with open() -> will create file if it doesn't exist
            pass
            logging.info(f"Created file at {file_path}")

    else:
        logging.info(f"File already exists at {file_path}")


