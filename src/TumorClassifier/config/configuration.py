import sys
sys.path.append('/Users/udita19/Desktop/Projects/BrainTumorClassification/src')


from TumorClassifier.constants import*
from TumorClassifier.utils.common import read_yaml, create_directories
from TumorClassifier.entity import config_entity
from TumorClassifier.entity.config_entity import DataIngestionConfig
from TumorClassifier.entity.config_entity import (PrepareBaseModelConfig, PrepareCallbacksConfig)

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
    


    def  get_prepare_base_model_config(self)->PrepareBaseModelConfig:

        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(

            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate =  self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return prepare_base_model_config
    

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([

            Path(model_ckpt_dir),
            Path (config. tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config



    