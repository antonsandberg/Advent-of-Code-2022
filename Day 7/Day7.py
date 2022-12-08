import time

def process_data(FILENAME):
    with open(FILENAME) as f:
        return f.read().split('\n')


def main():
    FILENAME = 'Day 7\sample_input.txt'
    data = process_data(FILENAME)
    

if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f'Time taken: {t2-t1:.6f}s')