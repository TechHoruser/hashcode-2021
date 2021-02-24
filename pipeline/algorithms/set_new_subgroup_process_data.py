import random
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.algorithms.load_file import LoadFile
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class SetNewSubgroupProcess(PipelineAlgorithmInterface):
    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        """ This method return a random subgroup data """
        if not global_params.test_group_percent and not global_params.test_group_amount:
            raise EnvironmentError('Not defined subgroup lenght for the process')

        data_array = global_params.data_to_process[LoadFile.FIRST_ROW_OF_ELEMENT:]
        if global_params.test_group_percent:
            if global_params.test_group_percent < 0 or global_params.test_group_percent > 1:
                raise ValueError('Invalid \'test_group_percent\' (%s)' % global_params.test_group_percent)

            global_params.test_group_amount = int(len(data_array) * global_params.test_group_percent)

        if global_params.test_group_amount:
            random.shuffle(data_array)
            data_array = data_array[:global_params.test_group_amount]

        global_params.data_to_process = global_params.data_to_process[:LoadFile.FIRST_ROW_OF_ELEMENT] + data_array