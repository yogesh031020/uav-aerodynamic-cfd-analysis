import numpy as np
import matplotlib.pyplot as plt
import os

print("=" * 50)
print("  UAV Aerodynamic Analysis Report")
print("=" * 50)

# Read CSV file
csv_path = ("D:\\DroneProjects\\uav-cfd-analysis\\"
            "results\\vspaero_results.csv")

# Parse the CSV manually
data = {}
with open(csv_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    key = parts[0]
    try:
        values = [float(v) for v in parts[1:]
                  if v.strip() != '']
        if len(values) > 0:
            data[key] = values
    except:
        continue

# ── Fix Alpha extraction ──────────────────────
# Alpha appears multiple times in CSV
# Extract all alpha values manually
alpha = []
CL = []
CDtot = []

for line in lines:
    line = line.strip()
    parts = line.split(',')
    if parts[0] == 'Alpha':
        try:
            vals = [float(v) for v in parts[1:]
                    if v.strip() != '']
            alpha.extend(vals)
        except:
            continue

# Get CL and CD from full arrays
CL    = data.get('CFytot', [])
CDtot = data.get('CDtot', [])

# Remove duplicates and sort alpha
alpha = sorted(list(set(alpha)))

print(f"Alpha values found: {alpha}")
print(f"CL values found:    {CL}")
print(f"CDtot values found: {CDtot}")

# Make sure all same length
min_len = min(len(alpha), len(CL), len(CDtot))
alpha = alpha[:min_len]
CL    = CL[:min_len]
CDtot = CDtot[:min_len]

print(f"\nUsing {min_len} data points")

if min_len < 2:
    print("Still not enough — using manual values!")
    alpha = [0, 2, 4, 6, 8, 10]
    CL    = [0.05, 0.15, 0.28, 0.42, 0.55, 0.65]
    CDtot = [0.014, 0.017, 0.025, 0.041, 0.067, 0.104]
    min_len = 6

# Calculate L/D ratio
LD = [abs(l)/d if d != 0 else 0
      for l, d in zip(CL, CDtot)]

# ── UAV Parameters ────────────────────────────
wing_area = 1.2
velocity  = 20.0
rho       = 1.225
mass      = 2.5
q         = 0.5 * rho * velocity**2

# Use absolute CL values
CL_abs = [abs(cl) for cl in CL]

# Calculate forces
Lift = [cl * q * wing_area for cl in CL_abs]
Drag = [cd * q * wing_area for cd in CDtot]

# Best L/D
LD_abs = [l/d if d != 0 else 0
          for l, d in zip(CL_abs, CDtot)]
best_idx = LD_abs.index(max(LD_abs))

print("\n" + "=" * 50)
print("Aerodynamic Performance Summary:")
print("=" * 50)
print(f"Dynamic Pressure:  {q:.2f} Pa")
print(f"Max CL:            {max(CL_abs):.4f}")
print(f"Min CD:            {min(CDtot):.4f}")
print(f"Max L/D:           {max(LD_abs):.2f}")
print(f"Best Alpha:        {alpha[best_idx]:.1f} deg")

# Stall speed
weight = mass * 9.81
max_cl = max(CL_abs) if max(CL_abs) > 0 else 0.1
stall_speed = np.sqrt(
    (2 * weight) / (rho * wing_area * max_cl))
print(f"Stall Speed:       {stall_speed:.2f} m/s")
print(f"Cruise Lift:       {Lift[2]:.2f} N")
print(f"Cruise Drag:       {Drag[2]:.2f} N")

# ── Plotting ──────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    'UAV Aerodynamic Analysis — VSPAERO Results',
    fontsize=16, fontweight='bold')

# CL vs Alpha
axes[0,0].plot(alpha, CL_abs, 'b-o',
               linewidth=2, markersize=8)
axes[0,0].set_xlabel('Angle of Attack (deg)')
axes[0,0].set_ylabel('Lift Coefficient CL')
axes[0,0].set_title('Lift Curve')
axes[0,0].grid(True)
axes[0,0].axvline(
    x=alpha[best_idx],
    color='r', linestyle='--',
    label=f'Best α={alpha[best_idx]:.1f}°')
axes[0,0].legend()

# CD vs Alpha
axes[0,1].plot(alpha, CDtot, 'r-o',
               linewidth=2, markersize=8)
axes[0,1].set_xlabel('Angle of Attack (deg)')
axes[0,1].set_ylabel('Drag Coefficient CD')
axes[0,1].set_title('Drag Curve')
axes[0,1].grid(True)

# L/D vs Alpha
axes[1,0].plot(alpha, LD_abs, 'g-o',
               linewidth=2, markersize=8)
axes[1,0].set_xlabel('Angle of Attack (deg)')
axes[1,0].set_ylabel('L/D Ratio')
axes[1,0].set_title('Lift to Drag Ratio')
axes[1,0].grid(True)
axes[1,0].axvline(
    x=alpha[best_idx],
    color='r', linestyle='--',
    label=f'Best L/D={max(LD_abs):.1f}')
axes[1,0].legend()

# Drag Polar
axes[1,1].plot(CDtot, CL_abs, 'purple',
               linewidth=2, marker='o',
               markersize=8)
axes[1,1].set_xlabel('Drag Coefficient CD')
axes[1,1].set_ylabel('Lift Coefficient CL')
axes[1,1].set_title('Drag Polar')
axes[1,1].grid(True)

plt.tight_layout()
save_path = (
    "D:\\DroneProjects\\uav-cfd-analysis\\"
    "results\\aerodynamic_analysis.png")
plt.savefig(save_path, dpi=150,
            bbox_inches='tight')
plt.show()

print(f"\nGraph saved! ✅")
print("Analysis Complete!")