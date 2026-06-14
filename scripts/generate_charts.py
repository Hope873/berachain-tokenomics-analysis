import os
import matplotlib.pyplot as plt
import numpy as np

# Set clean, professional styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available() else 'default')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Mock timeline: 12 Months
months = np.arange(1, 13)

# Simulated Data: BERA Emissions (Millions) vs Ecosystem Pool TVL (Millions)
bera_emissions = [10, 22, 35, 50, 68, 88, 110, 135, 162, 192, 225, 260]
ecosystem_tvl = [50, 75, 110, 160, 220, 300, 390, 490, 600, 720, 850, 1000]

# Plot BERA Cumulative Emissions (Left Axis)
color = '#FF6B6B'
ax1.set_xlabel('Months Post-Launch', fontweight='bold', labelpad=12)
ax1.set_ylabel('Cumulative BERA Emissions (M)', color=color, fontweight='bold')
line1 = ax1.plot(months, bera_emissions, color=color, linewidth=2.5, marker='o', label='BERA Supply')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second axis for Ecosystem TVL (Right Axis)
ax2 = ax1.twinx()
color2 = '#4D96FF'
ax2.set_ylabel('Ecosystem Pool TVL ($M)', color=color2, fontweight='bold')
line2 = ax2.plot(months, ecosystem_tvl, color=color2, linewidth=2.5, marker='s', linestyle='--', label='Ecosystem TVL')
ax2.tick_params(axis='y', labelcolor=color2)

# Grid and Layout tweaks
ax1.grid(True, linestyle=':', alpha=0.6)
plt.title('Berachain: Simulated Proof-of-Liquidity Supply Shock Mechanics', fontsize=14, fontweight='bold', pad=20)

# Combined Legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True)

plt.tight_layout()

# Save to assets directory
os.makedirs('assets', exist_ok=True)
plt.savefig('assets/supply_chart.png', dpi=300)
print("Chart generated successfully in assets/supply_chart.png")
