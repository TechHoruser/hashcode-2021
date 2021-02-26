from datetime import datetime
from pydantic import BaseModel


class Semaphore(BaseModel):
    street_name: str = None
    time_on: int = 1

class Street(BaseModel):
    start_index: int
    end_index: int
    name: str
    length: int
    semaphore: Semaphore = None
    waiting_cars: int = None

class Car(BaseModel):
    route: list
    current_street: Street
    route_time: int = 0
    rest_time_routing_street: int = 0

class Stage(BaseModel):
    rest_time: int
    streets: dict
    cars: list
    intersections: dict
    actions_to_do: list = []

class Intersection(BaseModel):
    index: int
    streets: list = []

class Action(BaseModel):
    intersection: Intersection
    semaphores: list = []

class GlobalParams(BaseModel):
    filename: str
    test_group_percent: float = None
    test_group_amount: float = None
    stage: Stage = None
    number_of_threads: int = 4
    result_data: list = [] 
