file_path = "../cpp_practice/trie/dicts/3k.txt"
file_path = "../cpp_practice/trie/dicts/scrabble270k.txt"
file_path = "../cpp_practice/trie/dicts/58k.txt"
file_path = "../cpp_practice/trie/dicts/alpha370k.txt"

def word2key(word):
  s = sorted(word)
  key = ''
  for c in s:
    key += c
  return key 
  vec = [0]*26
  for c in word:
    i = ord(c) - ord('a')
    if i < 0 or i > 25:
      return ''
    vec[i] = ord(c)
  key = ''
  for i in vec:
    if i:
      key += chr(i)
  return key

d = {}
largest = {}
with open(file_path) as f:
  for word in f:
    word = word.strip().lower()
    key = word2key(word)
    if not key:
      continue
    if not key in d:
      d[key] = []
    d[key].append(word)
    l = len(key)
    c = len(d[key])
    if not l in largest:
      largest[l] = (c, [key])
    elif c == largest[l][0]:
      largest[l][1].append(key)
    elif c > largest[l][0]:
      largest[l] = (c, [key])

for l in largest:
  c, keys = largest[l]
  if c > 2:
    print(l, c, keys)
    for key in keys:
      print(key, d[key])
