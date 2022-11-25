import asyncio

from timer import timer
from utils import generateSleepTime

NUM_CHILDREN = 300


class Child:
  def __init__(self, childId):
    self.childId = childId

  async def __call__(self):
    print(f"  Child {self.childId} started! sleeping now...")
    await asyncio.sleep(generateSleepTime())
    print(f"  Child {self.childId}: exiting!")


def parent(childList):
  print("Parent: starting Children")
  loop = asyncio.get_event_loop()
  tasks = asyncio.gather(*[child() for child in childList])
  loop.run_until_complete(tasks)
  print("Parent: Children finished")


@timer
def main():
  childList = [
      Child(childId) for childId in range(NUM_CHILDREN)
  ]

  parent(childList)


if __name__ == "__main__":
  print(f"Total time = {main()}")
