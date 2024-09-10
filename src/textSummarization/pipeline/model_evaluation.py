from textSummarization.config.configuration import ConfigurationManager
from src.textSummarization.components.model_evaluation import ModelEvaluation
from src.textSummarization.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
