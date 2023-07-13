import time

class Conect4:
    def __init__(self):
        # yes, the game only really needs vertical rows, but we add horizontal ones to make checks for a winner easier!
        self.vertical_rows = [[' ' for _ in range(6)] for _ in range(7)]
        self.horizontal_rows = [[' ' for _ in range(7)] for _ in range(6)]

        self.current_player = 'X'
        self.previous_player = lambda symbol: 'O' if symbol == 'X' else 'X'
    
    def print_board(self, is_tutorial=False):
        for row in self.horizontal_rows.copy()[::-1]:
            for char in '\n| ' + ' | '.join(row) + ' |\n' + '-' * 29:
                print(char, end='', flush=True)
            time.sleep(0.06)
        
        print('\n  ', end='')
        
        for char in '   '.join('1234567'):
            print(char, end='', flush=True)
            time.sleep(0.005)
        

        if is_tutorial == False:
            print('\n')
    
    def gameboard_isValid(self):
        # if it returns 0, there are no more moves players can play.
        # if it returns False, the current player has won the game.
        # if it returns True, the game carries on
        
        # checks for available game board moves
        if ' ' not in [char for row in self.horizontal_rows for char in row]:
            return ['0']
        
        for row in self.horizontal_rows:
            if 'OOOO' in ''.join(row) or 'XXXX' in ''.join(row):
                return [False, 'horizontally']
        for row in self.vertical_rows:
            if 'OOOO' in ''.join(row) or 'XXXX' in ''.join(row):
                return [False, 'vertically']
        
        
        # this is to check diagonally, variables such as gr_i mean going right index, gu_i is going up index and so on
        # going right:
        for gr_i in range(4):
            for gu_i in range(3):
                combo_checked = []
                for gd_i in enumerate(range(gr_i, gr_i + 4)):
                    if self.vertical_rows[gd_i[1]][gd_i[0] + gu_i] == ' ':
                        break
                    combo_checked.append(self.vertical_rows[gd_i[1]][gd_i[0] + gu_i])
                if len(combo_checked) == 4 and ''.join(combo_checked) in ['OOOO', 'XXXX']:
                    return [False, 'diagonally']
        
        # going left:
        for gl_i in range(6,2,-1):
            for gu_i in range(3):
                combo_checked = []
                for gd_i in enumerate(range(gl_i, gl_i - 4, -1)):
                    if self.vertical_rows[gd_i[1]][gd_i[0] + gu_i] == ' ':
                        break
                    combo_checked.append(self.vertical_rows[gd_i[1]][gd_i[0] + gu_i])
                if len(combo_checked) == 4 and ''.join(combo_checked) in ['OOOO', 'XXXX']:
                    return [False, 'diagonally']
        
        
        # returns True if conditions aren't met
        return [True]

    def begin_tutorial(self):
        ########  TUTORIAL UNLESS CHOSEN NOT TO  ########
        time.sleep(0.1)
        
        
        for char in 'Welcome to a game of connect 4!':
            print(char, end='', flush=True)
            time.sleep(0.035)
        time.sleep(1)
        
        for char in "\nThe goal is to place your symbol 'X' or 'O' in such a way which it connects 4 times either vertically, horizontally or diagonally.":
            print(char, end='', flush=True)
            time.sleep(0.035)
        time.sleep(1.5)

        for char in "\nHeres an example of the grid which you'll be playing with:":
            print(char, end='', flush=True)
            time.sleep(0.035)
        self.print_board(is_tutorial=True)
        
        time.sleep(0.5)

        for char in "\nWhen prompted, enter a number 1-7, representing the column you want to place your symbol at.\n'X' always starts first.\nIf you don't wamt to see this tutorial again on your next game, set the skip_tutorial positional argument in your instance to True.\nI trust that you get the jist of it by now, good luck and happy playing!!":
            print(char, end='', flush=True)
            time.sleep(0.035)
        time.sleep(4)

        print('\n' * 50)
        ##################################################

    def start(self, skip_tutorial=False):
        # starts or skips the tutorial depending on the condition given 
        if skip_tutorial == False:
            self.begin_tutorial()

        # main game loop
        while True:
            self.print_board()

            # checks to see if the game is won or still valid
            required_game_status = self.gameboard_isValid()
            if True not in required_game_status:
                if '0' in required_game_status:
                    print('No more valid moves are left, nobody wins!')
                    break
                elif False in required_game_status:
                    print(f'Player with symbol {self.previous_player(self.current_player)} wins {required_game_status[1]}!!!')
                    break

            # player enters a number until valid
            while True:
                try:
                    # checks the number's validity from 1-7
                    prompt_number = int(input('Enter column choice: ==>  '))
                    if not prompt_number in range(1,8):
                        print('Please enter a valid range from 1-7!')
                        time.sleep(2)
                        continue
                    # checks if the game board already has a maxed out column
                    elif 6 - self.vertical_rows[prompt_number - 1].count(' ') == 6:
                        print('This column is full, please pick one with available space!')
                        time.sleep(2)
                        continue
                # handles a non real number being passed
                except:
                    print('Please enter a valid number!')
                    time.sleep(2)
                    continue
                # if all is well, it breaks out the loop and holds the player's choice 
                break

            # placement of the player's choice
            self.vertical_rows[prompt_number - 1][6 - self.vertical_rows[prompt_number - 1].count(' ')] = self.current_player
            self.horizontal_rows[6 - self.vertical_rows[prompt_number - 1].count(' ') - 1][prompt_number - 1] = self.current_player

            # change players turn
            self.current_player = 'O' if self.current_player == 'X' else 'X'


game = Conect4()
game.start(skip_tutorial=False) # set the 'skip_tutorial' argument to True if you want to skip the start
