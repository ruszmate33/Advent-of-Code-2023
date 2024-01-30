SPEC_DIGITS = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
    ]

TEST_INPUT_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_INPUT_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

file_path = '../inputs/input1.txt'

# part1 54605
# part2 55429 with `include_alphabetic`


def extract_number_from_line(line: str, include_alphabetic=False) -> int:
    num = ''
    for i, char in enumerate(line):
        if char.isdigit():
            num += char
        if include_alphabetic:
            for d, val in enumerate(SPEC_DIGITS, start=1):
                if line[i:].startswith(val):
                    num += str(d)

    if not num:
        return 0
    num = num[0] + num[-1]
    return int(num)


def main():
    nums = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # lines = TEST_INPUT_1
        for line in lines:
            nums.append(
                extract_number_from_line(line, include_alphabetic=True))
    print(sum(nums))


if __name__ == '__main__':
    main()
