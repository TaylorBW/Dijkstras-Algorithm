#Edge class (Taken from Data structres and Algorithms p.201)
class Edge:
    def __init__(self,head,tail,weight):
        self.head = head
        self.tail = tail
        self.weight = weight
        
    def __lt__(self,other):
        return self.weight < other.weight