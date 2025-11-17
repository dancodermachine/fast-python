from random import random
from time import sleep
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, TimeoutError, wait, as_completed, FIRST_COMPLETED, FIRST_EXCEPTION 

# custom function to be executed in a worker process
def task(number):
    # report a message
    print(f"Worker task {number}...", flush=True)
    # block for a moment
    sleep(1)
    
# initialize a worker in a process pool
def init():
    # report a message
    print("Initializing worker ...", flush=True)
    
# protect the entry point
if __name__ == "__main__":
    # create and configure the process pool
    with ProcessPoolExecutor(2, initializer=init) as exe:
        # issue tasks to the process pool
        _ = exe.map(task, range(4))
    