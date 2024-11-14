# src/simulation/dps_simulator.py
class DPS_Simulator:
    def __init__(self, abilities, stats):
        self.abilities = abilities
        self.stats = stats

    def run_simulation(self, duration=60):
        total_damage = 0
        for current_time in range(duration):
            for ability in self.abilities:
                total_damage += ability.use(self.stats)
        dps = total_damage / duration
        return dps
