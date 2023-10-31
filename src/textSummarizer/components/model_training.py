from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
import torch
import os

from textSummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'            #check if gpu is available or not and sets the device accordingly
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)         #load the tokenizer 
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)        #load the model and send it to the device (gpu or cpu)
        seq2seq_data_collector = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)             #data collector for seq2seq model which will be used for training the model 

        dataset_samsum_pt = load_from_disk(self.config.data_path)           #load the dataset from the disk 

        
        trainer_args = TrainingArguments(                   #training arguments for the trainer present in yaml file
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )


        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collector,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"]
            )
        
        trainer.train()             #train the model

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,'pegasus-samsum-model'))           #save the model in the root directory 

        tokenizer.save_pretrained(os.path.join(self.config.root_dir,'pegasus-samsum-tokenizer'))           #save the tokenizer in the root directory        
    