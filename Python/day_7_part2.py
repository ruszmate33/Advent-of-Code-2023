from collections import Counter, defaultdict

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# 5905 for part 2 test
TEST_INPUT_PART_2 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# 6440 test inputs correct output

# first part 250951660 is the right answer
# 252135538 is too high
# 251481660 is the right answer


CARD_TYPES = (
    'high_card',
    'one_pair',
    'two_pair',
    'three',
    'full_house',
    'four',
    'five',
)

CARD_MAPPINGS = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 'J': 0}


def kind(hand: str) -> str:
    counter = Counter(hand)
    if counter['J'] == 5:
        return 'five'

    most_common_not_joker = [
        (card, num) for card, num in counter.most_common() if card != 'J'
    ][0][1]
    if num_jokers := counter.get('J'):
        most_common_not_joker += num_jokers
        # counter['J'] = 0  # don't consider J anymore
        del counter['J']

    try:
        second_most_common_not_joker = [
            (card, num) for card, num in counter.most_common() if card != 'J'
        ][1][1]
        # second_most_common = counter.most_common()[1][1]
    except IndexError:
        second_most_common_not_joker = 0
    if most_common_not_joker == 5:
        return 'five'
    elif most_common_not_joker == 4:
        return 'four'
    elif most_common_not_joker == 3 and second_most_common_not_joker == 2:
        return 'full_house'
    elif most_common_not_joker == 3:
        return 'three'
    elif most_common_not_joker == 2 and second_most_common_not_joker == 2:
        return 'two_pair'
    elif most_common_not_joker == 2:
        return 'one_pair'
    return 'high_card'


def value_of_card(char: str) -> int:
    try:
        value = int(char)
    except ValueError:
        value = CARD_MAPPINGS[char]
    return value


def compare_hands(hand_bid) -> tuple[int]:
    hand, _ = hand_bid
    return tuple(value_of_card(char) for char in hand)


def get_order_by_rank(type_hand_bid):
    ordered_type_hand_bid = {}
    for t in CARD_TYPES:
        if hands_bids := type_hand_bid.get(t):
            # ordered_type_hand_bid[t] = hands_bids.sort(key=compare_hands)
            hands_bids.sort(key=compare_hands)
            ordered_type_hand_bid[t] = hands_bids
        # except AttributeError as e:
        #     print(f'{e}, {t=}')
    return ordered_type_hand_bid


def total_winnings(ordered_type_hand_bid):
    from itertools import chain

    ordered_hand_bid = [hands_bids for hands_bids in ordered_type_hand_bid.values()]
    flat_ordered_hand_bid = list(chain.from_iterable(ordered_hand_bid))
    winnings = 0
    for i, hand_bid in enumerate(flat_ordered_hand_bid, start=1):
        # print(f'{i=}, {hand_bid[1]=}')
        winnings += i * hand_bid[1]
    return winnings


type_hand_bid: dict[list[tuple[str]]] = defaultdict(list)


def main():
    with open('input7.txt') as f:
        puzzle_input = f.read()
        # print(f'{TEST_INPUT=}')
        # for line in TEST_INPUT_PART_2.split('\n'):
        for line in puzzle_input.split('\n'):
            hand, bid = line.split(' ')
            # print(f'{hand=}, {bid=}')
            # print(f'{kind(hand)=}')
            type_hand_bid[kind(hand)].append((hand, int(bid)))
        # print(f'{type_hand_bid=}')
        # print(f'{get_order_by_rank(type_hand_bid)=}')
        print(f'{total_winnings(get_order_by_rank(type_hand_bid))=}')


if __name__ == '__main__':
    main()
