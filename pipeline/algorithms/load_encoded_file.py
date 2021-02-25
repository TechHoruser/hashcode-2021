import numpy
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams
from pipeline.algorithms.load_file import LoadFile

class LoadEncodedFile(PipelineAlgorithmInterface):
    INPUT_PATH = "./data/in/"
    INPUT_EXTENSION = ".encoded"
    SEPARATOR = " "
    ELEMENT_TYPE_FIRST_LINE = int
    ELEMENT_TYPE_OTHER_LINES = int

    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        with open(
            LoadEncodedFile.INPUT_PATH + global_params.filename + LoadEncodedFile.INPUT_EXTENSION
        ) as f:
            content = f.readlines()

        all_data = [
            numpy.array((line.replace("\n", "")).strip().split(LoadEncodedFile.SEPARATOR))
            .astype(
                LoadEncodedFile.ELEMENT_TYPE_FIRST_LINE
                if idx == 0
                else LoadEncodedFile.ELEMENT_TYPE_OTHER_LINES
            )
            .tolist()
            for idx, line in enumerate(content)
        ]

        global_params.data_without_encode = all_data[:LoadFile.FIRST_ROW_OF_ELEMENT]
        global_params.data_to_process = all_data[LoadFile.FIRST_ROW_OF_ELEMENT:]