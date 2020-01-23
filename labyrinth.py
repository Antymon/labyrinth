import matplotlib.pyplot as plt
import numpy as np

# marker values; changing will result in different colors,
# don't assign same values to different markers, they are used in logic
UNKNOWN = 0
CLAIMED = 1
FORBIDDEN = 2


class Labyrinth(object):
    def __init__(self, width=40, height=40, start=(0, 0), straightness_factor=0.9):
        """
        Creates an instance of randomized labirynth

        @param width:
        @param height:
        @param start:
        @param straightness_factor:
        """
        self.straightness_factor = straightness_factor

        # set bounding frames, not to check boundary conditions later
        board = Labyrinth.get_padded_matrix((width, height), padding_value=FORBIDDEN)

        path = [start]
        x, y = start
        board[y, x] = CLAIMED

        self.board = board
        self.path = path

        while len(path) > 0:
            unused_cells = self.get_neighbors(UNKNOWN, path[-1])

            if len(unused_cells) == 0:
                # no options for exploration, backtracking
                path.pop()
            else:
                cell = self.cell_selector(unused_cells)
                x, y = cell
                if self.is_cell_valid(cell):
                    path.append(cell)
                    board[y, x] = CLAIMED
                else:
                    board[y, x] = FORBIDDEN

        # mark start as some different color
        x, y = start
        board[y, x] = 4

        print(board)

    @classmethod
    def get_padded_matrix(cls, shape, padding_value=1, padding_width=1):
        height, width = shape
        matrix = np.zeros((height + 2 * padding_width, width + 2 * padding_width), dtype=np.uint8)
        matrix[:, 0] = padding_value
        matrix[:, width + 1] = padding_value
        matrix[0, :] = padding_value
        matrix[height + 1, :] = padding_value
        return matrix

    def get_neighbors(self, filter_marker, cell, cross_on=True):
        x, y = cell

        result = []

        cross = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                 ]

        if not cross_on:
            cross += [(x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]

        for x, y in cross:
            if self.board[y, x] == filter_marker:
                result.append((x, y))

        return result

    def is_cell_valid(self, point):
        claimed = self.get_neighbors(CLAIMED, point)
        return len(claimed) == 1

    def cell_selector(self, cells):

        cells_count = len(cells)
        probs = None

        if len(self.path) > 1 and cells_count > 1:
            x2, y2 = self.path[-2]
            x1, y1 = self.path[-1]
            dx = x1 - x2
            dy = y1 - y2
            ahead = (x1 + dx, y1 + dy)

            if ahead in cells:
                i = cells.index(ahead)

                probs = (1. - self.straightness_factor) / (cells_count - 1)
                probs = np.ones(cells_count) * probs
                probs[i] = self.straightness_factor

        i = np.random.choice(np.arange(cells_count), 1, p=probs)[0]
        return cells[i]

    def print(self, filename=None):

        nrows, ncols = self.board.shape
        image = np.zeros(nrows * ncols)
        image[::] = self.board.flatten()
        image = image.reshape((nrows, ncols))

        plt.matshow(image)
        if filename is not None:
            plt.savefig(filename)

        else:
            plt.show()


        return image

import time

if __name__ == '__main__':
    size = 20
    x = np.random.randint(1, size)
    y = 1
    start = (x, y)
    l = Labyrinth(size, size, start, straightness_factor=0.1)
    l.print('maze_{}.png'.format(time.time()))
