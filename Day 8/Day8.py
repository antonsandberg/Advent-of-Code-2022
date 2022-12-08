import time
import numpy as np


def process_data(FILENAME):
    with open(FILENAME) as f:
        data = f.read().strip().split('\n')
    list_data = []
    for row in data:
        list_data.append(list(map(int, row)))
    return np.array(list_data)


def main():
    FILENAME = 'Day 8\input.txt'
    forest = process_data(FILENAME)
    visible = sum(np.shape(forest))*2-4
    counted = set()

    # Part 1
    for i in range(1, len(forest)-1):
        for j in range(1, np.shape(forest)[0]-1):
            if (i, j) in counted:
                continue
            else:
                current_tree = forest[i, j]
                trees_left = forest[:i, j]
                trees_right = forest[i+1:, j]
                trees_up = forest[i, :j]
                trees_down = forest[i, j+1:]

                if all([True if x < current_tree else False for x in trees_left]):
                    visible += 1
                    counted.add((i, j))
                elif all([True if x < current_tree else False for x in trees_right]):
                    visible += 1
                    counted.add((i, j))
                elif all([True if x < current_tree else False for x in trees_up]):
                    visible += 1
                    counted.add((i, j))
                elif all([True if x < current_tree else False for x in trees_down]):
                    visible += 1
                    counted.add((i, j))
            
    print(f'Day 8 part 1: {visible}')


    # Part 2
    best_scenic_score = 0
    counted_2 = set()
    for i in range(1, len(forest)-1):
        for j in range(1, np.shape(forest)[0]-1):
            if (i, j) in counted_2:
                continue
            else:
                current_tree = forest[i, j]

                trees_left = forest[i, :j][::-1]
                trees_right = forest[i, j+1:]
                trees_up = forest[:i, j][::-1]
                trees_down = forest[i+1:, j]
                
                v_trees_left = 1
                v_trees_right = 1
                v_trees_up = 1
                v_trees_down = 1

                for k, other_tree in enumerate(trees_left):
                    if current_tree > other_tree:
                        v_trees_left += 1
                        if k == len(trees_left)-1:
                            v_trees_left -= 1
                    else:
                        break
                for k, other_tree in enumerate(trees_right):
                    if current_tree > other_tree:
                        v_trees_right += 1
                        if k == len(trees_right)-1:
                            v_trees_right -= 1
                    else:
                        break
                for k, other_tree in enumerate(trees_up):
                    if current_tree > other_tree:
                        v_trees_up += 1
                        if k == len(trees_up)-1:
                            v_trees_up -= 1
                    else:
                        break
                for k, other_tree in enumerate(trees_down):
                    if current_tree > other_tree:
                        v_trees_down += 1
                        if k == len(trees_down)-1:
                            v_trees_down -= 1
                    else:
                        break
                trees_visible = v_trees_left*v_trees_right*v_trees_up*v_trees_down 
                if trees_visible > best_scenic_score:
                    best_scenic_score = trees_visible

    print(f'Day 8 part 2: {best_scenic_score}')

if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {t2-t1:.6f}s')

