class HashTable:
    """
    A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each
    position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0.
    The mapping between an item and the slot where that item belongs in the hash table is called the hash function. The
    hash function will take any item in the collection and return an integer in the range of slot names, between 0 and
    m - 1.
    """

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @staticmethod
    def hash_function(key, size):
        """Implement a simple remainder method."""

        return key % size

    @staticmethod
    def rehash(old_hash, size):
        """Find a new hash value using the previous hash."""

        return (old_hash + 1) % size

    def get(self, key):
        """Given a key, return the value stored in the map or None otherwise."""

        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def put(self, key, data):
        """
        Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new
        value.
        """

        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace
