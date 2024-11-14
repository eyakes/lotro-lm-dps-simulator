import sys
import os

# Ensure the src directory is included in the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/data')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/gear')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/abilities')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/gstats')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/rotations')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/simulation')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/api')))

# src/main.py
from fireball import Fireball
from gear import GearItem
from gear_sets import GearSet
from stats import Stats
from dps_simulator import DPS_Simulator

# Create a stats object
stats = {'crit': 10, 'might': 5, 'fate': 8}

# Create gear items and apply them to stats
gear1 = GearItem('Helm of Might', {'crit': 5, 'might': 3})
gear2 = GearItem('Boots of Speed', {'fate': 2, 'might': 1})
gear3 = GearItem('Ring of Power', {'crit': 3})

# Apply stats from each Gear Item
gear1.apply_stats(stats)
gear2.apply_stats(stats)
gear3.apply_stats(stats)

# Create abilities
fireball = Fireball()

# Initialize simulator
simulator = DPS_Simulator([fireball], stats)

# Run simulation
dps = simulator.run_simulation(duration=60)
print(f"Estimated DPS: {dps}")
