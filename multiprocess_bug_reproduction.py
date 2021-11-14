"""
A small script reproducing a bug in ClearML with multiprocessing.
"""
from clearml import Task
from multiprocess_minimal import run as mp_min_run
import time

if __name__ == "__main__":
    task = Task.init(project_name='ClearML Debugging',
                     task_name='Multiprocess debugging',
                     task_type=Task.TaskTypes.custom)

    print('Script start')
    mp_min_run()
    print('Script end')
    task.close()
