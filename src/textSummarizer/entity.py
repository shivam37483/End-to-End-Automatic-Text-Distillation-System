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