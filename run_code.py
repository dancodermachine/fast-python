from random import random
from time import sleep
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, TimeoutError, wait, as_completed, FIRST_COMPLETED, FIRST_EXCEPTION 

# custom function executed by a worker process
def task(number):
    # block for a fraction of a second
    sleep(random())
    # return task number
    return number

# protect the entry point
if __name__ == "__main__":
    # start the process pool
    with ProcessPoolExecutor(10) as exe:
        # submit tasks and collect futures 
        futs = [exe.submit(task, i) for i in range(10)]
        # handle task results as they are completed
        for future in as_completed(futs):
            # retrieve the result
            result = future.result()
            # report the result
            print(f"> result for task {result}")