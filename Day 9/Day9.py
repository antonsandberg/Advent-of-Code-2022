import time

def process_data(FILENAME):
    with open(FILENAME) as f:
        return [x.split() for x in f.read().split('\n')]


def main():
    FILENAME = "Day 9\sample_input.txt"
    data = process_data(FILENAME)
    h = (0, 0)
    t = (0, 0)
    tail_pos = set()
    dirs = {'R':[0, 1], 'L':[0, -1], 'U':[-1, 0], 'D':[1, 0]}
    for inst, val in data:
        val = int(val)
        dr, dc = dirs[inst][0]*val, dirs[inst][1]*val
        h = (h[0]+dr, h[1]+dc)

        if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
            t = (h[0]-dirs[inst][0], h[1]-dirs[inst][1])
        if t not in tail_pos:
            tail_pos.add(t)
        print(f'{h=}')
        print(f'{t=}')
        print()

    
    print(len(tail_pos))

        
       



if __name__ == '__main__':
    main()