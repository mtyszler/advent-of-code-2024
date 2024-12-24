def parse_input(filename: str) -> list[list]:
    input_file = open(filename, 'r')
    matrix = [list(line.strip()) for line in input_file if line.strip()]
    return matrix


def find_word(matrix: list[list], word: str) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    def is_valid(x, y, dx, dy):
        # Check if the word can fit starting from (x, y) in direction (dx, dy)
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or matrix[nx][ny] != word[i]:
                return False
        return True

    total = 0

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if is_valid(r, c, dx, dy):
                    # return True, (r, c), (dx, dy)  # Found the word with its direction
                    total += 1

    return total


def find_x_word(matrix: list[list], word: str) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)
    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    cross = {
        (-1, -1): [{'shift': (-2, 0), 'direction': (1, -1)}, {'shift': (0, -2), 'direction': (-1, 1)}],
        (1, 1): [{'shift': (2, 0), 'direction': (-1, 1)}, {'shift': (0, 2), 'direction': (1, -1)}],
        (-1, 1): [{'shift': (-2, 0), 'direction': (1, 1)}, {'shift': (0, 2), 'direction': (-1, -1)}],
        (1, -1): [{'shift': (2, 0), 'direction': (-1, -1)}, {'shift': (0, -2), 'direction': (1, 1)}]
    }

    def is_valid(x, y, dx, dy):
        # Check if the word can fit starting from (x, y) in direction (dx, dy)
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or matrix[nx][ny] != word[i]:
                return False
        return True

    total = 0

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if is_valid(r, c, dx, dy):
                    # return True, (r, c), (dx, dy)  # Found the word with its direction
                    for cr in cross[(dx, dy)]:
                        wx, wy = cr['shift']
                        rr = r + wx
                        cc = c + wy
                        ddx, ddy = cr['direction']
                        if is_valid(rr, cc, ddx, ddy):
                            # print(r,c)
                            total += 1

    return total/2
