# from enum import Enum

# class AutomatonKind(Enum):
#     EMPTY = 0
#     TRIE = 1
#     AHOCORASIC = 2

# class KeysStore(Enum):
#     STORE_INTS   = 10
#     STORE_LENGTH = 20
#     STORE_ANY    = 30

# class Automaton:
#     def __init__(self) -> None:
#         self.meow = 24254535

#     def add_words(self, key):
#         print(self.meow)


# import ahocorasic
# print(ahocorasic.TEST)
# import pickle
# a = Automaton()
# with open('test', 'wb') as f:
#     pickle.dump(a, f)

# with open('test', 'rb') as f:
#     b = pickle.load(f)

# print(b.add_words(33))