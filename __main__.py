from algorithms import BaseAlgorithms
from manager_file import ManagerFile

examples = [
    {"fileName": "a_example", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "b_little_bit_of_everything", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "c_many_ingredients", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "d_many_pizzas", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "e_many_teams", "algorithm": BaseAlgorithms.basic,},
]


for indx, example in enumerate(examples):
    print(
        "Processing file:",
        example["fileName"],
        "(" + str(indx + 1) + "/" + str(len(examples)) + ")",
        flush=False,
    )
    mf = ManagerFile(example["fileName"])
    input_array = mf.loadFile()

    output = example["algorithm"](input_array)

    mf.saveFile([len(output), output])
