def flooding_round(topo, energy_model, tx_energy=100e-12, rx_energy=50e-12):
    node_count = topo.node_count
    transmitters = [n.id for n in topo.nodes if energy_model.is_alive(n.id)]
    for tx in transmitters:
        energy_model.consume_tx(tx, tx_energy)
        nbrs = topo.neighbors(tx)
        for r in nbrs:
            if energy_model.is_alive(r):
                energy_model.consume_rx(r, rx_energy)

