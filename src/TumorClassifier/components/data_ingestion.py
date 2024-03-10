import os 
import urllib.request as request
import zipfile 
from TumorClassifier import logger 
from TumorClassifier.utils.common import get_size
from TumorClassifier.entity import config_entity
from TumorClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config




    def download_file(self):
        if not os.path.exists(self.config.non_tumor_local_file):
            filename, headers = request.urlretrieve(
                self.config.non_tumor_source_URL, 
                self.config.non_tumor_local_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.non_tumor_local_file))}")

        if not os.path.exists(self.config.golima_local_file):
            filename, headers = request.urlretrieve(
                self.config.golima_source_URL,
                self.config.golima_local_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
               logger.info(f"File already exists of size : {get_size(Path(self.config.golima_local_file))}")





    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.golima_local_file, 'r') as zip_ref:
            # Extract all items from the zip file, excluding __MACOSX folder
            for item in zip_ref.infolist():
                if "__MACOSX" not in item.filename:
                    zip_ref.extract(item, unzip_path)

        with zipfile.ZipFile(self.config.non_tumor_local_file, 'r') as zip_ref:
            # Extract all items from the zip file, excluding __MACOSX folder
            for item in zip_ref.infolist():
                if "__MACOSX" not in item.filename:
                    zip_ref.extract(item, unzip_path)