
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Step 1: graph terminology
# Nodes: words
# Edges: 1-letter differences


# Step 2: build the graph
import string
## Read in the words
f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

## get_neighbor
## add vertices?

def get_neighbors(word):
    neighbors = []
    # for every letter in the word:
    for i in range(len(word)):
    ## for every letter in the alphabet:
        for alphaletter in string.ascii_lowercase:
    ### swap out the word-letter with the alphabet-letter
            # turn into a list
            word_list = list(word)
            word_list[i] = alphaletter

            ## turn the word list back into a string
            maybe_neighbor = "".join(word_list)

            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)

    return neighbors

    ### if the new word is in our word dictionary, then it's a neighbor

## Step 3: choose your algorithm
### BFS: "shortest tranformation sequence"

def find_ladders(start_word, end_word):
    q = Queue()
    visited = set()
    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]

        if current_node == end_word:
            return current_path

        if current_node not in visited:
            neighbors = get_neighbors(current_node)

            for neighbor in neighbors:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(find_ladders("hit", "cog"))