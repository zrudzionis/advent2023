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
  map(lambda strNumbers: toInt(strNumbers),
      map(lambda line: re.split(r' +', line.strip()),
          map(lambda v: v.split(':')[1], inputData.splitlines())
      )
  )
)
Race = namedtuple('Race', 'time distance')
races = [Race(vals[0][i], vals[1][i]) for i in range(0, len(vals[0]))]


def main():
  rez = 1
  for race in races:
      count = 0
      for waitTime in range(0, race.time + 1):
         time = race.time - waitTime
         speed = waitTime
         distance = speed*time
         if distance > race.distance:
            count += 1
      rez *= count
  print(rez)

main()
