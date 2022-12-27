import numpy as np

def process_data(FILENAME):
    with open(FILENAME) as f:
        raw = f.read().split('\n\n')
    monkey_inst = dict()
    for i, monkey in enumerate(raw):
        things = monkey.split('\n')
        items = things[1].split(':')[1]
        items = [int(x) for x in items.split(',')]
        operation = things[2].split('=')[1].lstrip()
        test = int(things[3].split('by')[1].lstrip())
        if_true = int(things[4].split('monkey')[1].lstrip())
        if_false = int(things[5].split('monkey')[1].lstrip())
        monkey_inst[i] = dict()
        monkey_inst[i]['items'] = items
        monkey_inst[i]['operation'] = operation
        monkey_inst[i]['test'] = test
        monkey_inst[i]['if_true'] = if_true
        monkey_inst[i]['if_false'] = if_false
    return monkey_inst





def main():
    FILENAME = 'Day 11\input.txt'
    monkeys = process_data(FILENAME)

    # Part 1 - run the game for 20 rounds
    # Part 2 - find another way to scale down 
    super_modulo = 1
    for i in range(len(monkeys)):
        super_modulo *= monkeys[i]['test']

    monkey_throws = [0]*len(monkeys)
    for _ in range(10000):
        for monkey_num, things in monkeys.items():
            new_things = things['items']
            # Checking if the list is empty
            if not new_things:
                continue
            

            for i, old in enumerate(things['items']):
                new_things[i] = eval(things['operation']) % super_modulo
                if new_things[i] % things['test'] == 0:
                    key_of_choice = 'if_true'
                else:
                    key_of_choice = 'if_false'
                
                monkey_throws[monkey_num] += 1
                
                monkeys[things[key_of_choice]]['items'].append(new_things[i])
            monkeys[monkey_num]['items'] = []          
    two_best = sorted(monkey_throws, reverse=True)[:2]
    two_best[0] = np.longlong(two_best[0])
    two_best[1] = np.longlong(two_best[1])
    print(f'Day 11 part 1: {np.longlong(np.prod(two_best))}')
 

if __name__ == '__main__':
    main()