import abc
from pipeline.global_params import GlobalParams

class PipelineProcessInterface(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def execute(cls, global_params: GlobalParams):
        """Load call pipeline invoke"""
        raise NotImplementedError