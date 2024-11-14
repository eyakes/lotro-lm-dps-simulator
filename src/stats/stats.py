class Stats:
    def __init__(self, crit=0, might=0, intellect=0, agility=0):
        self.crit = crit
        self.might = might
        self.intellect = intellect
        self.agility = agility
        # Additional stats can be added here (e.g., for virtues, racial traits, etc.)

    def __repr__(self):
        return f"Crit: {self.crit}, Might: {self.might}, Intellect: {self.intellect}, Agility: {self.agility}"
