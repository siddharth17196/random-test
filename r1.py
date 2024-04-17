class DisjointSet():
    
    def __init__(self, n):    
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def UnionRank(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)

        if ulp_u == ulp_v:
            return

        rank_u = self.rank[ulp_u]
        rank_v = self.rank[ulp_v]

        if rank_u < rank_v:
            self.parent[ulp_u] = ulp_v
        elif rank_v < rank_u:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=1

size = 7
ds = DisjointSet(size)
ds.UnionRank(1, 2)
ds.UnionRank(2, 3)
ds.UnionRank(4, 5)
ds.UnionRank(6, 7)
ds.UnionRank(5, 6)
ds.UnionRank(3, 7)

print(ds.find(3), ds.find(7))