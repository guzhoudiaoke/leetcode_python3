import collections

#class Trie:
#
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.children = collections.defaultdict(Trie)
#        self.end = False
#        
#
#    def insert(self, word):
#        """
#        Inserts a word into the trie.
#        :type word: str
#        :rtype: void
#        """
#        node = self
#        for c in word:
#            node = node.children[c]
#        node.end = True
#        
#
#    def search(self, word):
#        """
#        Returns if the word is in the trie.
#        :type word: str
#        :rtype: bool
#        """
#        node = self
#        for c in word:
#            if c not in node.children:
#                return False
#            node = node.children[c]
#
#        return node.end
#        
#
#    def startsWith(self, prefix):
#        """
#        Returns if there is any word in the trie that starts with the given prefix.
#        :type prefix: str
#        :rtype: bool
#        """
#        node = self
#        for c in prefix:
#            if c not in node.children:
#                return False
#            node = node.children[c]
#
#        return True
#        



#class Trie:
#
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.children = {}
#        self.end = False
#        
#
#    def insert(self, word):
#        """
#        Inserts a word into the trie.
#        :type word: str
#        :rtype: void
#        """
#        node = self
#        for c in word:
#            if c not in node.children:
#                node.children[c] = Trie()
#            node = node.children[c]
#        node.end = True
#        
#
#    def search(self, word):
#        """
#        Returns if the word is in the trie.
#        :type word: str
#        :rtype: bool
#        """
#        node = self
#        for c in word:
#            if c not in node.children:
#                return False
#            node = node.children[c]
#
#        return node.end
#        
#
#    def startsWith(self, prefix):
#        """
#        Returns if there is any word in the trie that starts with the given prefix.
#        :type prefix: str
#        :rtype: bool
#        """
#        node = self
#        for c in prefix:
#            if c not in node.children:
#                return False
#            node = node.children[c]
#
#        return True
#


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['end'] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]

        return 'end' in node
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

root = Trie()

print(root.search('abcd'))      # False
root.insert('abcd')             #
print(root.search('abcd'))      # True
print(root.search('abc'))       # False
print(root.startsWith('abc'))   # True
print(root.startsWith('abcd'))  # True
print(root.startsWith('a'))     # True
print(root.startsWith('b'))     # False
root.insert('abc')              # 
print(root.search('abc'))       # True
