import random

for i in range(1, 10):
    dado01 = random.randint(1, 6)
    dado02 = random.randint(1, 6)

    if dado01 > dado02:
        print(f'Dado01 {dado01} > dado02 {dado02}')
    elif dado02 > dado01:
        print(f'Dado01 {dado01} < dado02 {dado02}')
    else:
        print(f'dado01 {dado01} = dado02 {dado02}')
