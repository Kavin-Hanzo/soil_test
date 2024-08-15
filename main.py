from src.soiltester import logger
from src.soiltester.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.soiltester.pipeline.stage_02_prepare_base_model import PrepareBaseTrainingPipeline
from src.soiltester.pipeline.stage_03_training import ModelTrainingPipeline
#from src.soiltester.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
        logger.info(f"***********************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"
try: 
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

