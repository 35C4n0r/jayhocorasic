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
        self.insert_curr = self.root
        self.search_curr = self.root


    def insert(self, key: str) -> Node:
        # print(self.root.children)
        self.insert_curr = self.root
        """Key must be strictly an string"""
        key_size = len(key)


        for letter in list(key):

            # print("current root => ", self.insert_curr, "global root => ", self.root)

            present = self.insert_curr.children.get(letter, None)
            # print(present, letter, key)
             #If the letter already exists as a child
            if present is not None:
                self.insert_curr = present
                # print(self.insert_curr, self.insert_curr.letter, self.insert_curr.children)

            #Otherwise
            else:
                new_node = Node(letter=letter)
                self.insert_curr.children[letter] = new_node
                self.insert_curr = new_node
                # print("inserted ", self.insert_curr, new_node)
        # print()
        return self.insert_curr


    def search(self, pattern: str, default=None, restart: bool=True):
        # print(self.root.children)
        if restart:
            self.search_curr = self.root

        pattern_size = len(pattern)
        for letter in list(pattern):
            # print(self.search_curr.letter)
            present = self.search_curr.children.get(letter, None)
            # print(letter, present)
            if present is not None:
                self.search_curr = present
                # print(self.search_curr.letter)

            else:
                if default is None:
                    raise KeyError
                else:
                    return (default, 0)
        return (self.search_curr, 1)

    def delete(self):
        pass