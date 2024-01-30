TEST_INPUT_1 = """.....
.S-7.
.|.|.
.L-J.
....."""

TEST_INPUT_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

SYMBOLS_LAST_STEPS_TO_NEXT_STEPS = {
    # row, col coordinate
    '|': {(-1, 0): (-1, 0), (1, 0): (1, 0)},
    '-': {(0, 1): (0, 1), (0, -1): (0, -1)},
    'L': {(1, 0): (0, 1), (0, -1): (-1, 0)},
    'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
    '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
    'F': {(-1, 0): (0, 1), (0, -1): (1, 0)},
    '.': {},
}

START_SYMBOL = 'S'

# class Board:
#      def __init__(self, )


def get_start(board) -> list[tuple[int]]:
    for i, line in enumerate(board.split('\n')):
        for j, char in enumerate(list(line)):
            # print(f'{char=}')
            if char != START_SYMBOL:
                continue
            return i, j


def create_board(input: str) -> dict[tuple[int], str]:
    coordinates_symbols = {}
    for i, line in enumerate(input.split('\n')):
        for j, symbol in enumerate(list(line)):
            coordinates_symbols[i, j] = symbol
    return coordinates_symbols


def get_connections_to_start_with_next_steps(
    coordinates_symbols: dict[tuple[int], str], start: tuple[int]
) -> list[tuple[int]]:
    positions_last_step = []
    print(f'{start=}')
    start_row, start_col = start
    for move_row in (-1, 0, 1):
        for move_col in (-1, 0, 1):
            if (move_row, move_col) == (0, 0):
                continue
            step = (move_row, move_col)
            position_to_check = (start_row + move_row, start_col + move_col)
            try:
                symbol = coordinates_symbols[position_to_check]
            except KeyError:
                continue
            allowed_steps_next_steps = SYMBOLS_LAST_STEPS_TO_NEXT_STEPS[symbol]
            if step not in allowed_steps_next_steps:
                continue
            next_step = allowed_steps_next_steps[step]
            positions_last_step.append((position_to_check, next_step))
            print(f'{step=}, {position_to_check=}, {symbol=}, {next_step=}')
    return positions_last_step


def traverse_until_start(start: tuple[int, int], position: tuple[int, int], last_step: tuple[int], coordinates_symbols, steps) -> tuple[tuple[int, int]]:
    steps += 1
    if steps > 10_000:
        return
    if position == start:
        print(round(steps / 2))
        return
    symbol = coordinates_symbols[position]
    print('------------')
    print(f'{symbol=} {last_step=}')
    try:
        step = SYMBOLS_LAST_STEPS_TO_NEXT_STEPS[symbol][last_step]
    except KeyError as e:
        print(f'{symbol=} {last_step=}')
        raise e
    next_position = tuple(map(sum, zip(position, step)))
    print(f'{next_position=} {step=}')
    print('------------')
    return traverse_until_start(start, next_position, step, coordinates_symbols, steps)


def get_next_position_last_step(position, last_step: tuple[int], coordinates_symbols):
    symbol = coordinates_symbols[position]
    # print('------------')
    # print(f'{symbol=} {last_step=}')
    try:
        step = SYMBOLS_LAST_STEPS_TO_NEXT_STEPS[symbol][last_step]
    except KeyError as e:
        print(f'{symbol=} {last_step=}')
        raise e
    next_position = tuple(map(sum, zip(position, step)))
    # print(f'{next_position=} {step=}')
    # print('------------')
    return next_position, step



def main():
    with open('input10.txt') as f:
        puzzle_input = f.read()
        # print(TEST_INPUT_2)
        board = create_board(puzzle_input)
        start = get_start(puzzle_input)
        connections_to_start_with_next_steps = get_connections_to_start_with_next_steps(board, start)
        print(f'{start=}')
        # print(f'{board=}')
        # print(f'{connections_to_start_with_next_steps=}')
        for direction in connections_to_start_with_next_steps:
            steps = 1
            position, next_step = direction
            position_row, position_col = position
            step_row, step_col = next_step
            current_position = (position_row + step_row, position_col + step_col)
            last_step = next_step
            steps += 1
            # traverse_until_start(start, current_position, last_step, board, 1)
            while current_position != start:
                current_position, last_step = get_next_position_last_step(current_position, last_step, board)
                steps += 1
            print(f'{start=} {steps / 2=}')
        # 6946 too low
        # 6947 is the right answer


if __name__ == '__main__':
    main()
