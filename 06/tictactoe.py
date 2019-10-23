def TicTacDraw(board):
    # match symbols with numbers in the list
    lst = [' O ',' X ','   ']

    for i in range(0,len(board)) :

        # initialize a new line
        line = ''

        # print the line
        for num in board[i] :
            line = line + lst[num] + '|'
        print(line.strip('|'))

        # print separate line with the same length but do not print the last one
        if i != len(board)-1 :
            print('-' * len(line))


# # test
# board = [[0,1,2,0,1],[2,0,0,2,0],[1,1,2,1,1],[1,2,0,1,2]]
# TicTacDraw(board)