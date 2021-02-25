from concurrent.futures import ThreadPoolExecutor 
from pipeline.algorithms.pipeline_algorithm_interface import PipelineAlgorithmInterface
from pipeline.algorithms.load_file import LoadFile
from pipeline.global_algoritm_params import GlobalAlgoritmParams

class EncodeData(PipelineAlgorithmInterface):
    @classmethod
    def execute(cls, global_params: GlobalAlgoritmParams):
        number_of_threads = global_params.number_of_threads
        input_array = global_params.data_to_process
        global_params.data_without_encode = global_params.data_to_process[:LoadFile.FIRST_ROW_OF_ELEMENT]
        
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

        global_params.data_to_process = results

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