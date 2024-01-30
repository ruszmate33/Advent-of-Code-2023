from functools import reduce
from operator import mul

# 4361
# 467835 gear ratios
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

# 81709807 for the original input

def get_product_sign_coordinates(lines):
    product_sign_coordinates = []
    for i, line in enumerate(lines):
        line = line.strip()
        print(f'{i} {line}')
        for j, char in enumerate(line):
            if char != '*':
                continue
            # print(f'{i}-{j} {char}')
            product_sign_coordinates.append((i, j))
    return product_sign_coordinates

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
    # lines = TEST_INPUT.split('\n')
    with open('input3.txt') as f:
        lines = f.readlines()
    # print(lines)
        product_sign_coordinates = get_product_sign_coordinates(lines)
        print(f'{product_sign_coordinates=}')
        nums_coordinates = get_nums_coordinates(lines)
        print(f'{nums_coordinates=}')
        
        nums_around_product_sign = {}
        # print(nums_coordinates)
        for sign_cord in product_sign_coordinates:
            nums = []
            for num_coord, num in nums_coordinates.items():
            # print(f'{k=} {v=}')
                if is_adjacent(symbol_coord=sign_cord, num_coord=num_coord):
                    if not nums_around_product_sign.get(sign_cord):
                        nums_around_product_sign[sign_cord] = []
                    nums_around_product_sign[sign_cord].append(num)
        print(f'{nums_around_product_sign=}')
        print(sum([reduce(mul, nums) for nums in nums_around_product_sign.values() if len(nums) > 1]))



# 4361 is good for test     
# 342818
# 537066
# too low   
# 
# 538396 too high
# 538046 the right
    
if __name__ == '__main__':
    main()