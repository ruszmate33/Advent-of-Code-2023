from collections import defaultdict
import itertools
import time
import math


# 2 steps
TEST_INPUT_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

# 6 steps, 2 full cycles
TEST_INPUT_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# first part steps=15989 is the good answer!

# for part 2
TEST_INPUT_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def process_nodes(nodes):
    # type_hand_bid: dict[list[tuple[str]]] = defaultdict(list)

    # node_with_left_right: dict = defaultdict[dict]
    node_with_left_right = {}
    for node in nodes:
        key, left_right = node.split(' = ')
        left, right = left_right.strip('()').split(', ')
        # print(f'{key=}, {left, right}')
        if key not in node_with_left_right:
            node_with_left_right[key] = {}
        node_with_left_right[key]['L'] = left
        node_with_left_right[key]['R'] = right
    return node_with_left_right


def traverse_nodes(instructions, node_map):
    instructions = itertools.cycle(instructions)
    node = node_map['AAA']
    steps = 0
    # print(f'first node {node}')
    for inst in instructions:
        steps += 1
        node_key = node[inst]
        if node_key == 'ZZZ':
            print(f'{steps=}')
            break
        node = node_map[node_key]
        print(f'{node=}')


def traverse_multiple_nodes(instructions, node_map, start_node_keys):
    steps = 0
    ind_to_current_keys = {ind: key for ind, key in enumerate(start_node_keys)}
    instructions = itertools.cycle(instructions)
    t0 = time.time()
    for inst in instructions:
        # 10_668_805_667_831
        if steps == 100_000_000_000_000:
            print(f'{steps=}')
            break
        if steps % 10_000_000 == 0:
            print(f'{steps=}')
            print(f'{ind_to_current_keys=}')
            duration = time.time() - t0
            print(f'Time it took {round(duration, 1)} seconds')
            print(f'avg time/step {round(steps/duration)}')
            if steps != 0 and duration != 0:
                print(
                    f'projected {round(10_668_805_667_831 / (steps/duration)) / (60 * 60), 1} hours'
                )
            print('-----')

        # print(f'{ind_to_current_keys=}')
        # print(f'{inst=}')
        for ind, node_key in ind_to_current_keys.items():
            node = node_map[node_key]
            new_node_key = node[inst]
            ind_to_current_keys[ind] = new_node_key
        steps += 1
        # print(f'{ind_to_current_keys=}')
        if all(node_key[-1] == 'Z' for node_key in ind_to_current_keys.values()):
            print(f'{steps=}')
            break

# 13830919117339 is the right answer yuhuu!!!
def get_least_steps_to_z(instructions, node_map, node_key):
    steps = 0
    # ind_to_current_keys = {ind: key for ind, key in enumerate(start_node_keys)}
    instructions = itertools.cycle(instructions)

    for inst in instructions:

        # print(f'{ind_to_current_keys=}')
        # print(f'{inst=}')
        # for ind, node_key in ind_to_current_keys.items():
        node = node_map[node_key]
        node_key = node[inst]
        steps += 1
        # print(f'{ind_to_current_keys=}')
        if node_key[-1] == 'Z':
            print(f'{steps=}')
            return steps


def main():
    with open('input8.txt') as f:
        puzzle_input = f.read()
        # puzzle_input = TEST_INPUT_3
        instructions = puzzle_input.split('\n')[0]
        print(f'{instructions=}')
        nodes = puzzle_input.split('\n')[2:]
        # print(f'{nodes=}')
        node_map = process_nodes(nodes)
        print(f'{node_map=}')
        start_node_keys = [n for n in node_map if n[-1] == 'A']
        print(f'{start_node_keys=}')
        start_key_to_least_distance_to_z = {}
        for key in start_node_keys:
            steps_to_z = get_least_steps_to_z(instructions, node_map, key)
            print(f'{key}: {steps_to_z}')
            start_key_to_least_distance_to_z[key] = steps_to_z
        print(math.lcm(*start_key_to_least_distance_to_z.values()))


if __name__ == '__main__':
    main()
