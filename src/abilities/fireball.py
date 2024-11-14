# src/abilities/fireball.py
import random

class Fireball:
    def __init__(self, crit_multiplier=1.5):
        self.name = "Fireball"
        self.damage = 100
        self.cost = 20  # Mana or resource cost
        self.cooldown = 3  # Seconds
        self.crit_multiplier = crit_multiplier

    def use(self, stats):
        # Apply crit chance using dictionary access for 'crit'
        if stats['crit'] > random.random():  # stats['crit'] instead of stats.crit
            return self.damage * self.crit_multiplier
        return self.damage
