from pathlib import Path

#This file will return the path of both the config.yaml params.yaml file 
#Therefore instead of using the absolute path we can call them from here as their paths are constant

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")