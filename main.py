from TumorClassifier import logger
from TumorClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TumorClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from TumorClassifier.pipeline.stage_03_training import ModelTrainingPipeline
import os


STAGE_NAME = "Data Ingestion Stage"

try :

    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed \n\n x===============x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try :

    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>> stage {STAGE_NAME} completed \n\n x===============x")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training"
try :

    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model = ModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>> stage {STAGE_NAME} completed \n\n x===============x")

except Exception as e:
    logger.exception(e)
    raise e