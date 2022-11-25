import multiprocessing

from utils import heavyTask


class MyProcess(multiprocessing.Process):
  def __init__(self, processId, numOutputs):
    multiprocessing.Process.__init__(self)
    self.processId = processId
    self.numOutputs = numOutputs

  def run(self):
    print(f"Starting Process {self.processId}")
    heavyTask(self.numOutputs, self.processId)
    print(f"Exiting Process {self.processId}")
