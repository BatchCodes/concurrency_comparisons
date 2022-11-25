import threading
from time import sleep

from utils import generateSleepTime

NUM_OUTPUTS = 100


class MyThread (threading.Thread):
  def __init__(self, threadId):
    threading.Thread.__init__(self)
    self.threadId = threadId

  def run(self):
    print(f"Starting Thread {self.threadId}")
    sleep(generateSleepTime())
    print(f"Exiting Thread {self.threadId}")
