import numpy
from pipeline.pipeline_processes.pipeline_process_interface import PipelineProcessInterface
from pipeline.global_params import GlobalParams

class SaveFile(PipelineProcessInterface):
    OUTPUT_PATH = "./data/out/"
    OUTPUT_EXTENSION = ".out"

    @classmethod
    def execute(cls, global_params: GlobalParams):
        actions_to_do = []
        for action in global_params.stage.actions_to_do:
            semaphores = []
            for semaphore in action.semaphores:
                if semaphore.time_on > 0:
                    semaphores.append([semaphore.street_name, semaphore.time_on])
            
            actions_to_do += [
                action.intersection.index,
                len(semaphores),
            ] + semaphores
        data_to_export = [len(global_params.stage.actions_to_do)] + actions_to_do

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