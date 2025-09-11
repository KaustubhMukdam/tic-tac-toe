import random
import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Shows what number corresponds to what box on the board
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If valid move, then make it and return True
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


# Player Classes
class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (1-9): ')
            try:
                val = int(square) - 1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # If the board is empty, choose a random corner or center
            square = random.choice([0, 2, 4, 6, 8])
        else:
            # Use minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # AI player
        other_player = 'O' if player == 'X' else 'X'

        # Base case: check if previous move was winning
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximize
        else:
            best = {'position': None, 'score': math.inf}  # Minimize

        for possible_move in state.available_moves():
            # Make the move
            state.make_move(possible_move, player)
            
            # Recurse using minimax
            sim_score = self.minimax(state, other_player)

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # Update the best move
            if player == max_player:  # Maximize the max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # Minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    
    # While the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square + 1}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')


def get_user_choice():
    """Get and validate user's menu choice"""
    while True:
        try:
            choice = input("\nSelect game mode (1-5) or 'quit' to exit: ").strip().lower()
            if choice in ['quit', 'q', 'exit']:
                return 'quit'
            choice_num = int(choice)
            if 1 <= choice_num <= 5:
                return str(choice_num)
            else:
                print("Please enter a number between 1-5 or 'quit' to exit.")
        except ValueError:
            print("Invalid input. Please enter a number between 1-5 or 'quit' to exit.")


def ask_play_again():
    """Ask user if they want to play again"""
    while True:
        choice = input("\nDo you want to play again? (y/n) or 'quit' to exit: ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no', 'quit', 'q', 'exit']:
            return False
        else:
            print("Please enter 'y' for yes, 'n' for no, or 'quit' to exit.")


def run_single_game(choice):
    """Run a single game based on user's choice"""
    if choice == '1':
        # Human vs Human
        x_player = HumanPlayer('X')
        o_player = HumanPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player)
        
    elif choice == '2':
        # Human vs Easy AI
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player)
        
    elif choice == '3':
        # Human vs Hard AI
        x_player = HumanPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player)
        
    elif choice == '4':
        # Easy AI vs Hard AI simulation
        print("\nRunning 5 games between Easy AI (X) and Hard AI (O):")
        print("=" * 50)
        x_wins = 0
        o_wins = 0
        ties = 0
        
        for i in range(5):
            print(f"\nGame {i + 1}:")
            print("-" * 20)
            x_player = RandomComputerPlayer('X')
            o_player = SmartComputerPlayer('O')
            t = TicTacToe()
            result = play(t, x_player, o_player, print_game=True)
            
            if result == 'X':
                x_wins += 1
                print("Easy AI (X) wins this game!")
            elif result == 'O':
                o_wins += 1
                print("Hard AI (O) wins this game!")
            else:
                ties += 1
                print("This game is a tie!")
            
            if i < 4:  # Don't ask to continue after the last game
                input("Press Enter to continue to next game...")
        
        print(f"\nFinal Results:")
        print(f"Easy AI (X) wins: {x_wins}")
        print(f"Hard AI (O) wins: {o_wins}")
        print(f"Ties: {ties}")
        
    elif choice == '5':
        # Hard AI vs Hard AI simulation
        print("\nRunning 5 games between Hard AI (X) and Hard AI (O):")
        print("=" * 50)
        x_wins = 0
        o_wins = 0
        ties = 0
        
        for i in range(5):
            print(f"\nGame {i + 1}:")
            print("-" * 20)
            x_player = SmartComputerPlayer('X')
            o_player = SmartComputerPlayer('O')
            t = TicTacToe()
            result = play(t, x_player, o_player, print_game=True)
            
            if result == 'X':
                x_wins += 1
                print("Hard AI X wins this game!")
            elif result == 'O':
                o_wins += 1
                print("Hard AI O wins this game!")
            else:
                ties += 1
                print("This game is a tie!")
            
            if i < 4:  # Don't ask to continue after the last game
                input("Press Enter to continue to next game...")
        
        print(f"\nFinal Results:")
        print(f"Hard AI (X) wins: {x_wins}")
        print(f"Hard AI (O) wins: {o_wins}")
        print(f"Ties: {ties}")


def main():
    """Main game loop with do-while structure"""
    print("🎮 Welcome to Tic Tac Toe! 🎮")
    print("=" * 40)
    
    # Main game loop (do-while structure)
    while True:
        print("\nGame modes:")
        print("1. Human vs Human")
        print("2. Human vs Easy AI")
        print("3. Human vs Hard AI") 
        print("4. Easy AI vs Hard AI (simulation)")
        print("5. Hard AI vs Hard AI (simulation)")
        
        # Get user's choice
        choice = get_user_choice()
        
        # Check if user wants to quit
        if choice == 'quit':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        print(f"\n🎯 Starting game mode {choice}...")
        print("-" * 30)
        
        # Run the selected game
        run_single_game(choice)
        
        # Ask if user wants to play again
        if not ask_play_again():
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        # Clear screen effect
        print("\n" + "=" * 40)


# Run the game
if __name__ == '__main__':
    main()
