import sys

DELAY = 5   # Миллисекунды.

CELL_SIZE = 10      # Пикселей.
# Включает пространство для стен, поэтому в конечном счете вычтите 2.

XCELLS = 50
YCELLS = 50
MAZE_HEIGHT = YCELLS * CELL_SIZE + 1
MAZE_WIDTH = XCELLS * CELL_SIZE + 1
if XCELLS * YCELLS > sys.getrecursionlimit():
    sys.setrecursionlimit(XCELLS * YCELLS)

# Цвета
NULL_FILL = 'black'
PLAN_FILL = 'grey'
OPEN_FILL = 'white'
DOT_COLORS = ['green', 'red']   # start dot, finish dot

# Помощники
DIRECTIONS = ['north', 'east', 'south', 'west']
OPPOSITES = {'north': 'south', 'east': 'west', 'south': 'north', \
             'west': 'east'}