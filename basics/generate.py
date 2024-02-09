from random import choice, randint, shuffle
from statistics import mean

coin = choice(["heads", "tails"])
# we can perform the same idea in another way:
number = randint(1, 10)

cards = ["Jack", "Queen", "king"]
shuffle(cards)
# Note THAT SHUFFLE FUNCTION SHUFFELS THE LIST ITSELF DON'T RETURN THE SHUFFLED VALUES
print(coin, number)
for card in cards:
    print(card)

# using statistics library
my_grades = [100, 98, 99, 87, 88, 82]
print(f"your average grade is {int(mean(my_grades))}")
