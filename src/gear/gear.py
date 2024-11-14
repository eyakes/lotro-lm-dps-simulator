class GearItem:
    def __init__(self, name, stat_boosts):
        """stat_boosts should be a dictionary like {'crit': 10, 'might': 5}"""
        self.name = name
        self.stat_boosts = stat_boosts

    def apply_stats(self, stats):
        """Apply the gear item stat boosts to the current stats."""
        for stat, value in self.stat_boosts.items():
            stats[stat] += value

class GearSet:
    def __init__(self, gear_items):
        self.gear_items = gear_items

    def apply_to_stats(self, stats):
        """Apply the full gear set to the stats."""
        for item in self.gear_items:
            item.apply_stats(stats)
