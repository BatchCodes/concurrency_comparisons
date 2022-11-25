import os

FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "output.txt"
)


def heavyTask(max, taskId=0):
  for i in range(max):
    for j in range(i):
      for k in range(j):
        outputString = f"{taskId=} {i=} {j=} {k=}\n"
        with open(FILE_PATH, "a+") as file:
          file.write(outputString)


if __name__ == "__main__":
  heavyTask(100)
