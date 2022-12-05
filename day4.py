from textwrap import wrap
import itertools

X = [l.strip() for l in open('in\\4.txt')]

'''
X = [l.strip() for l in open('in\\1.txt')]
for elf in ('\n'.join(X)).split('\n\n'):
    for line in elf.split('\n'):
        asd =1 # do logic here
'''

numbers = [int(x) for x in X.pop(0).split(',')]
X.pop(0)

# creats a list of bingo boards. Each board is a 5 by 5 list of ints 
boards = [[[int(z) for z in wrap(y, 3)] for y in x.split('\n')] for x in ('\n'.join(X)).split('\n\n')]

# creates a list for each board where board[i][0] is how many numbers have been called from each row
progress = [([0,0,0,0,0],[0,0,0,0,0]) for x in range(len(boards))]

winner = None
for n in numbers:
    for board_index in range(len(boards)):
        for j in range(5):
            if n in boards[board_index][j]:
                progress[board_index][0][j] += 1
                progress[board_index][1][boards[board_index][j].index(n)] += 1
                break

        if 5 in progress[board_index][0]:
            winner = (board_index, n)
            break
    if winner:
        break


flat_list = list(itertools.chain(*boards[winner[0]]))
found_nums_sum = sum(x for x in flat_list if x in numbers[:numbers.index(winner[1])+1])
print((sum(flat_list) - found_nums_sum) * winner[1])