
class Node:
    def __init__(self, tall):
        self._tall = tall
        self._nesteNode = None

    def settNesteNode(self, node):
        self._nesteNode = node

    def hentNesteNode(self):
        return self._nesteNode

    def hentTall(self):
        return self._tall 
