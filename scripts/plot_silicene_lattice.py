import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/silicene/lattice_scan.csv")

x = data["lattice_constant_A"]
y = data["total_energy_eV"]

min_index = y.idxmin()
equilibrium_lattice = x[min_index]
minimum_energy = y[min_index]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker="o")
plt.scatter(equilibrium_lattice, minimum_energy, s=80)

plt.xlabel("Lattice Constant (Å)")
plt.ylabel("Total Energy (eV)")
plt.title("Silicene: Total Energy vs Lattice Constant")

plt.annotate(
    f"Minimum: a = {equilibrium_lattice:.2f} Å",
    (equilibrium_lattice, minimum_energy),
    xytext=(equilibrium_lattice + 0.10, minimum_energy + 0.30),
    arrowprops=dict(arrowstyle="->")
)

plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("figures/silicene_lattice_scan.png", dpi=300)
plt.show()

print(f"Equilibrium lattice constant: {equilibrium_lattice:.2f} Å")
print(f"Minimum total energy: {minimum_energy:.8f} eV")

