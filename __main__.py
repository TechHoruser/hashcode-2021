from datetime import datetime
from pipeline.pipeline import Pipeline, SubPipeline
from pipeline.global_algoritm_params import GlobalAlgoritmParams
from pipeline.algorithms.load_file import LoadFile
from pipeline.algorithms.set_new_subgroup_process_data import SetNewSubgroupProcess
from pipeline.algorithms.save_file import SaveFile
from pipeline.algorithms.load_encoded_file import LoadEncodedFile
from pipeline.algorithms.encode_data import EncodeData
from pipeline.algorithms.save_encoded_data_to_file import SaveEncodedDataToFile
from pipeline.algorithms.basic import Basic

load_pipeline = SubPipeline(
    [
        LoadEncodedFile,
        SubPipeline([LoadFile, EncodeData, SaveEncodedDataToFile])
    ], True
)

pipelines = [
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalAlgoritmParams(filename = "a_example")),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalAlgoritmParams(filename = "b_little_bit_of_everything")),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalAlgoritmParams(filename = "c_many_ingredients")),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalAlgoritmParams(filename = "d_many_pizzas")),
    Pipeline([
        load_pipeline,
        # SetNewSubgroupProcess,
        Basic,
        SaveFile,
    ], GlobalAlgoritmParams(filename = "e_many_teams", test_group_percent=.1)),
]


for indx, pipeline in enumerate(pipelines):
    start_datetime = datetime.now()
    print(
        "Processing file:",
        pipeline.global_algorithm_params.filename,
        "(" + str(indx + 1) + "/" + str(len(pipelines)) + ")",
        flush=False,
    )
    print("Start at: %s" % start_datetime.strftime('%H:%M:%S'))
    
    pipeline.execute()

    end_datetime = datetime.now()
    print("End at: %s (%s)" % (end_datetime.strftime('%H:%M:%S'), str(end_datetime-start_datetime)))
