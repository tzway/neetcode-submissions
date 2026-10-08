class Node:

    def __init__(self):
        self.word = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.tree = Node()

    def insert(self, word: str) -> None:
        curr = self.tree
        for c in word:
            if c in curr.children:
                pass
            else:
                curr.children[c] = Node()
            
            curr = curr.children[c]
        # in the end, set word = True
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.tree
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        