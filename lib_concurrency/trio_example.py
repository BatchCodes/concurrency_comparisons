import trio

from timer import timer
from utils import generateSleepTime

NUM_CHILDREN = 300


class Child:
  def __init__(self, childId):
    self.childId = childId

  async def __call__(self):
    print(f"  Child {self.childId} started! sleeping now...")
    await trio.sleep(generateSleepTime())
    print(f"  Child {self.childId}: exiting!")


async def parent(childList):
  async with trio.open_nursery() as nursery:
    for child in childList:

      print(f"Parent Starting Child {child.childId}")
      nursery.start_soon(child)

    print("Parent waiting for children to finish")

  print("Parent: Children finished")


@timer
def main():
  childList = [
      Child(childId) for childId in range(NUM_CHILDREN)
  ]

  trio.run(parent, childList)


if __name__ == "__main__":
  print(f"Total time = {main()}")
