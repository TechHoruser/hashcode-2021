import numpy
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class LoadFile(PipelineAlgorithmInterface):
    INPUT_PATH = "./data/in/"
    INPUT_EXTENSION = ".in"
    SEPARATOR = " "
    ELEMENT_TYPE_FIRST_LINE = int
    ELEMENT_TYPE_OTHER_LINES = str
    FIRST_ROW_OF_ELEMENT = 1

    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        with open(
            LoadFile.INPUT_PATH + global_params.filename + LoadFile.INPUT_EXTENSION
        ) as f:
            content = f.readlines()

        all_data = [
            numpy.array((line.replace("\n", "")).strip().split(LoadFile.SEPARATOR))
            .astype(
                LoadFile.ELEMENT_TYPE_FIRST_LINE
                if idx == 0
                else LoadFile.ELEMENT_TYPE_OTHER_LINES
            )
            .tolist()
            for idx, line in enumerate(content)
        ]

        global_params.data_without_encode = all_data[:LoadFile.FIRST_ROW_OF_ELEMENT]
        global_params.data_to_process = all_data[LoadFile.FIRST_ROW_OF_ELEMENT:]