class Node:

    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.tree = Node()

    def addWord(self, word: str) -> None:
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
        def searchFrom(node, word):
            curr = node
            for i,c in enumerate(word):
                # when char is . return recurive search results
                if c == '.':
                    print('enter the .')
                    for k in curr.children:
                        print(k)
                        print(word[i:])
                        if searchFrom(curr.children[k], word[i+1:]):
                            return True
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.word
        
        return searchFrom(self.tree, word)

        
