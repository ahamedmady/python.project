import os

def clear_sceern():
    os.system("cls")

class Player:
    def __init__(self) -> None:
        self.name = ""
        self.symbol = ""

    def chooce_name(self):
        while True:
            name = input("Enter yor name ,only letter:")
            if name.isalpha():
                self.name = name
                break
            print("invalid input should be only letters")

    def chooce_symbol(self):
        while True:
            symbol = input(f"{self.name},Enter a single letter:")
            if symbol.isalpha() and len(symbol)== 1:
                self.symbol = symbol
                break
            print("invalid input should be a single letters")
            
class menu:

    def main_menu(self):
        menu_text = """Welcome to X-O Game
                       1. Start Game
                       2. Quit Game
                       Enter yor choice (1 or 2)"""
        choice = input(menu_text)
        return choice
    
    def end_game(self):
         
        menu_text = """Game Over
                       1. Restart Game
                       2. Quit Game
                       Enter yor choice (1 or 2)"""
        choice = input(menu_text)

        return choice

class Board:

    def __init__(self) -> None:
        self.board = [str(i) for i in range(1,10)]

    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)

    def Update_board(self,choice,symbol):
        if self.is_valid_move(choice):
           self.board[choice - 1] = symbol
           return True
        return False   

    def is_valid_move(self,choice):
        return self.board[choice - 1].isdigit()
  
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]

class Game:
    def __init__(self) -> None:
        self.Player = [Player(),Player()]
        self.menu = menu()
        self.board = Board()
        self.current_player_index = 0

    def start_game(self):
        chiosc = self.menu.main_menu()
        clear_sceern()
        if chiosc == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for index, player in enumerate(self.Player, start=1):
            print(f"Player{index} : enter your detales")
            player.chooce_name()
            player.chooce_symbol()
            clear_sceern()

    def play_game(self):
        while True:
            self.play_turn()
            if self.chuck_win():
                self.congratulation_message()
                choice= self.menu.end_game()
                clear_sceern()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

            elif self.chuck_draw():
                self.Draw_Game()
                choice= self.menu.end_game()
                clear_sceern()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break


    def play_turn(self):
         player =self.Player[self.current_player_index]
         self.board.display_board()
         print(f"{player.name}$ Turn {player.symbol}")
         while True:
             try:
                 call_choice = int(input("choose a cell (1-9): "))
                 if 1<= call_choice <= 9 and self.board.Update_board(call_choice, player.symbol):
                     break
                 else:
                     print("Invalid move, try again")
             except ValueError:
                 print('please enter a number between 1 to 9')
         
         self.switch_player()
         clear_sceern()
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def chuck_win(self):
        win_combinistion = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]
        ]
        for com in win_combinistion:
            if (self.board.board[com[0]] == self.board.board[com[1]] == self.board.board[com[2]]):
                return True
                
        return False
        

    def chuck_draw(self):
        return all( not cell.isdigit() for cell in self.board.board )
    

    def congratulation_message(self):
        winner = self.Player[1 - self.current_player_index]
        print("-------------------------------------------------------")
        print(f"Congratulations {winner.name}! You have won the game!")
        print("-------------------------------------------------------")
        
    def Draw_Game(self):
        print("-------------------------------------------------------")
        print("The game is a draw! No winner this time")
        print("-------------------------------------------------------")
        

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print("Thanks for your playing")

game = Game()

game.start_game()