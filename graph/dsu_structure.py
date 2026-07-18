# disjoint set union
# Algorithmmically , DSU douest case about the heirarchy, it only case about the leader the representative
# in a stric heirarchy ->  a->b->c, a is the boss and c is the subordinate.
# In DSu (path compression): we start with a->b->c. but when you call find(c) the algorithm  flattens and points directly to a 
# Dsu destroys the heirarchy to gain the speed
# It turns a deep, slow heirarchy into a shallow, fast, flat structure.
# Dsu destroys the heirarchy to gain spees. it turns a deep, slow heirarch  into a shallow, fast , flat sturcture.
# the Dsu uses to main concepts:
# find(x): asks who is the leader of group x? we user the path compression here - every time you look for a leader, you update the node to point directly to the leader, making future lookups almost instant.
# union(x,y): Asks, Are these two in different groups? if so then merge them under one leader. We use union by rank - always attach the smaller group to thje larger to keep the structure flat.
# to make this work efficiently we dont just return the leader; we reecognize the chain so future lookups arre faster.
# the base case: if parent[node] == node, then the node is its own leader. 
# the pathe compression : the efficiency hack. Instead if just return the leader, we set the parent[node] directly to the leade we found , this collapses the path, ensuring the next next time you ask , its an O(1) lookup

class UnionFind:
    def __init__(self, n):
        # every node starts as it's own leader. Standard initialization set uo for the 
        self.parent = {i:i for i in range(n)} 

    def find(self,i):
        # If  node is it's own parent, It's the leader.
        if self.parent[i] == i:
            return i
        
        # path compression: Point node directly to the leader.
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # merge the two groups by setting one leader as the parent of the other
            self.parent[root_i] = root_j
            return True # successfully merged
        return False #Already in the same group
    

if __name__ == "__main__":
    dsu = UnionFind(5)

    # Initially, every one is their own leader.
    assert dsu.find(0) == 0
    assert dsu.find(1) == 1

    # Union 0 and 1, then 1 and 2

    dsu.union(0,1)
    dsu.union(1,2)

    # 3 Test: Are o,1, and 2 are in the same group?
    # The Leader of 0, 1, 2 should be the same.
    leader = dsu.find(0)
    assert dsu.find(1) == leader
    assert dsu.find(2) == leader

    # Test: Is 3 in a differnet group?
    assert dsu.find(3) != leader

    print("DSU Test Suite Passed: Groups are correctly maintained")