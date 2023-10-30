from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidator

from textSummarizer import logging

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidator(config=data_validation_config)
        data_validation.validate_all_files_present()