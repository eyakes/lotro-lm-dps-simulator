class GearSet:
    def __init__(self, gear_items):
        """gear_items is expected to be a list of GearItem objects"""
        self.gear_items = gear_items

    def apply_to_stats(self, stats):
        """Apply the full gear set to the stats by applying each GearItem's stats."""
        for item in self.gear_items:
            item.apply_stats(stats)  # Use the apply_stats method of each GearItem
