from datetime import datetime
from pipeline.pipeline import Pipeline, SubPipeline
from pipeline.global_params import GlobalParams
from pipeline.pipeline_processes.load_file import LoadFile
from pipeline.pipeline_processes.set_new_subgroup_process_data import SetNewSubgroupProcess
from pipeline.pipeline_processes.save_file import SaveFile
from pipeline.pipeline_processes.load_encoded_file import LoadEncodedFile
from pipeline.pipeline_processes.encode_data import EncodeData
from pipeline.pipeline_processes.save_encoded_data_to_file import SaveEncodedDataToFile
from pipeline.pipeline_processes.set_indexes import SetIndexes
from pipeline.pipeline_processes.basic import Basic

load_pipeline = SubPipeline(
    [
        LoadEncodedFile,
        SubPipeline([LoadFile, EncodeData, SaveEncodedDataToFile])
    ], True
)
load_pipeline = SubPipeline(
    [LoadFile]
)

pipelines = [
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalParams(filename = "a")),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalParams(filename = "b", test_group_percent=.1)),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalParams(filename = "c", test_group_percent=.1)),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalParams(filename = "d", test_group_percent=.1)),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalParams(filename = "e", test_group_percent=.1)),
    Pipeline([
        load_pipeline,
        Basic,
        SaveFile,
    ], GlobalParams(filename = "f", test_group_percent=.1)),
]


for indx, pipeline in enumerate(pipelines):
    start_datetime = datetime.now()
    print(
        "Processing file: \033[92m%s (%d/%d)\033[0m" % (
            pipeline.global_params.filename,
            indx + 1,
            len(pipelines),
        ),
        flush=False,
    )
    print("Start at: %s" % start_datetime.strftime('%H:%M:%S'))
    
    pipeline.execute()

    end_datetime = datetime.now()
    print("End at: %s (%s)\n\n" % (end_datetime.strftime('%H:%M:%S'), str(end_datetime-start_datetime)))
