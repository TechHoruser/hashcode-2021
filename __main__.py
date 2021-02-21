from datetime import datetime
from algorithms import BaseAlgorithms
from manager_file import ManagerFile

examples = [
    {"fileName": "a_example", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "b_little_bit_of_everything", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "c_many_ingredients", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "d_many_pizzas", "algorithm": BaseAlgorithms.subgroup_process, "algorithm_params": [BaseAlgorithms.basic, .05],},
    {"fileName": "e_many_teams", "algorithm": BaseAlgorithms.subgroup_process, "algorithm_params": [BaseAlgorithms.basic, .05],},
]


for indx, example in enumerate(examples):
    start_datetime = datetime.now()
    print(
        "Processing file:",
        example["fileName"],
        "(" + str(indx + 1) + "/" + str(len(examples)) + ")",
        flush=False,
    )
    print("Start at: %s" % start_datetime.strftime('%H:%M:%S'))
    mf = ManagerFile(example["fileName"])
    input_array = mf.loadFile()

    if 'algorithm_params' in example:
        output = example["algorithm"](input_array, *example['algorithm_params'])
    else:
        output = example["algorithm"](input_array)

    end_datetime = datetime.now()
    print("End at: %s (%s)" % (end_datetime.strftime('%H:%M:%S'), str(end_datetime-start_datetime)))

    mf.saveFile([len(output)] + output)
