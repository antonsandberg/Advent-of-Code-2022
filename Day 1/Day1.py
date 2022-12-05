import time

def process_data(INPUT):
    with open(INPUT) as f:
        data = f.readlines()
    return data

def main():
    TEXTFILE = 'Day 1\input.txt'
    data = process_data(TEXTFILE)
    
    # Part 1 and 2 together cause they were really similar
    calories_current_elf = 0 
    current_elf = 1
    calories_elves = []
    for instruction in data:
        if instruction != '\n':
            calories_current_elf += int(instruction.split('/')[0])
        else:
            calories_elves.append(calories_current_elf)
            calories_current_elf = 0
            current_elf += 1

    calories_elves = sorted(calories_elves, reverse=True)
    print(f'Day 1 part 1: {calories_elves[0]}')
    print(f'Day 1 part 2: {sum(calories_elves[0:3])}')


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {(t2-t1):.6f}s')
