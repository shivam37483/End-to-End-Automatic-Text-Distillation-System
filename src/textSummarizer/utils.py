from textSummarizer import logging
import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations              #ensures that the type of the arguments passed to the function is the same as the type of the arguments in the function definition
from box import ConfigBox                 #ConfigBox allows to easily call values from a yaml file as a dictionary 
from pathlib import Path
from typing import Any

@ensure_annotations           #better practice coz we are defining the type of parameters in all the functions in this module
def read_yaml(path_to_yaml: Path) -> ConfigBox:             #path_to_yaml: Path does not allow any other type of argument to be passed to the function besides Path
    '''
    Read Yaml file and returns
    
    Args:
        path_to_yaml (str): Path like input

    Raises:
        ValueError: If yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox type           #ConfigBox is a class from box module that allows to access the yaml file as a dictionary
    '''

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            logging.logger.info(f"yaml filr: {path_to_yaml} loaded successfully")

            return ConfigBox(content)            #returns the yaml file as a dictionary
        
    except BoxValueError:          #BoxValueError is an exception from box module that is raised when the yaml file is empty
        raise ValueError(f"Yaml file {path_to_yaml} is empty")   
    
    except Exception as e:          #handles any other exception that might be raised
        raise e      
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    Create a list of directories

    Args:
        path_to_directories (list): List of directories
        ignore _log (bool, optional): Ignore if multiple directories are created. Defaults to false.

    '''

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)        #creates the directories in the list if they do not exist already
        if verbose:
            logging.logger.info(f"Directory created at {path}")

            
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)          
    return f"~ {size_in_kb} KB"


