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


async def parent(childList):
  print("Parent: starting Children")
  tasks = [
      asyncio.create_task(child()) for child in childList
  ]
  for task in tasks:
    await task
  print("Parent: Children finished")


@timer
def main():
  childList = [
      Child(childId) for childId in range(NUM_CHILDREN)
  ]

  asyncio.run(parent(childList))


if __name__ == "__main__":
  print(f"Total time = {main()}")
