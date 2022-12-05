import time
from string import ascii_lowercase, ascii_uppercase

def main():
    with open('Day 3\input.txt') as f:
        data = f.read().strip().split()

    letters = ascii_lowercase
    LETTERS = ascii_uppercase
    ALL_LETTERS = letters + LETTERS
    letter_ranks = {l:i+1 for i, l in enumerate(ALL_LETTERS)}


    summa = 0
    for rucksack in data:
        half_length = int(len(rucksack)/2)
        first_half = rucksack[:half_length]
        second_half = rucksack[half_length:]
        common_char = ''.join(set(first_half).intersection(second_half))
        summa += letter_ranks[common_char]

    print(f'Day 3 part 1: {summa}')


    ind = 0
    summa_2 = 0
    while ind < len(data):
        first_half = [data[ind+0], data[ind+1], data[ind+2]]
        second_half = [data[ind+3], data[ind+4], data[ind+5]]
        common_char_1 = list(set.intersection(*map(set,first_half)))
        common_char_2 = list(set.intersection(*map(set,second_half)))

        summa_2 += letter_ranks[common_char_1[0]]
        summa_2 += letter_ranks[common_char_2[0]]
        ind += 6

    print(f'Day 3 part 2: {summa_2}')

t1 = time.perf_counter()
main()
t2 = time.perf_counter()

print(f'Time taken: {t2-t1:.4f}s')