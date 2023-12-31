from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import BaseModelPreparationPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipelline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipelline


STAGE_NAME = 'Data Ingestion Stage.'

try:
    logger.info(f'>>>>>>stage {STAGE_NAME} started<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>stage {STAGE_NAME} completed<<<<<<<\n\nx=====================x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Prepare base model'
try:
    logger.info('****************************************')
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
    obj = BaseModelPreparationPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'TRAINING'

try:
    logger.info(f'****************************************')
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
    obj = TrainingPipelline()
    obj.main()
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'MODEL EVALUATION'
try:
    logger.info(f'****************************************')
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
    obj = EvaluationPipelline()
    obj.main()
    logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e
