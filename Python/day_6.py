TEST_INPUT = (
"""Time:      7  15   30
Distance:  9  40  200"""
)

# 1710720 part 1

def number_of_way_to_win(time_to_race: int, distance_to_beat: int) -> int:
    races_won = 0
    for time_hold_botton in range(time_to_race + 1):
        speed = time_hold_botton
        time_to_travel = time_to_race - time_hold_botton
        distance_traveled = speed * time_to_travel
        if distance_traveled > distance_to_beat:
            races_won += 1
    return races_won


def main():
    with open('input6.txt') as f:
        puzzle_input = f.read().split('\n')
        # puzzle_input = TEST_INPUT.split('\n')
        
        # PART 1
        # times = [int(num) for num in puzzle_input[0].split(":")[1].split(" ") if num != ""]
        # distances = [int(num) for num in puzzle_input[1].split(":")[1].split(" ") if num != ""]
        # print(f'{times=}, {distances=}')

        # product_ways_to_win = 1
        # for time, distance in zip(times, distances):
        #     print(f'{time=}, {distance=}')
        #     product_ways_to_win *= number_of_way_to_win(time, distance)
        # print(f'{product_ways_to_win}')

        # PART 2
        # 35349468 is the right answer
        num_str = ''
        for num in puzzle_input[0].split(":")[1].split(" "):
            if num == '':
                continue
            num_str += num
        time = int(num_str)
        dist_str = ''
        for num in puzzle_input[1].split(":")[1].split(" "):
            if num == '':
                continue
            dist_str += num
        distance = int(dist_str)
        print(f'{time=}, {distance=}')
        print(f'{number_of_way_to_win(time, distance)=}')

        # distances = [int(num) for num in puzzle_input[1].split(":")[1].split(" ") if num != ""]


if __name__ == '__main__':
    main()