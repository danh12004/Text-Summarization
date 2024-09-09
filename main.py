from src.textSummarization.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.textSummarization.pipeline.data_validation import DataValidationTrainingPipeline
from src.textSummarization.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.textSummarization.pipeline.model_trainer import ModelTrainerTrainingPipeline
from src.textSummarization.logging import logger

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e