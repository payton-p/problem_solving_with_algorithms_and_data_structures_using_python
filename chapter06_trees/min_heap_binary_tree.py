# One important variation of a queue is called a priority queue. A priority queue acts like a queue in that you dequeue
# an item by removing it from the front. However, in a priority queue the logical order of items inside a queue is
# determined by their priority. The highest priority items are at the front of the queue and the lowest priority items
# are at the back.

# The classic way to implement a priority queue is using a data structure called a binary heap. A binary heap will
# allow us both enqueue and dequeue items in O(log(n)). The binary heap is interesting to study because when we diagram
# the heap it looks a lot like a tree, but when we implement it we use only a single list as an internal representation.

# Because the tree is complete, the left child of a parent (at position p) is the node that is found in position 2p
# in the list. Similarly, the right child of the parent is at position 2p + 1 in the list. To find the parent of any
# node in the tree, we can simply use Python’s integer division. Given that a node is at position n in the list, the
# parent is at position n/2.

class MinHeapBinaryTree:
    """
    A binary heap is a complete binary tree which satisfies the heap ordering property. For a min-heap, the value of
    each node is greater than or equal to the value of its parent, with the minimum-value element at the root.
    """

    def __init__(self):
        # You will notice that an empty binary heap has a single zero as the first element of heap_list and that this
        # zero is not used, but is there so that simple integer division can be used in later methods.
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, i):
        """Percolate a new item as far up in the tree as it needs to go to maintain the heap property."""

        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp

            i = i // 2

    def insert(self, k):
        """Insert the new item into the proper position in the min-heap."""

        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)

    def percolate_down(self, i):
        """Percolate a new item as far down the tree as it needs to go to maintain the heap property."""

        while (i * 2) <= self.current_size:
            min_child_node_index = self.min_child(i)

            if self.heap_list[i] > self.heap_list[min_child_node_index]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_node_index]
                self.heap_list[min_child_node_index] = tmp

            i = min_child_node_index

    def min_child(self, i):
        """The min child is the smallest child less than the root."""

        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        """Delete the minimum value (the root) and restore the heap structure and the heap order property."""

        previous_min_value = self.heap_list[1]

        # Take the last item in the list and moving it to the root position. Moving the last item maintains our heap
        # structure property. However, we have probably destroyed the heap order property of our binary heap, which is
        # why we also have to use percolate_down.
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()

        # Update the size.
        self.current_size = self.current_size - 1

        # Restore the heap order property by pushing the new root node down the tree to its proper position.
        self.percolate_down(1)

        return previous_min_value

    def build_min_heap(self, _list):
        """Build the min heap from a given list."""

        i = len(_list) // 2

        self.current_size = len(_list)
        self.heap_list = [0] + _list[:]

        while i > 0:
            self.percolate_down(i)
            i = i - 1
