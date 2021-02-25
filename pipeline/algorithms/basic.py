from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class Basic(PipelineAlgorithmInterface):
    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        _,number_of_two_person_teams,number_of_three_person_teams,number_of_four_person_teams = global_params.data_to_process[0]
        array_of_pizzas = [{
            'index': index,
            'ingredients': pizza_row[1:],
        } for index, pizza_row in enumerate(global_params.data_to_process[1:])]

        result = []
        for _ in range(number_of_two_person_teams):
            pizzas_to_group = cls.get_pizzas_to_group(2, array_of_pizzas)
            if pizzas_to_group:
                result.append([2] + pizzas_to_group)

        for _ in range(number_of_three_person_teams):
            pizzas_to_group = cls.get_pizzas_to_group(3, array_of_pizzas)
            if pizzas_to_group:
                result.append([3] + pizzas_to_group)

        for _ in range(number_of_four_person_teams):
            pizzas_to_group = cls.get_pizzas_to_group(4, array_of_pizzas)
            if pizzas_to_group:
                result.append([4] + pizzas_to_group)


        global_params.result_data = result


    @classmethod
    def get_pizzas_to_group(cls, number_of_persons, array_of_pizzas):
        if len(array_of_pizzas) < number_of_persons:
            return

        result = []
        for _ in range(number_of_persons):
            result.append(array_of_pizzas.pop()['index'])

        return result