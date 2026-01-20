#
#
#

import random
import time
import sys

class MindGame:
    # CLI implementation of the classic math-based mind game

    def __init__(self):
        # The Master List: All even numbers from 2 to 100
        # range(start, stop, step) is exclusive of the 'stop' value
        self.all_options: list[int] = [i for i in range(2, 102, 2)]
        self.secret_modifier: int = 0

    def clear_step(self, message: str) -> None:
        # Standardizes the prompt for each game step
        print(f"\n[STEP] {message}")
        input(">> Press ENTER when ready...")

    def get_random_sample(self) -> list[int]:
        """Returns 4 unique random numbers from the master list."""
        return random.sample(self.all_options, 4)

    def play(self) -> None:
        # Executes the game logic
        print("--- [Welcome to The Mind Game] ---")
        
        # Initial validation
        ready = input("Ready for your mind to be read? (Y/N): ").strip().upper()
        if ready != "Y":
            print("Come back when you're ready! Bye now :D")
            sys.exit()

        # Step 1 & 2
        self.clear_step("Pick a random whole number in your mind!")
        self.clear_step("Multiply that number by 2.")

        # Step 3: The Random Variable
        choices = self.get_random_sample()
        print(f"\nPick one of these numbers and add it to your total: {choices}")
        
        while True:
            try:
                pick = int(input("Input the number you picked: "))
                if pick in choices:
                    self.secret_modifier = pick
                    break
                print(f"Please choose a valid number listed: {choices}")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        # Step 4 & 5
        self.clear_step("Now divide your current total by 2.")
        self.clear_step("Subtract the original number you picked in your mind.")

        # Final Reveal
        print("\n" + "-" * 30)
        print("Reading your thoughts...")
        time.sleep(1.5)
        
        result = self.secret_modifier / 2
        print(f"\nYour FINAL number is: {int(result)}")
        print("-" * 30)
        print("MENTAL! INNIT? :p\n")

if __name__ == "__main__":
    game = MindGame()
    game.play()