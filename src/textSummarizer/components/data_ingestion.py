import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {file_name}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")

    def unzip_file(self):
        '''
        Extracts the zip file into data dictionary
        Function returns none
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        
        logger.info(f"Unzipping {self.config.local_data_file} to {unzip_path}")
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)

             