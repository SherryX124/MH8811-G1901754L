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


# # -------------------------------------------------------------
# # Another approach to do this

# from random import randint, choice, shuffle

# def genPassword(n):
#     lst = list()
#     password = ''

#     # determine the numbers for each category
#     numInt = randint(1, n-3)
#     numLower = randint(1, n-numInt-2)
#     numUpper = randint(1, n-numInt-numLower-1)
#     numSymbol = n - numInt - numLower - numUpper


#     # generate 0-9
#     for i in range(0,numInt) :
#         lst.append(randint(0, 9))

#     # generate lowercase letters
#     for i in range(0,numLower) :
#         lst.append(chr(randint(97, 122)))

#     # generate uppercase letters
#     for i in range(0,numUpper) :
#         lst.append(chr(randint(65, 90)))

#     # generate symbols
#     for i in range(0,numSymbol) :
#         lst.append(choice('~`!@#$%^&*_:;\',.|/\\'))


#     # rearrange the list
#     shuffle(lst)

#     # transfer to string
#     for i in range(0,n):
#         password = password + str(lst[i])

#     return password


# if __name__ == "__main__" :
#     print(genPassword(12))