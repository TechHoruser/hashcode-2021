import numpy
from pipeline.pipeline_processes.pipeline_process_interface import PipelineProcessInterface
from pipeline.global_params import GlobalParams

class SaveEncodedDataToFile(PipelineProcessInterface):
    OUTPUT_PATH = "./data/in/"
    OUTPUT_EXTENSION = ".encoded"

    @classmethod
    def execute(cls, global_params: GlobalParams):
        data_to_export = global_params.data_without_encode + global_params.data_to_process

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