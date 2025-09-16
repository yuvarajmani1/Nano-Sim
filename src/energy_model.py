class EnergyModel:
    def __init__(self, node_count, initial_energy=800e-9, threshold=2e-12):
        self.initial_energy = initial_energy
        self.threshold = threshold
        self.energy = [initial_energy for _ in range(node_count)]

    def is_alive(self, nid):
        return self.energy[nid] > self.threshold

    def consume_tx(self, nid, amount):
        self.energy[nid] = max(0.0, self.energy[nid] - amount)

    def consume_rx(self, nid, amount):
        self.energy[nid] = max(0.0, self.energy[nid] - amount)
