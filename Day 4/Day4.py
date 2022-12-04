import time

def read_data() -> str:
    with open('input.txt') as f:
        return f.read().split('\n')
    

def main():
    data = read_data()
    # Part 1 and 2 in the same, cause just adding an if
    part_1 = 0
    part_2 = 0
    for pair in data:
        pair_1, pair_2 = pair.split(',')
        s_1, e_1 = map(int, pair_1.split('-'))
        s_2, e_2 = map(int, pair_2.split('-'))

        gen_1 = range(s_1, e_1+1)
        gen_2 = range(s_2, e_2+1)

        # My solution with ranges
        # if all(item in gen_2 for item in gen_1) or all(item in gen_1 for item in gen_2):
        #     part_1 += 1

        # A lot smarter "math" solution I should have done
        if (s_1 >= s_2 and e_1 <= e_2) or (s_2 >= s_1 and e_2 <= e_1):
            part_1 += 1

        # My solution with ranges
        # if any(item in gen_2 for item in gen_1) or any(item in gen_1 for item in gen_2):
        #     part_2 += 1

        # A lot smarter "math" solution I should have done
        if not (e_1 < s_2 or e_2 < s_1):
            part_2 += 1

    print(f'Day 4 part 1: {part_1}')
    print(f'Day 4 part 2: {part_2}')

if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {(t2-t1):.6f}s')

