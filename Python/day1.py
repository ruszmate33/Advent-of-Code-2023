SPEC_DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

lines = [
'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen',
]

def main():
    nums = []
    with open('input1.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            num = ''
            for i, char in enumerate(line):
                if char.isdigit():
                    num += char
                for d, val in enumerate(SPEC_DIGITS, start=1):
                    if line[i:].startswith(val):
                        num += str(d)
            
            if num:
                num = num[0] + num[-1]
                nums.append(int(num))
                print(num)
    print(sum(nums))
                         

if __name__ == '__main__':
    main()