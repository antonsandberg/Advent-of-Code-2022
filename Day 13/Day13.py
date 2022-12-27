import json

def process_data(FILENAME):
    with open(FILENAME) as f:
        raw = f.read().split('\n\n')
    return [x.split('\n') for x in raw]

def main():
    FILENAME = 'Day 13\sample_input.txt'
    data = process_data(FILENAME)
    for pair in data:
        pair_1 = json.loads(pair[0])
        pair_2 = json.loads(pair[1])
        for index, (el1, el2) in enumerate(zip(pair_1, pair_2)):
            if isinstance(el1, list) and isinstance(el2, list):
                for ell1, ell2
            
            elif isinstance(el1, list) and isinstance(el2, int):
            
            elif isinstance(el1, int) and isinstance(el2)

if __name__ == '__main__':
    main()