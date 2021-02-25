from datetime import datetime
from pydantic import BaseModel


class GlobalAlgoritmParams(BaseModel):
    filename: str
    test_group_percent: float = None
    test_group_amount: float = None
    data_to_process: list = None
    data_without_encode: list = None
    number_of_threads: int = 4
    result_data: list = None
