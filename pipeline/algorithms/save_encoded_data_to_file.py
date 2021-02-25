import numpy
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class SaveEncodedDataToFile(PipelineAlgorithmInterface):
    OUTPUT_PATH = "./data/in/"
    OUTPUT_EXTENSION = ".encoded"

    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        data_to_export = global_params.data_to_process

        data = [
            " ".join(numpy.array(element).astype(str).tolist())
            if type(element) == list
            else element
            for element in data_to_export
        ]
        return numpy.savetxt(
            SaveEncodedDataToFile.OUTPUT_PATH + global_params.filename + SaveEncodedDataToFile.OUTPUT_EXTENSION,
            X=data,
            delimiter=" ",
            fmt="%s",
        )