class Fireball:
    def __init__(self):
        self.name = "Fireball"
        self.damage = 100
        self.cost = 20  # Mana or resource cost
        self.cooldown = 3  # Seconds
        
    def __repr__(self):
        return self.name
