from typing import List
from datetime import datetime
from pipeline.pipeline_processes.pipeline_process_interface import PipelineProcessInterface
from pipeline.global_params import GlobalParams

class Pipeline:
    def __init__(
        self,
        processes: List[PipelineProcessInterface],
        global_params: GlobalParams,
        disjunctive: bool = False
    ):
        self.processes = processes
        self.global_params = global_params
        self.disjunctive = disjunctive
    
    def execute(self):
        for algorithm in self.processes:
            try:
                if isinstance(algorithm, SubPipeline):
                    sub_pipeline = Pipeline(algorithm.processes, self.global_params, algorithm.disjunctive)
                    sub_pipeline.execute()
                else:
                    print("\033[96m%s\033[0m" % algorithm, end='')
                    start_datetime = datetime.now()
                    print(" => \033[34m%s" % start_datetime.strftime('%H:%M:%S'), end='')
                    algorithm.execute(self.global_params)
                    end_datetime = datetime.now()
                    print(" - %s (%s)\033[0m" % (end_datetime.strftime('%H:%M:%S'), str(end_datetime-start_datetime)), flush=True)
                
                if self.disjunctive:
                    return
            
            except Exception as exception:
                if not self.disjunctive:
                    raise exception
        
        if self.disjunctive:
            raise Exception('No complete any process')


class SubPipeline:
    def __init__(
        self,
        processes: List[PipelineProcessInterface],
        disjunctive: bool = False
    ):
        self.processes = processes
        self.disjunctive = disjunctive

        
