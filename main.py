class DisjointSet:
    def __init__(self) -> None:
        self.parent = {}
    
    def makeSet(self, n: int):
        for i in range(1, n+1):
            self.parent[i] = i
    
    def findParent(self, a: int):
        if self.parent[a] == a:
            return a
        
        parent = self.findParent(self.parent[a])
        self.parent[a] = parent
        return self.parent[a]

    def merge(self, a: int, b: int):
        self.parent[self.findParent(a)] = self.findParent(b)

    def isSameSet(self, a: int, b: int) -> bool:
        return self.findParent(a) == self.findParent(b)


        

if __name__ == "__main__":
    disjoint_set = DisjointSet()
    disjoint_set.makeSet(7)

    disjoint_set.merge(1, 2)
    disjoint_set.merge(2, 3)
    disjoint_set.merge(3, 6)
    disjoint_set.merge(6, 7)
    disjoint_set.merge(4, 5)
    disjoint_set.merge(1, 5)
    print(disjoint_set.parent)
    # disjoint_set.merge(3, 4)
    # disjoint_set.merge(4, 5)
    # print(disjoint_set.parent)