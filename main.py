from src.textSummarization.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.textSummarization.pipeline.data_validation import DataValidationTrainingPipeline
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