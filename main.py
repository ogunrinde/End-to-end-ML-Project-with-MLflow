from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

try:
    STAGE_NAME = "Data Ingestion stage"
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


try:
    STAGE_NAME = "Data Validation Stage"
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


try:
    STAGE_NAME = "Data Transformation Stage"
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e