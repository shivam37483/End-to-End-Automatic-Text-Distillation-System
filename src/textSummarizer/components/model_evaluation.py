from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_metric, load_from_disk, load_dataset
import pandas as pd
import torch
import tqdm as tqdm

from textSummarizer.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def generate_batch_sized_chunks(self,list_of_elements, batch_size):
        '''
        Splitting the dataset into smaller batches such that we can process simultaneously
        Yield successive batch-sized chunks from list_of_elements.
        '''
        for i in range(0, len(list_of_elements), batch_size):       #this finction is used to split the dataset into smaller batches
            yield list_of_elements[i:i + batch_size]       #yield is used to return a generator object -> generator object is an iterator which can be iterated only once


    def calculate_metric_on_test_ds(self,dataset,metric,model,tokenizer,
                                    batch_size=16,
                                    device='cuda'if torch.cuda.is_available() else 'cpu',
                                    column_text = 'article',         #column_text is the column name of the dataset which contains the text to be summarized
                                    column_summary = 'highlights'):           #column_summary is the column name of the dataset which contains the summary of the text
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text],batch_size))               #generate_batch_sized_chunks is a function which splits the dataset into smaller batches
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary],batch_size))

        for article_batch,target_batch in tqdm(
            zip(article_batches,target_batches),
            total=len(article_batches)):

            inputs = tokenizer(article_batch,max_length= 1024,             #tokenizer is used to tokenize the input text and return the input_ids and attention_mask -> input_ids is a tensor containing the indices of the tokens in the input sequence
                               truncation=True, padding='max_length',return_tensors='pt')
            
            summaries = model.generate(input_ids= inputs['input_ids'].to(device),
                                       attention_mask = inputs['attention_mask'].to(device),           #attention_mask is a mask that is used to avoid performing attention on padding token indices 
                                       length_penalty=0.8,     # parameter for length penalty ensures that the model does not generate sequences that are too long. 
                                       num_beams=8,        #num_beams is the number of beams for beam search 
                                       max_length=128)     #max_length is the maximum length of the sequence to be generated. An input sequence longer than max_length will be truncated to max_length
            
            #We decode the genrated texts using the tokenizer, replace the token and add the decoded texts with references to metric

            decoded_summaries = [tokenizer.decode(g,skip_special_tokens=True,
                                                  clean_up_tokenization_spaces=True)
                                  for g in summaries]
            
            decoded_summaries = [d.replace('', " ") for d in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries,references=target_batch)

        #Finally we compute the metric and return the ROUGE scores
        score = metric.compute()
        return score
    
    def evaluate(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

        #Loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1","rouge2","rougeL","rougeLsum"]
        rouge_metric = load_metric('rouge')

        score = self.calculate_metric_on_test_ds(dataset_samsum_pt['test'][0:10],
                                                 rouge_metric,model_pegasus,
                                                 tokenizer, batch_size=2,
                                                 column_text = 'dialogue', column_summary= 'summary')
        
        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)

        df =pd.DataFrame([rouge_dict],index=['pegasus'])
        df.to_csv(self.config.metric_file_name, index=False)