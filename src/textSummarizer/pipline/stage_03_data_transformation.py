from textSummarizer.logging import logger

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager().get_data_transformation_config()
            config = DataTransformation(config=config)
            config.convert()

        except Exception as e:
            logger.info(f"error in data transformation: {e}")
            raise e