from random import random

MIN_SLEEP_TIME = 1
MAX_SLEEP_TIME = 4


def generateSleepTime(minSleep=MIN_SLEEP_TIME, maxSleep=MAX_SLEEP_TIME):
  sleepTime = minSleep + (maxSleep - minSleep)*random()
  return sleepTime
