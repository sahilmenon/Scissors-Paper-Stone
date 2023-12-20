import random
moveslist = ['r','p','s']
print('Hello! This is rock paper scissors')


while True:
    comval = random.choice(moveslist)
    userinp = input('enter either r for rock, p for paper and s for scissors:    ')

    if userinp == 'r':
        if comval == 'r':
            print('It is a draw. try again')
        if comval == 'p':
            print('Computer chose paper. You have lost. Try again')
        if comval == 's':
            print('Computer chose scissors. You win! Try to see if you can beat it again!')
    elif userinp == 'p':
        if comval == 'r':
            print('Computer chose rock. You win! Try to see if you can beat it again!')
        if comval == 'p':
            print('It is a draw. try again')
        if comval == 's':
            print('Computer chose scissors. You have lost. Try again')
    elif userinp == 's':
        if comval == 'r':
            print('Computer chose rock. You have lost. Try again')
        if comval == 'p':
            print('Computer chose paper. You win! Try to see if you can beat it again!')
        if comval == 's':
            print('It is a draw. try again')
    else:
        print('value undetected. Ensure only "p", "r" or "s" is written')