import time


def process_data(FILENAME):
    with open(FILENAME) as f:
        _, moves = f.read().split('\n\n')
    moves = moves.split('\n')
    stacks = {  1: ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q'],
                2: ['W', 'D', 'B', 'G'],
                3: ['F', 'W', 'R', 'T', 'S', 'Q', 'B'],
                4: ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N'],
                5: ['M', 'P', 'D', 'V', 'F'],
                6: ['F', 'W', 'J'],
                7: ['L', 'N', 'Q', 'B', 'J', 'V'],
                8: ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N'],
                9: ['J', 'S', 'Q', 'C', 'W', 'D', 'M']}
    """stacks = {  1: ['Z', 'N'],
                2: ['M', 'C', 'D'],
                3: ['P']}"""

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
    
    #on_top_of = []
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