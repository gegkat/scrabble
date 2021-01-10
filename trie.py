import sys
sys.path.append("./pygtrie")
import pygtrie

def CleanWord(word):
  return word.strip().lower()

class Trie:
  def __init__(self, file_path):
    self.trie = pygtrie.CharTrie()

    print('Building trie...')
    num_words = 0
    with open(file_path) as f:
      for word in f:
        self.trie[CleanWord(word)] = True
        num_words += 1
    print('Trie built. Words found:', num_words)

  def IsWord(self, word):
    return self.trie.has_key(word)

  def IsPrefix(self, prefix):
    return self.trie.has_subtrie(prefix)

if __name__ == "__main__":
  file_path = "../cpp_practice/trie/dicts/3k.txt"
  # file_path = "../cpp_practice/trie/dicts/scrabble270k.txt"
  # file_path = "../cpp_practice/trie/dicts/58k.txt"
  # file_path = "../cpp_practice/trie/dicts/alpha370k.txt"

  t = Trie(file_path)
  while True:
    x = raw_input("Enter a word: ")
    if not x:
      break
    print("Word? ", t.IsWord(x), " Prefix? ", t.IsPrefix(x))
