from typing import Union
from enum import Enum

from trie import Trie

TEST = 30

# Automaton Kind
EMPTY = 0
TRIE = 1
AHOCORASIC = 2

#Automaton KeysStore
STORE_INTS   = 10
STORE_LENGTH = 20
STORE_ANY    = 30

#Automaton KeyType
KEY_STRING   = 100
KEY_SEQUENCE = 200


class Automaton:
    """A very simple Prototype Automaton"""

    def __init__(self, value_type, key_type) -> None:
        self.make_automaton_kind = EMPTY
        self._value_type = value_type
        self._key_type = key_type
        self.trie = Trie()
        pass
    
    @property
    def kind(self):
        return self._key_type

    @property
    def store(self):
        return 

    def add_words(self, key, value):
        node = self.trie.insert(key)
        node.value = value

    def remove_word(self):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def exist(self):
        pass

    def match(self):
        pass

    def longest_prefix(self):
        pass

    def get(self):
        pass

    def make_automaton(self):
        """
        Method to make an Ahocorasic Automaton
        """
        pass

    def findall(self):
        pass

    def iter(self):
        pass

    def iter_long(self):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass

    def get_stats(self):
        pass

    def dump(self):
        pass

    def __reduce__(self):
        pass

    def __sizeof__(self):
        pass

    def save(self):
        pass