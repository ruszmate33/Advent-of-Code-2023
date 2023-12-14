TEST_INPUT = (
"""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
)

# 27845 the right answer for 1st part
# 9496801 for 2nd

# Card Num
# hits
# copy number
class Card:
    def __init__(self, number: int, winning_nums: list[int], nums: list[int]):
        self.number = number
        self.copies = 1
        self.winning_nums = winning_nums
        self.nums = nums
        self.hits = len([num for num in nums if num in winning_nums])

    def increment_copy(self):
        self.copies += 1

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.number}, hits={self.hits}, copies={self.copies})'



cards = []

def main():
    # lines = TEST_INPUT.split('\n')
    with open('input4.txt') as f:
        lines = f.readlines()
        for line in lines:
            winning_part, nums = line.split(' | ')
            card_num, winning_nums = winning_part.split(': ')
            card_num = [int(s) for s in card_num.split() if s.isdigit()][0]
            winning_nums = [int(num_str) for num_str in winning_nums.split(' ') if num_str]
            nums = [int(num_str) for num_str in nums.split(' ') if num_str]
            card = Card(number=card_num, 
                        winning_nums=winning_nums,
                        nums=nums,
                        )
            cards.append(card)
        print(cards)
        for card in cards:
            # print(f'{card=}')
            num = card.number
            hits = card.hits
            affected_cards = cards[num: num+hits]
            # print(f'{affected_cards=}')
            for i in range(card.copies):
                [c.increment_copy() for c in affected_cards]
            # print(f'{cards=}')
            # print('='*10)
        # print(cards)
        print(f'{sum([c.copies for c in cards])=}')

    
if __name__ == '__main__':
    main()