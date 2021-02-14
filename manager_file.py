from os.path import split

import numpy


class ManagerFile:
    INPUT_PATH = "./data/in/"
    INPUT_EXTENSION = ".in"
    OUTPUT_PATH = "./data/out/"
    OUTPUT_EXTENSION = ".out"
    ELEMENT_TYPE_FIRST_LINE = int
    ELEMENT_TYPE_OTHER_LINES = int

    def __init__(self, fileName):
        self.__fileName = fileName

    def loadFile(self, separator=" "):
        with open(
            ManagerFile.INPUT_PATH + self.__fileName + ManagerFile.INPUT_EXTENSION
        ) as f:
            content = f.readlines()

        return [
            numpy.array((line.replace("\n", "")).split(separator))
            .astype(
                ManagerFile.ELEMENT_TYPE_FIRST_LINE
                if idx == 0
                else ManagerFile.ELEMENT_TYPE_OTHER_LINES
            )
            .tolist()
            for idx, line in enumerate(content)
        ]

    def saveFile(self, data):
        data = [
            " ".join(numpy.array(element).astype(str).tolist())
            if type(element) == list
            else element
            for element in data
        ]
        return numpy.savetxt(
            ManagerFile.OUTPUT_PATH + self.__fileName + ManagerFile.OUTPUT_EXTENSION,
            X=data,
            delimiter=" ",
            fmt="%s",
        )
