def TicTacDraw(board):
    # match symbols with numbers 0,1,2 in the list
    lst = [' O ',' X ','   ']

    for i in range(0,len(board)) :

        # initialize a new line
        line = ''

        # print the line
        for num in board[i] :
            line = line + lst[num] + '|'
        line = line.strip('|')
        print(line)

        # print separate line in the same length but do not print for the last line
        if i != len(board)-1 :
            print('-' * len(line))