import numpy
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class SaveFile(PipelineAlgorithmInterface):
    OUTPUT_PATH = "./data/out/"
    OUTPUT_EXTENSION = ".out"

    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        data_to_export = [len(global_params.result_data)] + global_params.result_data

        data = [
            " ".join(numpy.array(element).astype(str).tolist())
            if type(element) == list
            else element
            for element in data_to_export
        ]
        return numpy.savetxt(
            SaveFile.OUTPUT_PATH + global_params.filename + SaveFile.OUTPUT_EXTENSION,
            X=data,
            delimiter=" ",
            fmt="%s",
        )