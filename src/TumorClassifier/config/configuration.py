import sys
sys.path.append('/Users/udita19/Desktop/Projects/BrainTumor/BrainTumorClassification/src')


from TumorClassifier.constants import*
from TumorClassifier.utils.common import read_yaml, create_directories
from TumorClassifier.entity import config_entity
from TumorClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH) :
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig :
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
        root_dir = config.root_dir,
        non_tumor_source_URL = config.non_tumor_source_URL,
        golima_source_URL = config.golima_source_URL,
        non_tumor_local_file = config.non_tumor_local_file,
        golima_local_file = config.golima_local_file,
        unzip_dir = config.unzip_dir
        )

        return data_ingestion_config


    