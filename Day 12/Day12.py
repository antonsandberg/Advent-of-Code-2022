from collections import deque

def process_data(FILENAME):
    with open(FILENAME) as f:
        raw = f.read().split('\n')
    data = []
    for row_num, row in enumerate(raw):
        if 'E' in row:
            e = (row.index('E'), row_num)
        elif 'S' in row:
            s = (row.index('S'), row_num)
        data.append([x if x not in ['S', 'E'] else 'a' if x == 'S' else 'z' for x in row])    
    return data, s, e


def main():

    FILENAME = 'Day 12\input.txt'
    map, start, end = process_data(FILENAME)

    next = deque()
    next.append(start)
    neighbs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    max_y, max_x = len(map)-1, len(map[0])-1
    visited = set()
    steps = 0
    while next:
        coords = next.pop()
        for dx, dy in neighbs:
            x, y = coords
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                continue
            elif (new_x, new_y) == end:
                break
            elif (new_x, new_y) in visited:
                continue
            elif (ord(map[new_y][new_x]) - ord(map[y][x])) <= 1:
                next.append((new_x, new_y))
                visited.add((new_x, new_y))
                steps += 1
    
    print(steps)
            
            


    

if __name__ == '__main__':
    main()