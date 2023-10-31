from textSummarizer.utils import read_yaml,create_directories 
from textSummarizer import constants

from textSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig


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
    
    
    def get_data_validation_config(self) -> DataValidationConfig:       #function to return the DataIngestionConfig object
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])      #root_path is the path where all the data will be stored present in the config.yaml file

        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name)
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_training
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        return ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,

            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )
