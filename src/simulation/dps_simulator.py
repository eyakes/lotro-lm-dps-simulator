class Ability:
    def __init__(self, name, damage, cost, cooldown):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.cooldown = cooldown
        self.last_used = -self.cooldown  # Start the ability off cooldown

    def can_use(self, current_time):
        return current_time - self.last_used >= self.cooldown

    def use(self, current_time):
        self.last_used = current_time
        return self.damage


class DPS_Simulator:
    def __init__(self, abilities, stats):
        self.abilities = abilities  # List of Ability objects
        self.stats = stats          # Dictionary of character stats
        self.time = 0               # Time in seconds, starting at 0
        self.dps = 0                # Total DPS calculated
        self.rotation_order = []    # Define the rotation order

    def set_rotation(self, rotation_order):
        self.rotation_order = rotation_order

    def run_simulation(self, duration=60):
        """Simulates the DPS over a given duration."""
        total_damage = 0
        for current_time in range(duration):
            for ability in self.rotation_order:
                if ability.can_use(current_time):
                    total_damage += ability.use(current_time)
        
        self.dps = total_damage / duration
        return self.dps
