from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlproject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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


try:
    STAGE_NAME = "Model Trainer Stage"
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


try:
    STAGE_NAME = 'Model Evaluation'
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e
