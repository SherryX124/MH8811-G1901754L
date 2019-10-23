from random import choice, shuffle

def genPassword(n):
    lst = list()
    password = ''

    # define global variables
    global numbers, lowers, uppers, symbols
    numbers = '0123456789'
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '~`!@#$%^&*_:;\',.|/\\'

    # generate one from each category
    lst.append(choice(numbers))
    lst.append(choice(lowers))
    lst.append(choice(uppers))
    lst.append(choice(symbols))

    # generate the rest
    for i in range(0,n-4):
        lst.append(choice(numbers+lowers+uppers+symbols))
    
    # rearrange the list
    shuffle(lst)

    # transfer to string
    for i in range(0,n):
        password = password + lst[i]

    return password

if __name__ == "__main__" :
    print(genPassword(12))


    # numInt = random.randint(1,n-3)
    # numLower = random.randint(1,n-numInt-2)
    # numUpper = random.randint(1,n-numInt-numLower-1)
    # numSymbol = n - numInt - numLower - numUpper

    # integer = random.randint(0, 9)
    # lower = random.choice('abcdefghijklmnopqrstuvwxyz')
    # upper = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # symbol = random.choice('!@#$%^&*()_+=-:;\'<>,.|')