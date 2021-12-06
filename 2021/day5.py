

class Coordinate:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2

        self.m = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else 0

        self.b = y2 - (self.m * x2)

        self.max_h, self.min_h = max(self.y1, self.y2), min(self.y1, self.y2)
        self.max_w, self.min_w = max(self.x1, self.x2), min(self.x1, self.x2)

    def __str__(self):
        return str((self.x1, self.y1, self.x2, self.y2))


class Drawing:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = {}
        for row in range(height + 1):
            for col in range(width + 1):
                self.board[str((row, col))] = 0

    # add a coordinate to our board
    def __add__(self, coord: Coordinate):
        max_w, min_w = coord.max_w, coord.min_w
        max_h, min_h = coord.max_h, coord.min_h
        width = max_w - min_w
        height = max_h - min_h

        for row in range(min_h, max_h + 1):
            for col in range(min_w, max_w + 1):
                # if straight line, or if coord is within slope of line
                if str((row, col)) in self.board and \
                        (width == 0 or height == 0
                         or coord.m * col + coord.b == row):
                    self.board[str((row, col))] += 1

                elif width == 0 or height == 0 \
                        or coord.m * col + coord.b == row:
                    self.board[str((row, col))] = 1

        return self

    # to help visualize how it turned out
    def print_board(self):
        printout = []
        for i in range(0, self.width + 1):
            line = ""
            for j in range(0, self.height + 1):
                if self.board[str((i, j))] == 0:
                    line += "."
                else:
                    line += str(self.board[str((i, j))])
            printout.append(line)

        return printout


class Solution:
    def __init__(self, inp):
        # parse
        input_unparsed = inp.split("\n")
        coordinates = []
        for line in input_unparsed:
            line = line.strip()
            if line:
                coordinates.append([[int(y) for y in x.split(",")]
                                    for x in line.split(" -> ")])

        # create coordinate objects
        self.coordinates = []
        max_w, min_w = -99999999, 100000000
        max_h, min_h = max_w, min_w

        for item in coordinates:
            x1, y1, x2, y2 = item[0][0], item[0][1], item[1][0], item[1][1]
            self.coordinates.append(Coordinate(x1, y1, x2, y2))
            max_h, min_h = max(max_h, y1, y2), min(min_h, y1, y2)
            max_w, min_w = max(max_w, x1, x2), min(min_w, x1, x2)

        self.drawing = Drawing(max_w - min_w, max_h - min_h)

    def find_overlapping_lines(self):
        for coord in self.coordinates:
            self.drawing += coord

        no_overlapping_lines = 0
        for key in self.drawing.board:
            if self.drawing.board[key] >= 2:
                no_overlapping_lines += 1

        return no_overlapping_lines


