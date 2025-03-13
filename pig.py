import random

class Die:
    """A class representing a six-sided die."""
    def __init__(self, seed=0):
        random.seed(seed)
        self.value = 0

    def roll(self):
        """Roll the die and return the result."""
        self.value = random.randint(1, 6)
        return self.value

class Player:
    """A class representing a player in the Pig game."""
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_to_score(self, points):
        """Add points to the player's total score."""
        self.total_score += points

    def reset_turn(self):
        """Reset the turn (for when a 1 is rolled)."""
        return 0

class PigGame:
    """A class representing the Pig game."""
    def __init__(self):
        self.die = Die()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player = 0

    def switch_turn(self):
        """Switch the current player."""
        self.current_player = 1 - self.current_player

    def play_turn(self):
        """Handle a single turn of the current player."""
        player = self.players[self.current_player]
        turn_total = 0

        print(f"\n{player.name}'s turn. Current score: {player.total_score}")

        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled a {roll}")

            if roll == 1:
                print(f"Bad luck! {player.name} loses their turn with no points gained.")
                turn_total = player.reset_turn()
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}, Total score if held: {player.total_score + turn_total}")

                decision = input("Enter 'r' to roll again or 'h' to hold: ").lower()
                while decision not in ['r', 'h']:
                    decision = input("Invalid input. Enter 'r' to roll again or 'h' to hold: ").lower()

                if decision == 'h':
                    player.add_to_score(turn_total)
                    break

        self.switch_turn()

    def play_game(self):
        """Play the full game until a player reaches 100 points."""
        print("Welcome to Pig!")

        while all(player.total_score < 100 for player in self.players):
            self.play_turn()

        winner = max(self.players, key=lambda p: p.total_score)
        print(f"\nCongratulations! {winner.name} wins with a score of {winner.total_score}!")

if __name__ == "__main__":
    game = PigGame()
    game.play_game()