from datetime import datetime


def timer(func):
  def funcWrapper(*args, **kwargs):
    startTime = datetime.now()
    returnValue = func(*args, **kwargs)
    endTime = datetime.now()
    duration = endTime - startTime
    print(f"\n\nTime Elapsed: {duration}\n\n")
    return returnValue or duration
  return funcWrapper
