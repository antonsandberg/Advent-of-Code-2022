

def process_data(FILENAME):
    with open(FILENAME) as f:
        return  [x.strip() for x in f.readlines()]


def main():
    FILENAME = 'Day 10\input.txt'
    data = process_data(FILENAME)
    x = 1
    cycle = 0
    i = 0
    x_values = []
    while cycle <= 220:
        if data[i] == 'noop':
            cycle += 1
            i += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                x_values.append(x*cycle)
        else:
            _, val = data[i].split()
            val = int(val)
            x += val
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                x_values.append((x-val)*cycle)
        # print(cycle)
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                x_values.append((x-val)*cycle)
            i += 1
    
    print(sum(x_values))
    


if __name__ == '__main__':
    main()