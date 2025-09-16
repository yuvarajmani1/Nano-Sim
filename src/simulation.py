import csv
from tqdm import trange

class Simulation:
    def __init__(self, topo, energy_model, algorithm_fn, max_time=200, out_csv="data/results.csv"):
        self.topo = topo
        self.energy = energy_model
        self.algorithm = algorithm_fn
        self.max_time = max_time
        self.out_csv = out_csv

    def run(self):
        with open(self.out_csv, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["time","alive_nodes","avg_energy"])
        for t in trange(self.max_time, desc="Sim time"):
            self.algorithm(self.topo, self.energy)
            alive = sum(1 for i in range(self.topo.node_count) if self.energy.is_alive(i))
            avg_e = sum(self.energy.energy)/len(self.energy.energy)
            with open(self.out_csv, "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([t, alive, avg_e])
            if alive == 0:
                break
