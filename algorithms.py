class BaseAlgorithms:
    @classmethod
    def basic(cls, photoList):
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
