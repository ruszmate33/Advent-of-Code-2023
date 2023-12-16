import collections

SEED_TO_SOIL = (
"""50 98 2
52 50 48"""
)
# actually it is soil-seed-range

# seed 98 -> soil 50
# seed 99 -> soil 51

# seed 50 -> soil 52
# ...
# seed 97 -> soil 99

# numbers not in the mapping map to themselfs
# 10 -> 10

# the closest location with seeds: 79 14 55 13 is 35 (seed 13 -> 35 location)

# closest_location=218513636

# part 2 232257988 is wrong
# 81956384 is the right answer, from range 8

TEST_INPUT = (
"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
)


def get_list_nums_ranges(puzzle_input):
    list_nums_ranges = puzzle_input.split('\n')[1:]
    return list_nums_ranges

def build_map(num_num_range: list[str]):
    d = DefaultToSameValueDict()
    # print(f'{num_num_range=}')
    for el in num_num_range:
        el = el.split(' ')
        # print(f'{el=}')
        for i in range(int(el[2])):
            d[int(el[1]) + i] = int(el[0]) + i
    return d

def build_map_from_input(puzzle_input):
    return build_map(get_list_nums_ranges(puzzle_input))

def main():
    with open('input5.txt') as f:
        puzzle_input = f.read().split('\n\n')
        # puzzle_input = TEST_INPUT.split('\n\n')
        # print(f'{puzzle_input=}')
        # puzzle_input=['seeds: 79 14 55 13', 'seed-to-soil map:\n50 98 2\n52 50 48', 'soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15', 'fertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4', 'water-to-light map:\n88 18 7\n18 25 70', 'light-to-temperature map:\n45 77 23\n81 45 19\n68 64 13', 'temperature-to-humidity map:\n0 69 1\n1 0 69', 'humidity-to-location map:\n60 56 37\n56 93 4']


        seed_input = [int(seed) for seed in puzzle_input[0].split(' ')[1:] if seed]
        seed_ranges = []
        for seed_start, seed_length in zip(seed_input[::2], seed_input[1::2]):
            # print(f'{seed_start=}, {seed_length=}')
            seed_ranges.append(range(seed_start, seed_start + seed_length))
        print(f'{seed_input=}')
        print(f'{seed_ranges=}')
        print('seed_input: done')
        
        def create_function(puzzle_input, name):
            # 50 98 2
            # 52 50 48
            func_body_str = f"def get_{name}(stuff: int) -> int:\n"
            list_nums_ranges = get_list_nums_ranges(puzzle_input)
            el = list_nums_ranges[0]
            el = el.split(' ')
            func_body_str += f'    if stuff in range({el[1]}, {el[1]} + {el[2]}):\n'
            func_body_str += f'        return stuff + ({el[0]} - {el[1]})\n'

            for el in list_nums_ranges[1:]:
                el = el.split(' ')
                func_body_str += f'    elif stuff in range({el[1]}, {el[1]} + {el[2]}):\n'
                func_body_str += f'        return stuff + ({el[0]} - {el[1]})\n'
            func_body_str += '    return stuff\n'
            exec(func_body_str, globals())




        create_function(puzzle_input[1], 'soil')
        create_function(puzzle_input[2], 'fertilizer')
        create_function(puzzle_input[3], 'water')
        create_function(puzzle_input[4], 'light')
        create_function(puzzle_input[5], 'temp')
        create_function(puzzle_input[6], 'hum')
        create_function(puzzle_input[7], 'location')



        # def seeds_to_locations(seeds):
        #     return [get_location(get_hum(get_temp(get_light(get_water(get_fertilizer(get_soil(seed))))))) for seed in seeds]

        def seed_to_location(seed):
            return get_location(get_hum(get_temp(get_light(get_water(get_fertilizer(get_soil(seed)))))))


        # seed_to_loc = {}
        min_location = None
        for i, seed_range in enumerate(seed_ranges):
            # print(f'{seed_range=}')
            for seed in seed_range:
                # print(f'{seed=}')
                # if seed in seed_to_loc:
                #     continue
                location = seed_to_location(seed)
                # seed_to_loc[seed] = location
                if min_location is None:
                    min_location = location
                if location < min_location:
                    min_location = location
            print(f'range {i} finished, min so far {min_location}')
        print(f'{min_location=}')

        # seeds_to_locations = seeds_to_locations(seed_input)
        # print('seeds_to_locations calculated')
        # closest_location = min(seeds_to_locations)
        # print(f'{closest_location=}')
        

if __name__ == '__main__':
    main()