from node import Node

class Lenkeliste:
    def __init__(self):
        self._forsteNode = None

    def leggTilNode(self, node):
        if self._forsteNode is None:
            self._forsteNode = node

        elif self._forsteNode.hentNesteNode() is None:
            self._forsteNode.settNesteNode(node)

        else:
            forrige = self._forsteNode.hentNesteNode()

            while forrige is not None:
                if forrige.hentNesteNode() is None:
                    break
                else:
                    forrige = forrige.hentNesteNode()

            forrige.settNesteNode(node)

    def printLenkeliste(self):
        print(self._forsteNode.hentTall())
        forrige = self._forsteNode.hentNesteNode()

        while forrige is not None:
            print(forrige.hentTall())
            forrige = forrige.hentNesteNode()
