from collections import namedtuple
from pprint import pprint as pp
import re

input = """Time:        60     80     86     76
Distance:   601   1163   1559   1300"""

a = """Time:      7  15   30
Distance:  9  40  200"""

inputData = input
toInt = lambda x: list(map(int, x))
vals = list(
  map(lambda strNumbers: int(strNumbers),
          map(lambda v: v.split(':')[1].strip().replace(' ', ''), inputData.splitlines())
  )
)
Race = namedtuple('Race', 'time distance')
race = Race(vals[0], vals[1])


def main():
  count = 0
  for waitTime in range(0, race.time + 1):
      time = race.time - waitTime
      speed = waitTime
      distance = speed*time
      if distance > race.distance:
        count += 1
  print(count)

main()
