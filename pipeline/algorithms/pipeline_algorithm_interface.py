import abc
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class PipelineAlgorithmInterface(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def execute(cls, global_algorithm_params: GlobalAlgoritmParams):
        """Load call pipeline invoke"""
        raise NotImplementedError