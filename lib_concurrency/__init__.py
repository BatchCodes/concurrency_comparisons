from asyncio_example import main as asyncio_main
from asyncio_gather_example import main as asyncio_gather_main
from trio_example import main as trio_main

if __name__ == "__main__":
  asyncio_time = asyncio_main()
  asyncio_gather_time = asyncio_gather_main()
  trio_time = trio_main()
  print(f"asyncio time = {asyncio_time}")
  print(f"asyncio gather time = {asyncio_gather_time}")
  print(f"trio time = {trio_time}")
