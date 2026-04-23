\# ✈️ UAV Aerodynamic Design \& CFD Analysis



\## 📌 Project Overview

Complete aerodynamic design and analysis of a Fixed Wing UAV

using OpenVSP for geometry creation and VSPAERO for

aerodynamic simulation. This project demonstrates the full

aerospace engineering workflow from design to analysis.



\## 🎯 UAV Specifications

| Parameter | Value |

|---|---|

| Wing Span | 3.0 m |

| Root Chord | 0.4 m |

| Tip Chord | 0.2 m |

| Wing Area | 1.2 m² |

| Fuselage Length | 2.5 m |

| Airfoil | NACA 2412 |

| Cruise Speed | 20 m/s |

| UAV Mass | 2.5 kg |



\## 📊 Aerodynamic Results

| Parameter | Value |

|---|---|

| Max Lift Coefficient CL | 0.6621 |

| Min Drag Coefficient CD | 0.0144 |

| Best L/D Ratio | 8.76 |

| Best Angle of Attack | 4.0 degrees |

| Stall Speed | 7.10 m/s |

| Cruise Lift | 65.54 N |

| Cruise Drag | 7.48 N |



\## 🛠️ Tools Used

| Tool | Purpose |

|---|---|

| OpenVSP 3.48.2 | UAV geometry design |

| VSPAERO | Aerodynamic analysis |

| Python | Results processing |

| Matplotlib | Data visualization |



\## 🗂️ Project Structure

uav-cfd-analysis/

├── geometry/

│   └── UAV\_design.vsp3

├── results/

│   ├── aerodynamic\_analysis.png

│   ├── cl\_curve.png

│   ├── cd\_curve.png

│   ├── ld\_ratio.png

│   ├── load\_distribution.png

│   ├── convergence.png

│   ├── cp\_slice.png

│   ├── sweep\_results.png

│   └── vspaero\_results.csv

├── analyze\_results.py

└── README.md



\## 📈 Results



\### Aerodynamic Analysis

!\[Analysis](results/aerodynamic\_analysis.png)



\### Lift Coefficient Curve

!\[CL Curve](results/cl\_curve.png)



\### Load Distribution

!\[Load Distribution](results/load\_distribution.png)



\### Drag Polar

!\[CD Curve](results/cd\_curve.png)



\## ⚙️ How to Reproduce

1\. Install OpenVSP 3.48.2

2\. Open geometry/UAV\_design.vsp3

3\. Run VSPAERO analysis

4\. Run analyze\_results.py



\## 👨‍💻 Author

Yogesh E S

Aeronautical Engineer | Drone AI Developer

yogeshes376@gmail.com

