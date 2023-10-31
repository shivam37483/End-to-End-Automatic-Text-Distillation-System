from textSummarizer.logging import logger

from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipline.stage_04_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info("Stage: {}".format(STAGE_NAME))
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Stage: {} completed successfully".format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data VALIDATION Stage"
try:
    logger.info("Stage: {}".format(STAGE_NAME))
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info("Stage: {} completed successfully".format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data TRANSFORMATION Stage"
try:
    logger.info("Stage: {}".format(STAGE_NAME))
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info("Stage: {} completed successfully".format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL TRAINING Stage"
try:
    logger.info("Stage: {}".format(STAGE_NAME))
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info("Stage: {} completed successfully".format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e