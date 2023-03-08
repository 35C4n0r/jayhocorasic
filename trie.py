class Node:
    def __init__(self, letter, value=None):
        self.letter = letter
        self.value = value

        # {letter: Node()}
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = Node(None, None)
        self.current_node: Node = self.root
        self.root = Node('')
        self.curr = self.root

    def insert(self, key: str) -> Node:
        self.curr = self.root
        """Key must be strictly an string"""
        key_size = len(key)
        for letter in list(key):
             present = self.root.children.get(letter)

             #If the letter already exists as a child
             if present:
                  self.curr = present
            
            #Otherwise
             else:
                  new_node = Node(letter=letter)
                  self.curr.children[letter] = new_node
                  self.curr = new_node
        return self.curr


    def search(self, pattern):
            pass

    def delete(self):
        pass