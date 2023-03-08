import ahocorasic

automaton = ahocorasic.Automaton()

for idx, key in enumerate('he her hers she'.split()):
   automaton.add_word(key, (idx, key))

assert automaton.get('he') == (0, "he")
assert automaton.get('she') == (3, "she")
assert automaton.get('cat', 'not exists') == "not exists"
