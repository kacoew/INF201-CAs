"""
Battle.py

Task 5: Running battles

Create a Battle class to manage turn-based combat between two
Character objects.
"""

from character import Character, Warrior, Mage


class Battle:
    """Manages a turn-based battle between two characters."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the Battle.

        Args:
            hero (Character): The player's character.
            enemy (Character): The opposing character.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        Play one round of combat.

        The hero attacks first. If the enemy survives,
        the enemy attacks the hero.
        """
        hero_damage = self.hero.attack(self.enemy)
        print(f"{self.hero.name} deals {hero_damage} damage.")

        if self.enemy.is_alive:
            enemy_damage = self.enemy.attack(self.hero)
            print(f"{self.enemy.name} deals {enemy_damage} damage.")

    def simulate_battle(self) -> Character:
        """
        Run battle rounds until one character dies.

        Returns:
            Character: The winning character.
        """
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.hero.is_alive:
            return self.hero

        return self.enemy


if __name__ == "__main__":

    # Test 1: Warrior vs Character
    hero = Warrior("Aragorn")
    enemy = Character("Orc")

    battle = Battle(hero, enemy)

    winner = battle.simulate_battle()

    print(f"\nWinner: {winner.name}")
    print(f"{hero.name}: {hero.hp} HP")
    print(f"{enemy.name}: {enemy.hp} HP")

    print("\n" + "-" * 30 + "\n")

    # Test 2: Warrior vs Mage
    hero = Warrior("Aragorn")
    enemy = Mage("Saruman")

    battle = Battle(hero, enemy)

    winner = battle.simulate_battle()

    print(f"\nWinner: {winner.name}")
    print(f"{hero.name}: {hero.hp} HP")
    print(f"{enemy.name}: {enemy.hp} HP")