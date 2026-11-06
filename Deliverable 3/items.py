"""
Task 3: Weapon class
Items.py contains the Weapon class, which represents a weapon that can be equipped by a character. 
The damage dealt by the weapon is determined by rolling a dice, which is represented by the Dice class in dice.py.
The Weapon class has methods to roll the damage and to provide a string representation of the weapon.
"""

# Task 3: Weapon class

from dice import Dice


class Weapon:
    """A weapon whose damage is decided by a dice roll."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon.

        Args:
            name (str): Name of the weapon, e.g. "Sword".
            damage_dice (Dice): The dice rolled to find the damage.
        """
        if not isinstance(damage_dice, Dice):
            raise TypeError("damage_dice must be an instance of Dice")
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's dice and return the damage."""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation like Weapon(name='Sword', damage_dice=Dice(sides=4))."""
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice!r})"


if __name__ == "__main__":
    sword = Weapon("Sword", Dice(4))
    print(sword)
    rolls = [sword.roll_damage() for _ in range(1000)]
    print(min(rolls), max(rolls))

    try:
        Weapon("Stick", 6)
    except TypeError as error:
        print("TypeError:", error)


