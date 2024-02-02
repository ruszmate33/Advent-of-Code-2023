# cubes RGB
# - Each time you play this game,
# he will hide a secret number of cubes of each color in the bag
# - your goal is to figure out information about the number of cubes

# To get information,
# once a bag has been loaded with cubes,
# the Elf will reach into
# the bag, grab a handful of random cubes, show them to you,
# and then put them back in the bag.
# He'll do this a few times per game.

import math

file_path = "../inputs/input2.txt"

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# part1 puzzle input solution 2085
# TEST_INPUT with part1 is 8

# part2 puzzle input solution 79315
# TEST_INPUT with part1 is 2286

POSSIBLE_CUBES = {"red": 12, "green": 13, "blue": 14}


def process_game_sets(line: str) -> list[str]:
    line = line.strip()
    sets = line.split(": ")[1].split("; ")
    return [s.split(", ") for s in sets]


def valid_draw(draw, possible_cubes: dict[str, int]):
    num, color = draw.split(" ")
    if int(num) > possible_cubes[color]:
        return False
    return True


def get_minimum_set(sets):
    minimum_set = {}
    for draws in sets:
        for draw in draws:
            num, color = draw.split(" ")
            num = int(num)
            if minimum_set.get(color, 0) < num:
                minimum_set[color] = num
    return minimum_set


def sum_of_products_minimum_sets(lines: list[str]) -> int:
    sum_of_prods = 0
    for line in lines:
        game_sets = process_game_sets(line)
        minimum_set = get_minimum_set(game_sets)
        sum_of_prods += math.prod(list(minimum_set.values()))
    return sum_of_prods


def sum_of_valid_game_ids(
    lines: list[str], possible_cubes: dict[str, int]
) -> int:
    valid_game_ids = []
    for line in lines:
        game_id = line.split(": ")[0].split(" ")[1]
        game_sets = process_game_sets(line)
        if all(
            valid_draw(draw, possible_cubes)
            for draws in game_sets
            for draw in draws
        ):
            valid_game_ids.append(int(game_id))
    return sum(valid_game_ids)


def main():
    with open(file_path) as f:
        lines = f.readlines()
        # lines = TEST_INPUT.split('\n')
        print(
            f"part 1"
            f"{sum_of_valid_game_ids(lines, possible_cubes=POSSIBLE_CUBES)=}"
        )
        print(f"part 2 {sum_of_products_minimum_sets(lines)=}")


if __name__ == "__main__":
    main()
