# This is the new object-oriented code for your player.py file

class Stats:
    """
    Encapsulates all the numerical stats for a player.
    """
    def __init__(self, max_health, strength, dexterity, intelligence):
        self.max_health = max_health
        self.current_health = max_health
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def decrease_health(self, amount):
        """Decreases health but not below zero."""
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0
        print(f"Health is now {self.current_health}/{self.max_health}")


class Player:
    """
    Represents the player and all their data, including stats, history, etc.
    """
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience_points = 0
        self.stats = Stats(max_health=100, strength=10, dexterity=5, intelligence=5)

        # We can include the other player data here too
        self.visited_scenes = []
        self.history = []
        self.vars = {}

    def take_damage(self, amount):
        """Delegates taking damage to the stats object."""
        print(f"{self.name} takes {amount} damage!")
        self.stats.decrease_health(amount)
        if self.stats.current_health == 0:
            print(f"{self.name} has been defeated!")

    def gain_experience(self, amount):
        self.experience_points += amount
        print(f"{self.name} gains {amount} XP.")
        self.level_up()

    def level_up(self):
        """Checks if the player has enough XP to level up."""
        experience_needed = self.level * 100
        if self.experience_points >= experience_needed:
            self.level += 1
            self.experience_points -= experience_needed
            self.stats.max_health += 20
            self.stats.current_health = self.stats.max_health
            self.stats.strength += 2
            print(f"LEVEL UP! {self.name} is now Level {self.level}!")
