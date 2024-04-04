"""
If you have never heard of Trie, then here is an article and a bunch of references to help you.
Let's jump into the topic.

What is Trie?

Trie is a tree-like data structure wherein all the nodes stores alphabetical values (most commonly). Trie is an
ordered tree data structure in which every traversal down the branch retrieves you a string or word. Here is a formal
definition from Wikipedia, A trie also called a digital tree or prefix tree, is a kind of search tree—an ordered tree
data structure used to store a dynamic set or associative array where the keys are usually strings. Fun Fact: Trie
name comes from name retrieval.

Representation:

Template 1 ( Representation )

class TrieNode{
public:
    bool end;
    TrieNode* children[27];
    TrieNode(){
        end = false;
        memset(children, NULL, sizeof(children));
    }
};

It contains an empty root node and references to all other nodes.

The number of references depends on the total number of values possible.
Example: If the trie represents strings that contain only lowercase letters. Then the number of references needs to be 26 since there are 26 different alphabets from 'a' to 'z'.
If trie represents bits it has only two references. (0 and 1)

To be more clear, What does a node contains?
It contains two parts.

The array of references to other nodes.
Boolean value - leaf (To check whether the string ends at that node or not)
Note here leaf is not to check whether it is leaf node or not.
Let's take an example and build a trie.

List = { "apple", "app", "abide", "ball", "bat" }
Note: All the string in the list contains lowercase letters from 'a' to 'z'.



Image 1



Status: apple is added to the trie.

Here the first node at the top is root and it is empty. 
Notes: 
Now root has a ref. to node 'a' and node 'a' has reference to 'p' and so on. All other  reference are still NULL.




Image 2




Status: app added to trie which already contains apple.
From the root, we have to check whether the reference node exists or not.
If exists, we have to move to the node or create a new node.

Fun Fact: All the descendants of a node have a common prefix of the string associated with that node
Correction in the image: 'e' node in apple also have leaf value true.




image 3




Status: abide is added. It shares prefix 'a' with apple and app.





Image 4





Status: ball is added.
Since 'b' reference is not present in root. we create it.




Image 5




Status: bat added.
Final image of the trie after inserting strings in the list.
We have to  traverse the trie to search a string.
I hope it made some sense.
It really takes a day to produce the images. A upvote would be encouraging. Thanks.

Template for build trie and search a string in a trie:

	TrieNode* root = new TrieNode();        /* Root Creation */
	
    void insert(string word) {              /* Insert word into the trie */
        TrieNode* node = root;
        for(char c : word){
            if(!node -> children[c - 'a']){
                node -> children[c - 'a'] = new TrieNode();
            }
            node = node -> children[c - 'a'];
        }
        node -> end = true;
    }
    
    
    bool search(string word) {             /* Search word into the trie */
        TrieNode* node = root;
        for(char c : word){
            if(!node -> children[c - 'a']){
                return false;
            }
            node = node -> children[c - 'a'];
        }
        return node -> end;
    }
    
If you still have a hard time understanding it. I attached some articles and youtube videos to help you.

"""


# https://www.youtube.com/watch?v=dOXfffhl4uI&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ&index=189&ab_channel=ApnaCollege

# https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python/11015381#11015381


class TrieNode:
    def __init__(self):
        # Dict: Key = letter, Item = TrieNode
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def build_trie(self, words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.end

    def _walk_trie(self, node, word, word_list):

        if node.children:
            for char in node.children:
                word_new = word + char
                if node.children[char].end:
                    # if node.end:
                    word_list.append(word_new)
                    # word_list.append( word)
                self._walk_trie(node.children[char], word_new, word_list)

    def auto_complete(self, partial_word):
        node = self.root

        word_list = []
        # find the node for last char of word
        for char in partial_word:
            if char in node.children:
                node = node.children[char]
            else:
                # partial_word not found return
                return word_list

        if node.end:
            word_list.append(partial_word)

        #  word_list will be created in this method for suggestions that start with partial_word
        self._walk_trie(node, partial_word, word_list)
        return word_list