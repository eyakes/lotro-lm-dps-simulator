import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# src/main.py
from abilities.fireball import Fireball
from gear.gear import GearItem
from stats.stats import Stats
from simulation.dps_simulator import DPS_Simulator

# Create a stats object
stats = Stats(crit=0.2, might=100)

# Create gear items and apply them to stats
gear_item = GearItem(name="Crit Ring", stat_boosts={'crit': 0.1})
gear_item.apply_to_stats(stats)

# Create abilities
fireball = Fireball()

# Initialize simulator
simulator = DPS_Simulator([fireball], stats)

# Run simulation
dps = simulator.run_simulation(duration=60)
print(f"Estimated DPS: {dps}")
