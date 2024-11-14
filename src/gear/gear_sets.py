class GearSet:
    def __init__(self, gear_items):
        self.gear_items = gear_items

    def apply_to_stats(self, stats):
        """Apply the full gear set to the stats."""
        for item in self.gear_items:
            item.apply_stats(stats)
