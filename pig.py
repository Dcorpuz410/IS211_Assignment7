import random


class Pig:

    def __init__(self):
        self.die = Dice()
        self.p1 = Player('Player 1')
        self.p2 = Player('Player 2')

    def play(self):
        while self.p1.score < 100 and self.p2.score < 100:
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()
        if self.p1.score > self.p2.score:
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')


class Player:

    def __init__(self, title):
        self.name = title
        self.score = 0
        self.die = Dice(6)

    def move(self):
        round_score = 0
        again = 'y'
        # creating a while loop for the player's turn
        while again == 'y':
            self.die.roll()
            roll = self.die.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score + roll
                print("{}'s round score is {}".format(self.name, round_score))
                again = input('roll again? (y/n)')
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))


class Dice:

    def __init__(self, n=6):
        self.sides = n
        self.roll()

    # I believe this line is what is causing my trouble, but I am stuck as to what I did wrong here
    def roll(self):
        self.value = int(random.random() * self.sides + 1)


if __name__ == "__main__":
    print('Welcome to the Pig game!')
    game = Pig()
    game.play()
    print('Bye')