import time
from collections import defaultdict


def process_data(FILENAME):
    with open(FILENAME) as f:
        unf, moves = f.read().split('\n\n')
    moves = moves.split('\n')
    unf = unf.splitlines()
    unf = unf[:-1]

    stacks = defaultdict(list)
    for line in unf:
        maybe_crates = line[1::4]
        for i, maybe_crate in enumerate(maybe_crates):
            if maybe_crate != " ":
                stacks[i+1].append(maybe_crate)
        
    for key, stack in stacks.items():
        stacks[key] = stack[::-1]

    return stacks, moves


def main():
    FILENAME = 'Day 5\input.txt'
    stacks, moves = process_data(FILENAME)
    stacks_2, _ = process_data(FILENAME)
    # Part 1
    for move in moves:
        _, n_of_moves, _, location, _, destination = move.split()
        for _ in range(int(n_of_moves)):
            stacks[int(destination)].append(stacks[int(location)].pop())
    
    part_1 = "".join([c[-1] for c in stacks.values()])
    print(f'Day 5 part 1: {part_1}')

    # Part_2
    for move in moves:
        _, n_of_moves, _, location, _, destination = move.split()

        tmp_list = []
        for _ in range(int(n_of_moves)):
            tmp_list.append(stacks_2[int(location)].pop())

        stacks_2[int(destination)] += tmp_list[::-1]

    part_2 = "".join([c[-1] for c in stacks_2.values()])
    print(f'Day 5 part 2: {part_2}')


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {t2-t1:.6f}s')