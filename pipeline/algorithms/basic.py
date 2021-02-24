from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class Basic(PipelineAlgorithmInterface):
    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        global_params.result_data = [
            [1, 2],
            [3, 4, 5]
        ]