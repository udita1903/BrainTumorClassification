from dataclasses import dataclass 
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    non_tumor_source_URL: str
    golima_source_URL: str

    non_tumor_local_file: Path
    golima_local_file: Path
    unzip_dir: Path