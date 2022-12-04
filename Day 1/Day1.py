import time

with open('input.txt') as f:
    data = f.readlines()

def main():
    # Part 1 and 2 together cause they were really similar
    calories_current_elf = 0 
    calories_best_elf = 0
    current_elf = 1
    best_elf = 1
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


t1 = time.perf_counter()
main()
t2 = time.perf_counter()
print(f'Time taken: {(t2-t1):.4f}s')
