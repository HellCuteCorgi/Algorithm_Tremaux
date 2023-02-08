import random
from walker_base import WalkerBase

FOUND_COLOR = 'red'
VISITED_COLOR = 'gray70'


class Tremaux(WalkerBase):
    class Node(object):
        __slots__ = 'passages'

        def __init__(self):
            self.passages = set()

    def __init__(self, maze):
        super(Tremaux, self).__init__(maze, maze.start(), self.Node())
        self._maze.clean()
        self._last = None  # Заполнитель на потом

    def _is_junction(self, cell):
        return cell.count_halls() > 2

    def _is_visited(self, cell):
        return len(self.read_map(cell).passages) > 0

    def _backtracking(self, cell, last):
        return last in self.read_map(cell).passages

    def step(self):
        # This is so profoundly ugly

        if self._cell is self._maze.finish():
            self._isDone = True
            self.paint(self._cell, FOUND_COLOR)
            return

        # Напечатать self._cell.get_position()
        paths = self._cell.get_paths(last=self._last)
        # print paths
        random.shuffle(paths)

        if self._is_visited(self._cell):
            # Мы были здесь раньше
            if self._backtracking(self._cell, self._last):
                # Мы возвращаемся назад; посмотреть, есть ли непройденные пути
                unvisited = filter(lambda c: not self._is_visited(c), paths)
                if len(unvisited) > 0:
                    self._last = self._cell
                    self._cell = unvisited.pop()
                else:
                    # Непройденных путей нет, продолжаем возвращаться
                    self.paint(self._cell, VISITED_COLOR)
                    # Find the path back
                    passages = self.read_map(self._cell).passages
                    unvisited = set(self._cell.get_paths()).difference(passages)
                    self._last = self._cell
                    self._cell = unvisited.pop()
            else:
                # Мы зациклились на ранее посещенной ячейке; повернись
                self._cell, self._last = self._last, self._cell
        else:
            # Новая ячейка; двигаться беспорядочно
            if len(paths) > 0:
                # Не тупик
                self.paint(self._cell, FOUND_COLOR)
                self._last = self._cell
                self._cell = paths.pop()
            else:
                # Это тупик; вернуться
                self.paint(self._cell, VISITED_COLOR)
                self._cell, self._last = self._last, self._cell

        self.read_map(self._last).passages.add(self._cell)