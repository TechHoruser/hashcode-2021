import numpy
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class SetIndexes(PipelineAlgorithmInterface):
    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        global_params.data_to_process = [{
            'index': index,
            'element': element
        } for index, element in enumerate(global_params.data_to_process)]