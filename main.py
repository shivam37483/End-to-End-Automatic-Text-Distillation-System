from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("Stage: {}".format(STAGE_NAME))
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Stage: {} completed successfully".format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e