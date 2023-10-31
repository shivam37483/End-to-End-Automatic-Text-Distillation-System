import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from textSummarizer.config.configuration import DataTransformationConfig 

class DataTransformation:       #class to transform the data
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)      #AutoTokenizer is a class from transformers library which is used to tokenize the data

    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):           #start data transformation
        logger.info("Starting data transformation")

        logger.info("Loading dataset")
        dataset_samsum = load_from_disk(self.config.data_path)       #load_from_disk is a function from datasets library which loads the dataset from the path provided
        
        logger.info("Converting dataset to features")
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features,batched=True)      #map is a function from datasets library which applies the function to the dataset

        logger.info("Saving dataset")        
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,'samsum_dataset'))        #save_to_disk is a function from datasets library which saves the dataset to the path provided
        
        logger.info("Data transformation completed")
