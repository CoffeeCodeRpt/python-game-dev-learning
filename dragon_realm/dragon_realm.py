from slow_print import slow_print
from get_dragon_cave import get_dragon_cave

# The story is presented to the users.
story = """You are in a land full of dragons. In front of you, you see two caves.
In one cave, the dragon in friendly and will share his treasure with you.
In the other, the dragon is greedy and hungry, and will eat you on sight.
Which cave will you go into? 1 or 2?
"""

slow_print(story)

# The user must choose which cave to enter
answer = input()

while answer != '1' and answer != '2':
    print(f"{answer} is not a valid answer. Please choose 1 or 2")
    answer = input()

# The dragon is either good or evil and the player will win or lose.
friend = get_dragon_cave()

# The player is congratulated or consoled depending on the outcome.
approach = "You approach the cave. Slowly. So slowly..."
slow_print(approach)
if answer == friend:
    conclusion = """The cave is dark and spooky. Right as you step inside, a large dragon jumps ou at you!
Jaws open wide!...
and the dragon screams with joy as he passes you a treasure chest and a golden goblet.
You open the chest and find a large pile of gold and jewels. 
You open the goblet and find a small dragon.
You are now the proud owner of a small dragon.
"""

    slow_print(conclusion)
else:
    conclusion = """The cave is dark and spooky. Right as you step inside, a large dragon jumps ou at you!
Jaws open wide!...
and the dragon roars with delight as it eats you.
You are dead."""

    slow_print(conclusion)

