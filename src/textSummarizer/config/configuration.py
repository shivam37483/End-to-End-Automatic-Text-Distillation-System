from textSummarizer.utils import read_yaml,create_directories 
from textSummarizer import constants

from textSummarizer.entity import DataIngestionConfig 

class ConfigurationManager:      #class to read the config file and params file
    def __init__(
            self,
            config_file_path = constants.CONFIG_FILE_PATH,       #constants is a file which contains all the paths 
            params_file_path = constants.PARAMS_FILE_PATH
            ):
        
        self.config = read_yaml(config_file_path)      #read_yaml is a function which reads the yaml file and returns a dictionary
        self.params = read_yaml(params_file_path)

        #config is a ConfigBox(shown in trials.ipynb) object which is a dictionary with dot notation access with help of read_yaml function
        create_directories([self.config.artifacts_root])              #create_directories is a function which creates directories if they don't exist; artifacts_root is the path where all the artifacts will be stored present in the config.yaml file

    def get_data_ingestion_config(self) -> DataIngestionConfig:       #function to return the DataIngestionConfig object
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        # return DataIngestionConfig(
        #     root_dir = config.root_dir,
        #     source_URL = config.source_URL,
        #     local_data_file = config.local_data_file,
        #     unzip_dir = config.unzip_dir
        # )        

        return data_ingestion_config