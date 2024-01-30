from collections import defaultdict
import itertools


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


def main():
    with open('input8.txt') as f:
        puzzle_input = f.read()
        instructions = puzzle_input.split('\n')[0]
        # print(f'{instructions=}')
        nodes = puzzle_input.split('\n')[2:]
        # print(f'{nodes=}')
        node_map = process_nodes(nodes)
        # print(f'{node_map=}')
        traverse_nodes(instructions, node_map)


if __name__ == '__main__':
    main()
