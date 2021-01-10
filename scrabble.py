import trie
from itertools import permutations

# file_path = "../cpp_practice/trie/dicts/3k.txt"
file_path = "../cpp_practice/trie/dicts/scrabble270k.txt"
# file_path = "../cpp_practice/trie/dicts/58k.txt"
# file_path = "../cpp_practice/trie/dicts/alpha370k.txt"

'''
1 Point - A, E, I, L, N, O, R, S, T and U.
2 Points - D and G.
3 Points - B, C, M and P.
4 Points - F, H, V, W and Y.
5 Points - K.
8 Points - J and X.
10 Points - Q and Z.
'''

score_key = {
  'a': 1,
  'b': 4,
  'c': 4,
  'd': 2,
  'e': 1,
  'f': 4,
  'g': 3,
  'h': 4,
  'i': 1,
  'j': 10,
  'k': 5,
  'l': 1,
  'm': 3,
  'n': 1,
  'o': 1,
  'p': 4,
  'q': 10,
  'r': 1,
  's': 1,
  't': 1,
  'u': 2,
  'v': 4,
  'w': 4,
  'x': 4,
  'y': 4,
  'z': 10,
  '?': 0,
}

def score(word, n_bonus):
  score = 0
  for char in word:
    score += score_key[char]
  if len(word) >= n_bonus:
    score += 40
  return score


t = trie.Trie(file_path)
while True:
  x = raw_input("Enter tiles: ")
  if not x:
    break
  num_tiles = len(x)
  if num_tiles > 8:
    print('max tiles is 8')
    continue
  count = 0
  words = []
  
  for i in range(1, num_tiles+1):
    perms = set([''.join(p) for p in permutations(x, i)])
    count += len(perms)
    for perm in perms:
      if t.IsWord(perm):
        words.append((score(perm, num_tiles), perm))

  words = sorted(words, key=lambda element: (element[0], element[1]))
  for word in words:
    print(word[0], word[1])
  print("unique permutations found: ", count)
  print("words found: ", len(words))
