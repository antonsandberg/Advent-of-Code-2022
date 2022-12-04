import time

def rock_paper_scissors_1(opp, you):
    if opp == 'A' and you == 'X':
        return(1+3)
    elif opp =='B' and you == 'X':
        return(1)
    elif opp == 'C' and you == 'X':
        return(6+1)
    elif opp == 'A' and you == 'Y':
        return(6+2)
    elif opp == 'B' and you == 'Y':
        return(3+2)
    elif opp == 'C' and you == 'Y':
        return(2)
    elif opp == 'A' and you == 'Z':
        return(3)
    elif opp == 'B' and you == 'Z':
        return(6+3)
    else:
        return(3+3)

def rock_paper_scissors_2(opp, you):
    if opp == 'A' and you == 'X':
        return(0+3)
    elif opp =='B' and you == 'X':
        return(0+1)
    elif opp == 'C' and you == 'X':
        return(0+2)
    elif opp == 'A' and you == 'Y':
        return(3+1)
    elif opp == 'B' and you == 'Y':
        return(3+2)
    elif opp == 'C' and you == 'Y':
        return(3+3)
    elif opp == 'A' and you == 'Z':
        return(6+2)
    elif opp == 'B' and you == 'Z':
        return(6+3)
    else:
        return(6+1)


with open('input.txt') as f:
    data = [x.split() for x in f.read().split('\n')]

def main():
    score_1 = 0
    score_2 = 0
    for y in data:
        score_1 += rock_paper_scissors_1(y[0], y[1])
        score_2 += rock_paper_scissors_2(y[0], y[1])


    print(f'Day 2 part 1: {score_1}')
    print(f'Day 2 part 2: {score_2}')


t1 = time.perf_counter()
main()
t2 = time.perf_counter()
print(f'Time taken: {(t2-t1):.4f}s')
