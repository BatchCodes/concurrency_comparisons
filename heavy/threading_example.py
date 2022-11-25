import threading

from utils import heavyTask

NUM_THREADS = 3


class MyThread (threading.Thread):
  def __init__(self, threadId, numOutputs):
    threading.Thread.__init__(self)
    self.threadId = threadId
    self.numOutputs = numOutputs

  def run(self):
    print(f"Starting Thread {self.threadId}")
    heavyTask(self.numOutputs, self.threadId)
    print(f"Exiting Thread {self.threadId}")
