import time
import datetime

def getCompileTime():
  start = time.time()
  end = time.time()

  sec = (end - start)
  result = datetime.timedelta(seconds=sec)
  print(result)

  result_list = str(datetime.timedelta(seconds=sec)).split(".")
  print(result_list[0])

