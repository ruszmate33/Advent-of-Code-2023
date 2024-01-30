TEST_INPUT = (
"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
)

# 27845 the right answer



def main():
    # lines = TEST_INPUT.split('\n')
    with open('input4.txt') as f:
        lines = f.readlines()
        winning_numbers, numbers = [],  []
        for line in lines:
            winning_part, nums = line.split(' | ')
            card_num, winning_nums = winning_part.split(': ')
            winning_nums = [int(num_str) for num_str in winning_nums.split(' ') if num_str]
            # print(f'{winning_nums=}')
            nums = [int(num_str) for num_str in nums.split(' ') if num_str]
            # print(f'{nums=}')
            numbers.append(nums)
            winning_numbers.append(winning_nums)
        # with open('input3.txt') as f:
        #     lines = f.readlines()
        # print(f'{winning_numbers=}')
        # print(f'{numbers=}')
        score = 0
        for nums, winning_nums in zip(numbers, winning_numbers):
            # print(f'{[num for num in nums if num in winning_nums]=}')
            hits = len([num for num in nums if num in winning_nums])
            # print(f'{hits=}')
            if hits > 0:
                score += 2 ** (hits - 1)
            # print(f'{score=}')
        print(score)

        


    
if __name__ == '__main__':
    main()