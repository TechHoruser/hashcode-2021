import numpy
from pipeline.pipeline_processes.pipeline_process_interface import PipelineProcessInterface
from pipeline.global_params import GlobalParams

class SetIndexes(PipelineProcessInterface):
    @classmethod
    def execute(cls, global_params: GlobalParams):
        global_params.data_to_process = [{
            'index': index,
            'element': element
        } for index, element in enumerate(global_params.data_to_process)]