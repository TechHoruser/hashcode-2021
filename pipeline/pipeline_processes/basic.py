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

class Basic(PipelineProcessInterface):
    @classmethod
    def execute(cls, global_params: GlobalParams):
        streets = {}
        # Set the number that a street appears
        for car in global_params.stage.cars:
            for street in car.route:
                if street.name not in streets:
                    streets[street.name] = 0
                streets[street.name] += 1
        
        for _, intersection in global_params.stage.intersections.items():
            count_of_occurrences_street_in_routes = 0
            for street in intersection.streets:
                count_of_occurrences_street_in_routes += streets[street.name] if street.name in streets else 0
            
            # If at least one car passes through the intersection: calc the percent for an intersection semaphore
            # compared to others in the same intersection and stablish the time of the semaphore with this value
            # TODO: Stablish a maximun time
            if count_of_occurrences_street_in_routes > 0:
                for street in intersection.streets:
                    percent = streets[street.name]/count_of_occurrences_street_in_routes if street.name in streets else 0
                    street.semaphore.time_on = 0 if percent == 0 else 1 if 0 < percent < 1 else round(percent)
        