class GearItem:
    def __init__(self, name, stat_boosts):
        """stat_boosts should be a dictionary like {'crit': 10, 'might': 5}"""
        self.name = name
        self.stat_boosts = stat_boosts

    def apply_stats(self, stats):
        """Apply the gear item stat boosts to the current stats."""
        for stat, value in self.stat_boosts.items():
            if stat in stats:
                stats[stat] += value
            else:
                stats[stat] = value  # Add the stat if it doesn't exist
