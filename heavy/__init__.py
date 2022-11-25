from processing_example import MyProcess
from threading_example import MyThread
from timer import timer

NUM_TASKS = 3
NUM_OUTPUTS = 100


@timer
def main(
    ConcurrencyClass,
    numTasks=NUM_TASKS,
    numOutputs=NUM_OUTPUTS
):

  tasks = [
      ConcurrencyClass(taskId, numOutputs)
      for taskId in range(numTasks)
  ]

  for task in tasks:
    task.start()

  for task in tasks:
    task.join()


if __name__ == "__main__":
  processesTime = main(MyProcess)
  # threadingTime = main(MyThread)
  # print(
  #     f"\nProcessing Time: {processesTime}\nThreading Time: {threadingTime}"
  # )
