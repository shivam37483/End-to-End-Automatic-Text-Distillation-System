import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidator:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_present(self) -> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    logger.info(f"File {file} not found")
                    
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"VAILDATION STATUS: {validation_status}")
                else:
                    validation_status = True    
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"VAILDATION STATUS: {validation_status}")
                        logger.info(f"File {file} found")

            return validation_status
        except Exception as e:  
            logger.error(e)
            raise e