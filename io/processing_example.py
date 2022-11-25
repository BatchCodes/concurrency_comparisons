import multiprocessing
from time import sleep

from utils import generateSleepTime

NUM_OUTPUTS = 100


class MyProcess(multiprocessing.Process):
  def __init__(self, processId):
    multiprocessing.Process.__init__(self)
    self.processId = processId

  def run(self):
    print(f"Starting Process {self.processId}")
    sleep(generateSleepTime())
    print(f"Exiting Process {self.processId}")
