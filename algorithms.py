import random
from concurrent.futures import ThreadPoolExecutor
from manager_file import ManagerFile

class BaseAlgorithms:
    """ This class is destined to implement algorithms as functions """

    @classmethod
    def encode_file(cls, file, method_of_algorithm):
        """ This method encode a data file and save it, if yet exist return that """
        pass

    @classmethod
    def subgroup_process(cls, input_array, method_of_algorithm, test_group_percent = None, test_group_amount = None):
        """ This method return a random subgroup data """
        data_array = input_array[ManagerFile.FIRST_ROW_OF_ELEMENT:]
        if test_group_percent:
            if test_group_percent < 0 or test_group_percent > 1:
                raise ValueError('Invalid \'test_group_percent\' (%s)' % test_group_percent)

            test_group_amount = int(len(data_array) * test_group_percent)

        if test_group_amount:
            random.shuffle(data_array)
            data_array = data_array[:test_group_amount]

        return method_of_algorithm(input_array[:ManagerFile.FIRST_ROW_OF_ELEMENT] + data_array)


    @classmethod
    def basic(cls, input_array):
        _,number_of_two_person_teams,number_of_three_person_teams,number_of_four_person_teams = input_array[0]
        array_of_pizzas = [pizza_row[1:] for pizza_row in input_array[1:]]
        encoded_pizzas, encoded_ingredients = PerformanceUtils.encode_array(array_of_pizzas, 2)
        array_of_pizzas = [{
            'index': index,
            'ingredients': pizza_row,
        } for index, pizza_row in enumerate(encoded_pizzas)]

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


        return result

    @classmethod
    def get_pizzas_to_group(cls, number_of_persons, array_of_pizzas):
        if len(array_of_pizzas) < number_of_persons:
            return

        result = []
        for _ in range(number_of_persons):
            result.append(array_of_pizzas.pop()['index'])

        return result


# Based in Slides Problem
class ListsUtils:
    @classmethod
    def diff_lists(cls, list1, list2):
        return list1 - list2

    @classmethod
    def intersect_lists(cls, list1, list2):
        return (list1 - list2) | (list2 - list1)

    @classmethod
    def union_lists(cls, list1, list2):
        return list1 | (list2 - list1)

    @classmethod
    def calc_score_between_lists(cls, list1, list2):
        return min(
            len(ListsUtils.diff_lists(list1, list2)),
            len(ListsUtils.union_lists(list1, list2)),
            len(ListsUtils.diff_lists(list2, list1)),
        )

class PerformanceUtils:
    @classmethod
    def encode_array(cls, input_array, number_of_threads):
        features = []
        executor = ThreadPoolExecutor(number_of_threads)

        futures = []
        for number_of_thread in range(number_of_threads):
            from_index = int(number_of_thread*len(input_array)/number_of_threads)
            to_index = int((number_of_thread+1)*len(input_array)/number_of_threads)
            futures.append(executor.submit(cls.sub_encode_array, input_array[from_index:to_index], features))

        ended = False
        while not ended:
            ended = True
            for future in futures:
                ended &= future.done()

        results = []

        for future in futures:
            results += future.result()[0]

        return (results, features)


    @classmethod
    def sub_encode_array(cls, input_array, features = []):
        output_array = []
        for element in input_array:
            if isinstance(element, list):
                output_element = cls.sub_encode_array(element, features)[0]
                output_array.append(output_element)
            
            else:
                if element not in features:
                    features.append(element)
                output_array.append(features.index(element))
        
        return (output_array, features)
