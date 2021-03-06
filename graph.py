import numpy as np

class Graph:
    """
    Used as an UI for more human-friendly graph-creation.
    """

    def __init__(self):
        self.data = []
        self.nameTable = {}


    def addNode(self, name):
        """
        Add a node to the graph.
        :param name: The name of the node
        """
        size = len(self.data)
        self.nameTable[name] = size
        self.data.append([0] * size)
        for i in range(size + 1):
            self.data[i].append(0)


    def join(self, a, b, w):
        """
        Join two nodes.
        :param a: The first node
        :param b: The second node
        :param w: The weight of the edge
        """
        i1 = self.nameTable[a]
        i2 = self.nameTable[b]

        self.data[i1][i2] = w
        self.data[i2][i1] = w

    def __str__(self):
        return "\n".join([" ".join([str(c) for c in row]) for row in self.data])


def main():
    g = Graph()

    g.addNode("x")
    g.addNode("y")

    g.join("x", "y", 10)

    g.addNode("z")
    g.addNode("k")

    print(g)

if __name__ == "__main__":
    main()
