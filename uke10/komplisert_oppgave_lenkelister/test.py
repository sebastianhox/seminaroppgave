from node import Node
from lenkeliste import Lenkeliste
import random


lenkeliste = Lenkeliste()


for i in range(10):
    node = Node(random.randint(0,10))
    lenkeliste.leggTilNode(node)

lenkeliste.printLenkeliste()
