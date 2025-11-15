from time import sleep
from random import random
from multiprocessing import (
    Process,
    current_process,
    parent_process,
    active_children,
    Lock,
    Semaphore,
    Event,
    Condition,
    Barrier,
    set_start_method,
    Value,
    Pipe,
    Queue,
    Manager,
    Pool
) 

# custom function to be executed in a child process
def task(shared_barrier, ident):
    # generate a unique value between 0 and 10
    value = random() * 10
    # block for a moment
    sleep(value)
    # report result
    print(f"Process {ident} got: {value}", flush=True)
    # wait for all other processes to complete
    shared_barrier.wait()
    
# protect the entry point
if __name__ == "__main__":
    # create a barrier for (5 workers + 1 main process)
    barrier = Barrier(5 + 1)
    # create the worker processes
    workers = [Process(target=task, args=(barrier, i)) for i in range(5)]
    # start the worker processes
    for worker in workers:
        # start process
        worker.start()
    # wait for all worker processes to finish
    print("Main process waiting on all results...")
    barrier.wait()
    # report once all processes are done
    print("All processes have their results")