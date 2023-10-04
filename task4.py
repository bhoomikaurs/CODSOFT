import random


class RockPaperScissors:
    def __init__(self):
        self.computerScore = 0
        self.yourScore = 0

    def display_score(self):
        print("              Score             ")
        print("       You          Computer    ")
        print("{: ^16}{:^16}".format(self.yourScore, self.computerScore))

    def display_choice(self, you, computer):
        print("  You   :", self.full_name(you))
        print("Computer:", self.full_name(computer))

    @staticmethod
    def computer_random_choice():
        return random.choice(['r', 'p', 's'])

    @staticmethod
    def full_name(opt):
        names = {'r': "Rock", 'p': "Paper", "s": "Scissor"}
        return names[opt]

    def game(self):
        you = input("\n\nRock, Paper, or Scissor: ").lower()
        if you not in "rps":
            print("Invalid Input")
            return
        comp = self.computer_random_choice()
        if you == comp:
            print("\n          Tie ")
        elif (you == 'r' and comp == 's') or (you == 's' and comp == 'p') or (you == 'p' and comp == 'r'):
            print("\n       You Won ")
            self.yourScore += 1
        else:
            print("\n       You lost ")
            self.computerScore += 1
        self.display_choice(you, comp)
        self.display_score()


if __name__ == "__main__":
    game_instance = RockPaperScissors()
    while True:
        game_instance.game()
