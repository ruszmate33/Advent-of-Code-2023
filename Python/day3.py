# 4361
TEST_INPUT = (
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
)

# 4462
TEST_INPUT_2 = (
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
..........
........+.
.........1
..........
.......100
.........*
1........."""
)

num_to_record={(1, range(21, 24)): 688, 
               (1, range(76, 78)): 95, 
               (1, range(79, 82)): 728, 
               (1, range(92, 95)): 896, 
               (1, range(119, 122)): 153, 
               (2, range(3, 6)): 122, 
               (2, range(62, 65)): 509, 
               (3, range(22, 25)): 698, 
               (3, range(27, 30)): 373, 
               (3, range(31, 34)): 992, 
               (3, range(66, 69)): 781, 
               (3, range(99, 102)): 399, 
               (3, range(129, 132)): 266}
6700


TEST_INPUT_3 = (
"""..............423....688..934............970................................95.728..........896...113..................153..972.............
...122..................*.....*..........................919..509*..........&...@.........../...........................+.......*...........
....+..........259....698..373.992.52.674.........................781...22........130.584.....-...%399.......777.................266........"""
)

TEST_INPUT_4 = (
"""..........................43.......*..............$.......-.....998...106.......=.......486*....&.......+......................982..........
.554......................*.......50.231.........409..............+...$.....*........72.....716.........51..445.....*284........*........350
.........425............*.94..836......&..............#516..............775.701.....*............................744..........541......-...."""
)

TEST_INPUT_5 = (
"""350...
...x..
......
...350
.x....
"""
)

TEST_INPUT_6 = (
"""350....
...x...
.......
...350.
.x.....
"""
)

def get_symbol_coordinates(lines):
    symbol_coordinates = []
    for i, line in enumerate(lines):
        line = line.strip()
        print(f'{i} {line}')
        for j, char in enumerate(line):
            if char.isdigit() or char == '.':
                continue
            # print(f'{i}-{j} {char}')
            symbol_coordinates.append((i, j))
    return symbol_coordinates

def get_nums_coordinates(lines):
    nums_coordinates = {}
    for i, line in enumerate(lines):
        line = line.strip()
        # print(f'{i} {line}')
        num = ''
        for j, char in enumerate(line):
            if not char.isdigit():
                if num:
                    nums_coordinates[(i, range(j-len(num), j))] = int(num)
                    num = ''
                continue
            num += char
            # end of line
            if j == len(line) - 1:
                if char.isdigit() and num:
                    nums_coordinates[(i, range(j-len(num)+1, j))] = int(num)
                    num = ''    


    return nums_coordinates

def is_adjacent(symbol_coord, num_coord):
    # is_adjacent(symbol_coord=(2, 3), num_coord=(1, range(0,3))
    # print(f'{symbol_coord[0]=}')
    # print(f'{num_coord[0]=}')

    # (2, range(136, 139)) v=350
    # (3, 135)

    # symbol_coordinates=[(1, 35), (1, 50), (1, 58), (1, 80), (1, 91), (1, 96), (1, 104), (2, 26), (2, 66), (2, 70), (2, 76), (2, 116), (2, 128), (3, 24), (3, 39), (3, 54), (3, 84), (3, 135)]
    if num_coord == (1, range(136, 139)):
        print('debug')
    
    if (
        symbol_coord[0] - 1 == num_coord[0] or
        symbol_coord[0] == num_coord[0] or
        symbol_coord[0] + 1 == num_coord[0]
    ) and (
        symbol_coord[1] - 1 in num_coord[1] or
        symbol_coord[1] in num_coord[1] or
        symbol_coord[1] + 1 in num_coord[1]
    ):
        if num_coord == (1, range(136, 139)):
            print(f'debug: True {symbol_coord=}')
        return True
    return False



def main():
    # lines = TEST_INPUT_5.split('\n')
    with open('input3.txt') as f:
        lines = f.readlines()
        # print(lines)
        symbol_coordinates = get_symbol_coordinates(lines)
        print(f'{symbol_coordinates=}')
        nums_coordinates = get_nums_coordinates(lines)
        print(f'{nums_coordinates=}')
        
        num_to_record = {}
        # print(nums_coordinates)
        for k, v in nums_coordinates.items():
            print(f'{k=} {v=}')
            for sym_cord in symbol_coordinates:
                if is_adjacent(symbol_coord=sym_cord, num_coord=k):
                    num_to_record[k]= nums_coordinates[k]
                    break
        print(f'{num_to_record=}')
        print(sum(num_to_record.values()))

        for k, v in num_to_record.items():
            if v == 350:
                print(k, v)



# 4361 is good for test     
# 342818
# 537066
# too low   
# 
# 538396 too high
# 538046 the right
    
if __name__ == '__main__':
    main()