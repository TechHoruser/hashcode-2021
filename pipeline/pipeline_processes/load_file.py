import numpy
from pipeline.pipeline_processes.pipeline_process_interface import PipelineProcessInterface
from pipeline.global_params import (
    Street,
    Car,
    Stage,
    Intersection,
    Semaphore,
    Action,
    GlobalParams
)


class LoadFile(PipelineProcessInterface):
    INPUT_PATH = "./data/in/"
    INPUT_EXTENSION = ".txt"
    SEPARATOR = " "
    ELEMENT_TYPE_FIRST_LINE = int
    ELEMENT_TYPE_OTHER_LINES = str
    FIRST_ROW_OF_ELEMENT = 1

    @classmethod
    def execute(cls, global_params: GlobalParams):
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


        seconds,_,number_of_streets,_,_ = all_data[0]
        intersections = {}
        streets = {}
        for row in all_data[1:number_of_streets+1]:
            streets[row[2]] = Street(start_index=row[0], end_index=row[1], name=row[2], length=row[3])
            if row[1] not in intersections:
                intersections[row[1]] = Intersection(index=row[1])
            streets[row[2]].semaphore = Semaphore(street_name=streets[row[2]].name)
            intersections[row[1]].streets.append(streets[row[2]])
        
        actions_to_do = []
        for _, intersection in intersections.items():
            actions_to_do.append(Action(intersection=intersection, semaphores=[street.semaphore for street in intersection.streets]))
        
        cars = [Car(
            route=[
                streets[street_name]
                for street_name
                in row[1:]
            ],
            current_street=streets[row[1]]
        ) for row in all_data[number_of_streets+1:]]


        global_params.stage = Stage(
            rest_time=seconds,
            streets=streets,
            cars=cars,
            intersections=intersections,
            actions_to_do=actions_to_do
        )