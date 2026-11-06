"""
Object-oriented game simulator - Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
Character.py is an updated version of the original, with a Weapon class added. The Weapon class is in items.py, and the Dice class is in dice.py.
Task 1: Character class and Task 3: Weapon class are implemented in this file. The Character class can now take a Weapon object and use it in attacks.
Task 1 says make a Character class with attributes for name, hp_max, damage, and methods for attack, take_damage, heal, and introduce. 
Task 3 adds the ability for a Character to have a Weapon, which uses a Dice object to determine damage.
"""

# Task 1 + Task 3: Character class with Weapon support

from items import Weapon


class Character:
    """Represents a character in the RPG."""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, 
                 weapon: Weapon | None = None) -> None:
        """
        Initialise the Character.

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100).
            damage (int): Base damage when attacking without a weapon (default = 10).
            weapon (Weapon | None): Optional equipped weapon (default = None).
        """
        self.name = name
        self.hp_max = hp_max
        self._hp = hp_max  # private: only changed by take_damage() and heal()
        self.damage = damage
        self.weapon = weapon

    @property
    def hp(self) -> int:
        """Current hit points (read-only)."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """True if the character has more than 0 HP (read-only)."""
        return self._hp > 0

    def take_damage(self, amount: int) -> None:
        """Reduce own HP by ``amount``. HP never goes below 0."""
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increase own HP by ``amount``. HP never goes above hp_max."""
        if amount < 0:
            raise ValueError("Healing cannot be negative")
        if not self.is_alive:
            return  # a dead character cannot be healed (our choice)
        self._hp = min(self._hp + amount, self.hp_max)

    def roll_attack_damage(self) -> int:
        """Return how much damage this character deals right now."""
        if self.weapon is not None:
            return self.weapon.roll_damage()
        return self.damage

    def attack(self, target: "Character") -> int:
        """Attack ``target`` and return the damage dealt."""
        damage = self.roll_attack_damage()
        target.take_damage(damage)
        return damage

    def introduce(self) -> None:
        """Print a short introduction."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of the character object."""
        return f"<{type(self).__name__} name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """Readable description of the character."""
        return f"{type(self).__name__}: {self.name} with {self.hp} HP and {self.damage} damage"


if __name__ == "__main__":
    from dice import Dice  # only needed for the tests below

    # Task 1 tests
    c = Character("Test")
    c.take_damage(150)
    print(c.hp, c.is_alive)              # expected: 0 False

    c = Character("Test")
    c.take_damage(30)
    c.heal(50)
    print(c.hp)                          # expected: 100 (not 120)

    link = Character("Link")
    sauron = Character("Sauron")
  
    link.attack(sauron)
    print(sauron.hp)                     # expected: 90

    try:
        sauron.hp = 999
    except AttributeError as error:
        print("AttributeError:", error)  # expected: hp cannot be set from outside

    try:
        c.take_damage(-5)
    except ValueError as error:
        print("ValueError:", error)      # expected: Damage cannot be negative

    # Task 3 tests
    dummy = Character("Dummy", hp_max=1000)
    a = Character("A")
    print("Damage on dummy (no weapon):  ", [a.attack(dummy) for _ in range(5)])   # always 10
    zelda = Character("Zelda", weapon=Weapon("Sword", Dice(20)))
    print("Damage on dummy with weapon:", [zelda.attack(dummy) for _ in range(5)])            # random 1-20
