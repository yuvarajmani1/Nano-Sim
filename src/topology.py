import random, math

class Node:
    def __init__(self, nid, x, y):
        self.id = nid
        self.x = x
        self.y = y

class Topology:
    def __init__(self, node_count=350, area=(0.01,0.01), tx_range=0.0015):
        self.node_count = node_count
        self.area = area
        self.tx_range = tx_range
        self.nodes = self.deploy_nodes()

    def deploy_nodes(self):
        nodes = []
        for i in range(self.node_count):
            x = random.uniform(0, self.area[0])
            y = random.uniform(0, self.area[1])
            nodes.append(Node(i, x, y))
        return nodes

    def neighbors(self, node_id):
        ref = self.nodes[node_id]
        nbrs = []
        for n in self.nodes:
            if n.id == node_id: continue
            d = math.hypot(n.x - ref.x, n.y - ref.y)
            if d <= self.tx_range:
                nbrs.append(n.id)
        return nbrs
