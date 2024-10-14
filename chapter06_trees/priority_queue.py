class PriorityQueue:
    """
    A priority queue is a type of queue that arranges elements based on their priority values. Elements with higher
    priority values are typically retrieved or removed before elements with lower priority values. Each element has a
    priority value associated with it. When we add an item, it is inserted in a position based on its priority value.

    A priority queue is an abstract data type similar to a regular queue or stack abstract data type. Each element in a
    priority queue has an associated priority. In a priority queue, elements with high priority are served before
    elements with low priority.

    The classic way to implement a priority queue is using a data structure called a binary heap.

    Used in Dijkstra's algorithm and Prim's Spanning Tree algorithm.
    """

    def __init__(self):
        self.heap_array = [(0, 0)]
        self.current_size = 0

    def build_heap(self, _list):
        """Build the priority queue (aka heap) from a given list."""

        self.current_size = len(_list)
        self.heap_array = [(0, 0)]

        for i in _list:
            self.heap_array.append(i)

        i = len(_list) // 2

        while i > 0:
            self.percolate_down(i)
            i = i - 1

    def percolate_down(self, i):
        """Percolate a new item as far down the tree as it needs to go to maintain the heap property."""

        while i * 2 <= self.current_size:
            min_child = self.min_child(i)

            if self.heap_array[i][0] > self.heap_array[min_child][0]:
                tmp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[min_child]
                self.heap_array[min_child] = tmp

            i = min_child

    def min_child(self, i):
        """The min child is the smallest child less than the root."""

        if i * 2 > self.current_size:
            return -1
        else:
            if i * 2 + 1 > self.current_size:
                return i * 2
            else:
                if self.heap_array[i * 2][0] < self.heap_array[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def percolate_up(self, i):
        """Percolate a new item as far up in the tree as it needs to go to maintain the heap property."""

        while i // 2 > 0:
            if self.heap_array[i][0] < self.heap_array[i // 2][0]:
                tmp = self.heap_array[i // 2]
                self.heap_array[i // 2] = self.heap_array[i]
                self.heap_array[i] = tmp

            i = i // 2

    def add(self, k):
        """Add the new item into the proper position in the priority queue/heap."""

        self.heap_array.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)

    def delete_min(self):
        """Delete the minimum value (the root) and restore the heap structure and the heap order property."""

        value = self.heap_array[1][1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_array.pop()
        self.percolate_down(1)

        return value

    def is_empty(self):
        """Check if the priority queue is empty."""

        if self.current_size == 0:
            return True
        else:
            return False

    def decrease_key(self, value, amount):
        """
        Find the priority queue/heap item to decrease by looking at its value.

        This is used in Dijkstra's algorithm when the distance to a vertex that is already in the priority queue is
        reduced, and this moves that vertex toward the front of the priority queue.
        """

        done = False
        i = 1
        key = 0

        while not done and i <= self.current_size:
            if self.heap_array[i][1] == value:
                done = True
                key = i
            else:
                i = i + 1

        if key > 0:
            self.heap_array[key] = (amount, self.heap_array[key][1])
            self.percolate_up(key)

    def __contains__(self, vertex):
        """Determine whether collection contains an item."""

        for pair in self.heap_array:
            if pair[1] == vertex:
                return True

        return False
