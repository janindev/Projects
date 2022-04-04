
import itertools as it

teams = ['Marketing', 'PO', 'DA', 'Tech', 'CCC', 'BusDev']

print('All combinations:')

for x,y in it.combinations(teams, 2):
    print(x,y)

print('\n'* 2)



######################################

n = int(len(teams)/2)                   #number of combinations within one round, 6 teams --> 6/2 = 3 combinations

groups = []

print('Rounds of 3:')

for i in range(len(teams)-1):           #number of rounds equals number of teams minus 1, 6 teams --> 5 rounds
    t = teams[:1] + teams[-i:] + teams [1:-i] if i else teams           #t = first item in list + last i teams + all teams except last i teams 
    groups.append(list(zip(t[:n], reversed(t[n:]))))

count = 1

for i in groups:
    print(f'Round {count}', i, '\n')
    count = count+1
