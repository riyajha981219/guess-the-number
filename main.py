"""
Guess the number game
Computer will choose a random number between 1 to 100 and user has to guess what number is it
"""
import random

"""Global variables"""
divisors = [5, 3, 2]
length = len(divisors)
var = random.randint(1, 10)

"""Class that runs the program"""


class Guess:
    def checkWin(self, go=True):
        count = 0

        """While 'true'"""

        while go:
            guess = int(input("Guess the number between 1 and 10: "))
            while guess not in range(1, 11, 1):
                guess = int(input("Please enter valid input: "))
            print()

            """if you guessed right or not!!"""

            if guess == var:
                go = False

            else:
                if (len(divisors) > 0):
                    choice = input("Do you want a hint? (Y/N): ").lower()

                    """Do you want hint?"""
                    while choice not in ["y", "n"]:
                        choice = input("Enter Y or N: ")
                    if choice == "N":
                        continue
                    else:
                        """Only 3 hints given"""

                        if (len(divisors) > 0):
                            print(
                                f"\nThe modulus of the number is {var%divisors[0]} with {divisors[0]}\n")
                            divisors.remove(divisors[0])
                            count += 1
                        else:
                            go = False
                else:
                    """If no. of hints over! Game over!"""
                    go = False

        """Check if winner lost or won!"""
        if guess == var:
            print(
                f"Yas! You intelligent one!!😎 \nThe answer was in fact: {var}")

        else:
            print(
                f"Better luck next time buddy !🙄\nThe right answer was: {var}")

        """The end"""
        print("*" * 30)
        print("Thanks for playing!!")
        print("*" * 30)


play = Guess()
play.checkWin()
