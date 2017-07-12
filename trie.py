

#insert and re_insert are from https://discuss.leetcode.com/topic/16629/accepted-python-implementation-for-trie

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.val = None
        self.pointers={}
        

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        self.rec_insert(word, self.root)
        return
            
    def rec_insert(self, word, node):
        if word[:1] not in node.pointers:
            newNode=TrieNode()
            newNode.val=word[:1]
            node.pointers[word[:1]]=newNode
            self.rec_insert(word, node)
        else:
            nextNode = node.pointers[word[:1]]
            if len(word[1:])==0:
                nextNode.pointers[' '] ='__END__'
                return
            return self.rec_insert(word[1:], nextNode)

    def remove(self, word):

        current_node = self.root
        removal_level = self.root.pointers
        key_to_remove = word[0]

        for letter in word:
            if letter in current_node.pointers:
                if len(current_node.pointers) > 1:
                    removal_level = current_node.pointers
                    key_to_remove = letter
                current_node = current_node.pointers[letter]
            else:
                return None

        del removal_level[key_to_remove]


            
test = Trie()
test.insert("dog")
test.insert("door")