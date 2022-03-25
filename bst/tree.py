import random
from node import Node

class Tree:
    def __init__(self, root_node: Node):
        self.root = root_node

    def display(self):
        return self.root.display()

    def insert(self, z: Node):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def maximum(self):
        def maximum_rec(x: Node):
            while x.right is not None:
                x = x.right
            return x

        return maximum_rec(self.root)

    def minimum(self):
        def minimum_rec(x: Node):
            while x.left is not None:
                x = x.left
            return x

        return minimum_rec(self.root)

    def successor(self):
        def successor_rec(x: Node):
            if x.right is not None:
                return self.minimum(x.right)
            y = x.p
            while y is not None and x == y.right:
                x = y
                y = y.p
            return y

        return successor_rec(self.root)

    def transplant(self, x: Node, y: Node):
        """transplants Node x -> Node y"""
        if y.p is None:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        if x is not None:
            x.p = y.p

    def delete(self,z: Node):
        if z.left is None:
            self.transplant(z.right, z)
        elif z.right is None:
            self.transplant(z.left, z)
        else:
            y = self.minimum(z.right)
            if y.p is not None:
                self.transplant(y.right, y)
                y.right = z.right
                y.right.p = y
            self.transplant(y, z)
            y.left = z.left
            y.left.p = y


def main():

    # create a Node
    node1 = Node(key=20)

    # create a BST, setting root to be the Node we just made
    my_tree = Tree(node1)

    # generate and insert 15 random new Nodes into the BST
    # add 2 specific nodes to test deleting after
    NUM_NODES = 15
    for i in range(NUM_NODES):
        j = random.randint(1,50)   
        my_tree.insert(Node(j))

    # print BST
    my_tree.display()
    
    # print maximum and minimum key in BST
    print("maximum key value: " + str(my_tree.maximum()))
    print("minimum key value: " + str(my_tree.minimum()))

    # insert 2 nodes.
    node_1 = Node(17)
    node_2 = Node(3)
    print("inserting 2 nodes:" + str(node_1) + ", " + str(node_2))
    my_tree.insert(node_1)
    my_tree.insert(node_2)
    my_tree.display()

    # delete 2 nodes.
    print("deleting node: " + str(node_1))
    my_tree.delete(node_1)
    my_tree.display()
    print("deleting node: " + str(node_2))
    my_tree.delete(node_2)
    my_tree.display()



if __name__ == "__main__":
    main()