from textSummarizer.logging import logger

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation 


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(model_evaluation_config)
            model_evaluation_config.evaluate()

        except Exception as e:
            logger.info(f"error in Model Evaluation: {e}")
            raise e