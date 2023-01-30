import numpy as np
import random

# We use random.seed(0) to make sure
# that our random always returns the same result
random.seed(0)

def initialize():
    """
    This function creates a numpy 3x3 array 
    that initializes every value to equal 3
    """
    # TODO: Fill in numpy arrays so that we have a 3x3 board filled with values 3 [this marks as empty]
    # NOTE: Our array is 3x3 and every index value should be 3 (blank spot)
    # 0's act as O's
    # 1's act as X's
    # 3's act as placeholders for blank spots
    board = np.full((3, 3), 3)
    return board
    
def choose_starting_player():
    """ 
    This function chooses the starting player and returns the player
    it uses random to select the starting player
    return value 0 = computer goes first
    return value 1 = player goes first
    """
    # TODO: Fill the coin flip to decide if 0 or 1 goes first and return the value
    # Flip a coin to see who goes first with X's
    # return integer (0 or 1)
    player = np.random.randint(0, 2)
    
    if player == 1:
        print("You go first. Your letter is X.")
    return player
        
# Converts internal numpy array into a visual ASCII board.       
def display_board(board):
    """
    This function displays the board
    When printing, follow these conventions:
    index entry 0 = 'O'
    index entry 1 = 'X'
    index entry 3 = ' ' (empty spot)
    """
    # TODO: Fill this board list with X,O or ' ' (empty) depending on the situation
    # The board_list should be a list (not a numpy Matrix!)
    board_list = []
    
    for array in board:
        for value in array:
            if value == 0:
                board_list.append("O")
            elif value == 1:
                board_list.append("X")
            elif value == 3:
                board_list.append(" ")
            else:
                None

    # NOTE: print function already displays the board_list, you just have to fill it properly    
    
    # END OF TODO 
    
    # inputs O's, X's, and blank spots into an ASCII tictactoe board
    print("""
 {} | {} | {}
---+---+---
 {} | {} | {}
---+---+---
 {} | {} | {}
""".format(*board_list))
    
    
def return_open_slots(board):
    # Checks for open slots using Boolean arrays.
    # Important when checking for winner (if draw) and checking if user's input...
    # ...is valid
    open_slots = []

    bool_arr = (board == 3)
    flat_bool_arr = bool_arr.flatten()
    
    # is spot taken by 3's? If so, then spot is open.
    # appends (i + 1) because inputs are indexed to 1
    for i in range(0, len(flat_bool_arr)):
        if flat_bool_arr[i] == True:
            open_slots.append(i + 1)
            
    return open_slots


def notify_game_end(active_player):
    # if active_player is 1, declare user to be winner
    # if active_player is 0, declare the computer to be winner
    if active_player == 1:
        print("You win!")
    elif active_player == 0:
        print("You lost!")
    else:
        print("Draw!")
        
def check_for_winner(active_player, board):
    """ 
    Checks for a winner, going through rows and comparing if active_player just managed to fill the slots
    """
    for i in range(0, 3):
    # Checks rows and columns for match
        rows_win = (board[i, :] == active_player).all()
        cols_win = (board[:, i] == active_player).all()
        
        if rows_win or cols_win:
            return True
            
    diag1_win = (np.diag(board) == active_player).all()
    diag2_win = (np.diag(np.fliplr(board)) == active_player).all()
    
    if diag1_win or diag2_win:
    # Checks both diagonals for match
        return True
    else:
        return False


def place_letter(active_player, input_location, board):
    
    """
    This function places the letter of the active_player
    to the given location input number (1-9)
    """
    # TODO: Place the active_player value 
    # to the the input_location at the board
    
    if input_location == 1:
        board[0][0] = active_player
    elif input_location == 2:
        board[0][1] = active_player
    elif input_location == 3:
        board[0][2] = active_player
    elif input_location == 4:
        board[1][0] = active_player
    elif input_location == 5:
        board[1][1] = active_player
    elif input_location == 6:
        board[1][2] = active_player
    elif input_location == 7:
        board[2][0] = active_player
    elif input_location == 8:
        board[2][1] = active_player
    elif input_location == 9:
        board[2][2] = active_player
    else:
        None

def player_turn(board):
    display_board(board)
    
    # TODO: Read user input as user_input and cast it as integer
    user_input = int(input("Pick an open slot:\n"))
    
    # End of TODO
    # Now, the code continues operation
    if user_input in return_open_slots(board):
        place_letter(1, user_input, board)
    else:
        # NOTE: Notice how this function calls itself if the slot is not open!
        print("That's not a open slots.")
        player_turn(board)
    

def comp_turn(board):
    # Randomly chooses from open_slots to place its letter    
    open_slots = return_open_slots(board)
    comp_input = random.choice(open_slots)
    place_letter(0, comp_input, board)
    
def change_player(active_player):
    if active_player == 0:
        return 1
    else:
        return 0

def main():
    # Initialize everything
    running = True
    turn_number = 1
    board = initialize()
    active_player = choose_starting_player()
    while running:
        # Lets run the logic
        if active_player == 0:
            comp_turn(board)
        elif active_player == 1:
            player_turn(board)
        
        # Check if someone won?
        winner = check_for_winner(active_player, board)
        if winner:
            display_board(board)
            notify_game_end(active_player)
            running = False
            break
        # Check if the turn_number is 9 (same as full board!)
        if turn_number == 9:
            display_board(board)
            notify_game_end(-1)
            running = False
            break
        
        # If not, set the turn for the next player
        turn_number += 1
        active_player = change_player(active_player)

main()
