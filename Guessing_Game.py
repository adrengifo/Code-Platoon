import random


class GuessingGame():
    # print('hello')
    solved = False

    def __init__(self, number):
        self.number = number

    def guess(self, user_guess):
        if int(user_guess) < self.number:
            print('low')
        elif int(user_guess) > self.number:
            print('high')
        else:
            GuessingGame.solved = True
            print('correct')
        return 1

game = GuessingGame(random.randint(1, 100))
last_guess = None
last_result = None
# print(game.solved)
while game.solved is False:
    if last_guess is not None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess = input("Enter your guess: ")
    last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")
