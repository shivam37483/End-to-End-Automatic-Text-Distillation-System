from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)                     #frozen = True makes the class immutable (read-only)
class DataIngestionConfig:             #defininig return type of the function which will be made later 
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True) 
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass(frozen=True)              #Its a configuraton class for data transformation which will be used by other classes
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path

    # Parameters
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir:Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path