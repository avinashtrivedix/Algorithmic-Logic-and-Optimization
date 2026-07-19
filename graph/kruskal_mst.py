# Minimum Spanning Tree 
# You have  set of citites and the cost to build a road between any of two of them. you want to connect all cities with the minimum total cost.
# The Logic: this is where we combine sorting and DSU.
# Sort all the edges by cost (cheapest first)
# Iterate through edges: IF connecting two cities doesnt create a cycle connect them.
# Use DSU to detect cycles instantly
# the toolbox : Kruskals Algorithm.
# sort and Iterate: sort:  edges.sort(key = lambda x: x[2]) (sort by weight)
# Iterate: for each edge: (u,v,weight): 

# the union find class
class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False
    
# the Kruskal's Logic    
def kruskal_mst(n, edges):
    # sort edges by weight (the 3rd in [u,v,weight]) , In cp and technical interview, the edge is almost universally represented as triple or tuple.
    edges.sort(key = lambda x: x[2])
    dsu = UnionFind(n)
    mst_cost = 0
    edges_count = 0
    for u, v, weight in edges:
        # uSe the the tools union method to connect them and check cycles
        if dsu.union(u, v):
            mst_cost += weight
            edges_count += 1

    return mst_cost if edges_count == n-1 else -1


if __name__ == "__main__":
    n = 3
    edges = [[0, 1, 1], [1, 2, 2], [0, 2, 10]]
    cost = kruskal_mst(n, edges)
    print(f"otoal mst cost: {cost}")
    assert cost == 3
    print("Success: Greedy strategy verified.")