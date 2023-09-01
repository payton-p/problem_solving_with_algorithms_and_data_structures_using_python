# These definitions were largely taken from:
# https://runestone.academy/ns/books/published/pythonds/SortSearch/Hashing.html
# Review that link for additional details.
from chapter05_searching_and_sorting.hash_table import HashTable


# Hashing:
# A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each
# position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0. The
# mapping between an item and the slot where that item belongs in the hash table is called the hash function. The hash
# function will take any item in the collection and return an integer in the range of slot names, between 0 and m - 1.

# Load Factor:
# The number of slots occupied is referred to as the load factor, and is commonly denoted by
# lambda = number of items / table size.

# Perfect Hash Function:
# Given a collection of items, a hash function that maps each item into a unique slot is referred to as a perfect hash
# function. If we know the items and the collection will never change, then it is possible to construct a perfect hash
# function, but otherwise, there is no systematic way to construct a perfect hash function.

# Collisions - Linear Probing:
# When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table.
# This process is called collision resolution. Open addressing is a collision resolution that starts at the original
# hash value position and then moves in a sequential manner through the slots until it encounters the first slot that
# is empty. By systematically visiting each slot one at a time, we are performing an open addressing technique called
# linear probing.

# Collisions - Clusters:
# A disadvantage to linear probing is the tendency for clustering; items become clustered in the table. This means that
# if many collisions occur at the same hash value, a number of surrounding slots will be filled by the linear probing
# resolution. One way to deal with clustering is to extend the linear probing technique so that instead of looking
# sequentially for the next open slot, we skip slots, thereby more evenly distributing the items that have caused
# collisions.

# Collisions - Rehashing
# The general name for this process of looking for another slot after a collision is rehashing.

# Collisions - Use a Prime Number for the Table Size:
# It is important to note that the size of the “skip” must be such that all the slots in the table will eventually be
# visited. Otherwise, part of the table will be unused. To ensure this, it is often suggested that the table size be a
# prime number.

# Collisions - Quadratic Probing:
# A variation of the linear probing idea is called quadratic probing. Instead of using a constant “skip” value, we use
# a rehash function that increments the hash value by 1, 3, 5, 7, 9, and so on.

# Chaining:
# An alternative method for handling the collision problem is to allow each slot to hold a reference to a collection
# (or chain) of items. Chaining allows many items to exist at the same location in the hash table. When collisions
# happen, the item is still placed in the proper slot of the hash table. As more and more items hash to the same
# location, the difficulty of searching for the item in the collection increases.

def _hash(string_to_be_hashed, table_size):
    hash_sum = 0
    for position in range(len(string_to_be_hashed)):
        hash_sum = hash_sum + ord(string_to_be_hashed[position])

    return hash_sum % table_size


def main():
    hash_table = HashTable()
    hash_table.put(54, "cat")
    hash_table.put(26, "dog")
    hash_table.put(93, "lion")
    hash_table.put(17, "tiger")
    hash_table.put(77, "bird")
    hash_table.put(31, "cow")
    hash_table.put(44, "goat")
    hash_table.put(55, "pig")
    hash_table.put(20, "chicken")

    print(hash_table.slots)
    print(hash_table.data)
    print(hash_table.get(20))


if __name__ == "__main__":
    main()
