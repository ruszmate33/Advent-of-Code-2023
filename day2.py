# cubes RGB
# - Each time you play this game, he will hide a secret number of cubes of each color in the bag
# - your goal is to figure out information about the number of cubes

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

import math

test_input = (
"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
)
possible_cubes = {'red': 12, 'green': 13, 'blue': 14}
valid_game_ids = []

def valid_draw(draw):
    num, color = draw.split(' ')
    # print(f'{num=} {color=}')
    if int(num) > possible_cubes[color]:
        # print(f'not valid {num=} {color=}') 
        return False
    return True

def get_minimum_set(sets):
    minimum_set = {}
    for draws in sets:
        for draw in draws:
            print(f'{draw=}')
            num, color = draw.split(' ')
            num = int(num)
            # if color not in minimum_set:
            #     minimum_set[color] = num
            if minimum_set.get(color, 0) < num:
                minimum_set[color] = num
    return minimum_set 



def main():
    sum_of_prods = 0
    # lines = test_input.split('\n')
    # print(lines)
    with open('input2.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            game_id = line.split(': ')[0].split(' ')[1]
            sets = line.split(': ')[1].split('; ')     
            sets = [s.split(', ') for s in sets]    
            minimum_set = get_minimum_set(sets)
            sum_of_prods += math.prod(list(minimum_set.values()))
            print(sum_of_prods)


# def main():
#     # lines = test_input.split('\n')
#     with open('input2.txt') as f:
#         lines = f.readlines()
#         # print(lines)
#         for line in lines:
#             line = line.strip()
#             game_id = line.split(': ')[0].split(' ')[1]
#             # print(f'{game_id=}')
#             sets = line.split(': ')[1].split('; ')
#             # print(f'{sets=}')
#             # for s in sets:
#             #     # print(f'id {game_id} {s}')
#             #     draws = s.split(', ')
#             sets = [s.split(', ') for s in sets]    
#             # print(f'{sets=}')
#             if all(valid_draw(draw) for draws in sets for draw in draws):
#                 valid_game_ids.append(int(game_id))
#                     #     print(f'not valid {draw}')
#                 # if all(valid_draw(draw) for draw in draws):
#                 #     valid_game_ids.append(int(game_id))

#         print(f'{valid_game_ids=}')
#         print(f'{sum(valid_game_ids)}')
                 
                
if __name__ == '__main__':
    main()