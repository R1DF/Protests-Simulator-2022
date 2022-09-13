# Package import
from random import randint

# Internal import
from .item import Item

# Apple class
class DiceOfFate(Item):
    def __init__(self, holder):
        Item.__init__(self, holder, "DICE_OF_FATE", "Dice of Fate")

    def use(self):
        new_luck = randint(1, 100)
        print("You shook the die...")
        if new_luck > self.holder.luck and new_luck > 80:
            print("Perfect! You feel like you've received a blessing.")
        elif self.holder.luck < new_luck < 80:
            print("You feel like something changed for the better.")
        elif new_luck == self.holder.luck:
            print("... You felt nothing. Too bad.")
        elif self.holder.luck > new_luck > 30:
            print("Uh oh... You feel a stomachache...")
        else:
            print("The die bounced off to nowhere, watching your luck fall exponentially. What a disaster!")
        self.holder.luck = new_luck
        self.dispose()

