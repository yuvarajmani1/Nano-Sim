from topology import Topology
from energy_model import EnergyModel
from algorithms.fld import flooding_round
from simulation import Simulation
from plotter import plot_alive
import os

def main():
    os.makedirs("data", exist_ok=True)
    os.makedirs("plots", exist_ok=True)

    topo = Topology(node_count=350, area=(0.01,0.01), tx_range=0.0015)
    em = EnergyModel(node_count=topo.node_count, initial_energy=800e-9)
    sim = Simulation(topo, em, algorithm_fn=flooding_round, max_time=400, out_csv="data/results.csv")
    sim.run()
    print("Simulation finished. Plotting...")
    plot_alive("data/results.csv", "plots/alive_nodes.png")
    print("Results saved: data/results.csv and plots/alive_nodes.png")

if __name__ == "__main__":
    main()
