import numpy as np

class BaseAlgorithms:
    @classmethod
    def basic(cls, input_array):
        number_of_pizzas,number_of_two_person_teams,number_of_three_person_teams,number_of_four_person_teams = input_array[0]
        array_of_pizzas = [pizza_row[1:] for pizza_row in input_array[1:]]
        encoded_pizzas, encoded_ingredients = PerformanceUtils.encodeArray(array_of_pizzas)

        return [""]


# Based in Slides Problem
class ListsUtils:
    @classmethod
    def diffLists(cls, list1, list2):
        return list1 - list2

    @classmethod
    def intersectLists(cls, list1, list2):
        return (list1 - list2) | (list2 - list1)

    @classmethod
    def unionLists(cls, list1, list2):
        return list1 | (list2 - list1)

    @classmethod
    def calcScoreBetweenLists(cls, list1, list2):
        return min(
            len(ListsUtils.diffLists(list1, list2)),
            len(ListsUtils.unionLists(list1, list2)),
            len(ListsUtils.diffLists(list2, list1)),
        )

class PerformanceUtils:
    @classmethod
    def encodeArray(cls, input_array, features = []):
        output_array = []
        for element in input_array:
            if type(element) is type([]):
                output_element, features = cls.encodeArray(element, features)
                output_array.append(output_element)
            
            else:
                if element not in features:
                    features.append(element)
                output_array.append(features.index(element))
        
        return (output_array, features)
