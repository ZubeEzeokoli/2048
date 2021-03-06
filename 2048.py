
DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    ran1 = generate_piece(game_board) #dictionary
    ran2 = generate_piece(game_board) #dictionary
    game_board[ran2['row']][ran2['column']] = ran2['value']
    # TODO: place the piece at the specified location
    game_board[ran1['row']][ran1['column']] = ran1['value']
   
    # Initialize game state trackers
    print_board(game_board)
    # Game Loop
    skip = 0
    board_copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while True:
        for r in range(4):
            for c in range(4):
                board_copy[r][c] = game_board[r][c]
        # TODO: Reset user input variable
        # TODO: Take computer's turn
        # place a random piece on the board
        game_tracker = 0 #checks to see if board is full so it stops printing values so I can check for valid moves for a valid input
        for r in game_board:
                for c in r:
                    if c != 0:
                        game_tracker += 1
        #if game_tracker != 16:
            # ran2 = generate_piece(game_board) #dictionary
            # game_board[ran2['row']][ran2['column']] = ran2['value']
       
        # check to see if the game is over using the game_over function
        if game_over(game_board) == True:
            print('Game Over')
            break
       
        # TODO: Show updated board using the print_board function
        #print_board(game_board)
       
        # TODO: Take user's turn
        # Take input until the user's move is a valid key
        user_input = input()
        while user_input != 'w' and user_input != 'a' and user_input != 's' and user_input != 'd' and user_input != 'q':
            user_input = input()
           
        # if the user quits the game, print Goodbye and stop the Game Loop
        if user_input == 'q':
            print('Goodbye')
            break

        # if there isn't a valid move get an input
        if user_input == 'a' or user_input == 'd':
            ctr = 0
            for r in game_board:#checks board to see if its filled
                for c in r:
                    if c != 0:
                        ctr += 1
            for x in range(4):#checks if any possible moves
                for y in range(3,0,-1):
                    if ctr >= 16 and game_board[x][y] != game_board[x][y-1]:
                        ctr += 1
            if ctr == 28:#gets new input then breaks
                while user_input == 'a' or user_input == 'd':
                    user_input = input()
                    if user_input == 'w' or user_input == 's':
                        break
                    user_input = 'a'
        if user_input == 'w' or user_input == 's':
            ctr = 0
            for r in game_board:#checks board to see if its filled
                for c in r:
                    if c != 0:
                        ctr += 1
            for y in range(4):#checks if any possible moves
                for x in range(3,0,-1):
                    if ctr >= 16 and game_board[x][y] != game_board[x-1][y]:
                        ctr += 1
            if ctr == 28:#gets new input then breaks
                while user_input == 'w' or user_input == 's':
                    user_input = input()
                    if user_input == 'd' or user_input == 'a':
                        break
                    user_input = 'w'

        # Execute the user's move
        if user_input == 'w':
            for x in range(4):
                for c in range(4):
                    for r in range(3):
                        if game_board[r][c] == 0:
                            game_board[r][c] = game_board[r+1][c]
                            game_board[r+1][c] = 0
            for col in range(4):
                for row in range(3):
                    if game_board[row][col] == game_board[row+1][col]:
                        game_board[row][col] *= 2
                        game_board[row+1][col] = 0
            for x in range(4):
                for c in range(4):
                    for r in range(3):
                        if game_board[r][c] == 0:
                            game_board[r][c] = game_board[r+1][c]
                            game_board[r+1][c] = 0
        elif user_input == 'a':
            for row in range(len(game_board)):
                for r in range(4):
                    for c in range(4):
                        if game_board[r][c] == 0:
                            game_board[r].pop(c)
                            game_board[r].insert(3,0)
                for col in range(len(game_board)):
                    if game_board[row][col] == game_board[row][col-1]:
                        game_board[row][col] *= 2
                        game_board[row].pop(col-1)
                        game_board[row].insert(3,0)
                if len(game_board[row]) == 3:
                    game_board[row].insert(3,0)
                elif len(game_board[row]) == 2:
                    game_board[row].insert(3,0)
                    game_board[row].insert(3,0)
                elif len(game_board[row]) == 1:
                    game_board[row].insert(3,0)
                    game_board[row].insert(3,0)
                    game_board[row].insert(3,0)
                   
        elif user_input == 's':
            for x in range(4):
                for c in range(4):
                    for r in range(3,0,-1):
                        if game_board[r][c] == 0:
                            game_board[r][c] = game_board[r-1][c]
                            game_board[r-1][c] = 0
            for col in range(4):
                for row in range(3,0,-1):
                    if game_board[row][col] == game_board[row-1][col]:
                        game_board[row][col] *= 2
                        game_board[row-1][col] = 0
            for x in range(4):
                for c in range(4):
                    for r in range(3,0,-1):
                        if game_board[r][c] == 0:
                            game_board[r][c] = game_board[r-1][c]
                            game_board[r-1][c] = 0
        elif user_input == 'd':
            for row in range(len(game_board)):
                for r in range(4):
                    for c in range(4):
                        if game_board[r][c] == 0:
                            game_board[r].pop(c)
                            game_board[r].insert(0,0)
                for col in range(len(game_board)-1,0,-1):
                    if game_board[row][col] == game_board[row][col-1]:
                        game_board[row][col] *= 2
                        game_board[row].pop(col-1)
                        game_board[row].insert(0,0)
                if len(game_board[row]) == 3:
                    game_board[row].insert(0,0)
                elif len(game_board[row]) == 2:
                    game_board[row].insert(0,0)
                    game_board[row].insert(00)
                elif len(game_board[row]) == 1:
                    game_board[row].insert(0,0)
                    game_board[row].insert(0,0)
                    game_board[row].insert(0,0)
            # Check if the user wins
        for r in range(len(game_board)):
            for c in range(len(game_board)):
                if game_board[r][c] == 2048:
                    print('You Win')
                    ctr = 1
            if ctr == 1:
                break
        if ctr == 1:
            break
        if board_copy == game_board:
            print_board(game_board)
            continue
        else:
            ran2 = generate_piece(game_board) #dictionary
            game_board[ran2['row']][ran2['column']] = ran2['value']
        print_board(game_board)
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    ctr = 0
    #finds 0's which means there's still space
    for row in game_board:
        for col in row:
            if col == 0:
                return False
    #finds same nums left and right, up and down so it means you can still merge only in first 3 rows
    for r in range(len(game_board)-1):
        for c in range(len(game_board)-1):
            if game_board[r][c] == game_board[r][c+1] or game_board[r][c] == game_board[r+1][c]:
                return False
    # looks at last row and col and compares values for similar to see if you can still add
    for c in range(len(game_board)-1):
        if game_board[(len(game_board)-1)][c] == game_board[(len(game_board)-1)][c+1]:
            return False
    for r in range(len(game_board)-1):
        if game_board[r][(len(game_board)-1)] == game_board[r+1][(len(game_board)-1)]:
            return False
    return True
# TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 4, 8, 0],
          [0, 0, 0, 0]])