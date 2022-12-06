import time

def process_data(FILENAME):
    with open(FILENAME) as f:
        return f.read().strip()



def main():

    FILENAME = 'Day 6\input.txt'

    part = 2
    if part == 1:
        substr_len = 4
    else:
        substr_len = 14 
    
    data = process_data(FILENAME)
    for i in range(len(data)-substr_len):
        substr = data[i:i+substr_len]
        if len(set(substr)) == len(substr):
            print(f'Day 6 part {part}: {i+substr_len}')
            return


if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {t2-t1:-6f}s')
    