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

class DefaultToSameValueDict(collections.defaultdict):
    def __missing__(self, key: int) -> int:
        return key

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
    # puzzle_input = TEST_INPUT.split('\n\n')
    with open('input5.txt') as f:
        # puzzle_input = [line.strip() for line in f.readlines()]
        puzzle_input = f.read().split('\n\n')
        # print(f'{puzzle_input=}')
        # puzzle_input=['seeds: 79 14 55 13', 'seed-to-soil map:\n50 98 2\n52 50 48', 'soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15', 'fertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4', 'water-to-light map:\n88 18 7\n18 25 70', 'light-to-temperature map:\n45 77 23\n81 45 19\n68 64 13', 'temperature-to-humidity map:\n0 69 1\n1 0 69', 'humidity-to-location map:\n60 56 37\n56 93 4']


        seed_input = [int(seed) for seed in puzzle_input[0].split(' ')[1:] if seed]
        print('seed_input: done')
        # print(f'{seed_input=}')

        seed_to_soil = build_map_from_input(puzzle_input[1])
        print('seed_to_soil: done')
        print(f'{seed_to_soil=}')

        soil_to_fertilizer = build_map_from_input(puzzle_input[2])
        print('soil_to_fertilizer: done')

        fertilizer_to_water = build_map_from_input(puzzle_input[3])
        print('fertilizer_to_water: done')

        water_to_light = build_map_from_input(puzzle_input[4])
        print('water_to_light: done')


        light_to_temp = build_map_from_input(puzzle_input[5])
        print('light_to_temp: done')


        tempt_to_hum = build_map_from_input(puzzle_input[6])
        print('tempt_to_hum: done')


        hum_to_location = build_map_from_input(puzzle_input[7])
        print('hum_to_location: done')



        def seeds_to_locations(seeds):
            # return {seed: 
            # hum_to_location[tempt_to_hum[light_to_temp[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed]]]]]]] for seed in seeds}
            for seed in seeds:
                yield hum_to_location[tempt_to_hum[light_to_temp[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed]]]]]]]

        seeds_to_locations = seeds_to_locations(seed_input)
        print('seeds_to_locations calculated')
        closest_location = min(seeds_to_locations)
        print(f'{closest_location=}')
        
        # for seed, location in seeds_to_locations.items():
        #     if location == closest_location:
        #         print(f'{seed=}, closesest {location=}')

    # print(f'{hum_to_location[tempt_to_hum[light_to_temp[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed_input[-1]]]]]]]]}')
    
if __name__ == '__main__':
    main()