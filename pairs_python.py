
import itertools as it

teams = ['Marketing', 'PO', 'DA', 'Tech', 'CCC', 'BusDev', 'HR', 'Finance'] 

print('All combinations:')

for x,y in it.combinations(teams, 2):
    print(x,y)

print('\n'* 2)


######################################

##https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
##https://stackoverflow.com/questions/56428614/groups-of-unique-pairs-where-members-appear-once-per-group/56435147#56435147


n = int(len(teams)/2)       #number of combinations within one round, 6 teams --> 6/2 = 3 combinations

groups = []

print('Rounds of 3:')

for i in range(len(teams)-1):                                       #number of rounds equals number of teams minus 1, 6 teams --> 5 rounds
    rt = teams[:1] + teams[-i:] + teams [1:-i] if i else teams      #rt --> list with rotating teams --> first item in teams list (Marketing) + last i items in teams + items in teams between first and last i teams (i.e. Teams in between)
    groups.append(list(zip(rt[:n], reversed(rt[n:]))))              #append to groups list --> first items of rt and rt reversed

count = 1

for i in groups:
    print(f'Round {count}', i, '\n')
    count = count+1