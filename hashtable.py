from linkedlist import LinkedList

# # Note to reviewers - making heavy use of the following code snippet:
# index = self._bucket_index(key)
# bucket = self.buckets[index]
# entry = bucket.find(lambda key_value: key_value[0])


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n^2) in all conditions, will always need to iterate
        through each item of each array."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n^2) in all conditions, will always need to iterate
        through each item of each array."""
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            # Collect all values in each bucket
            for key, value in bucket.items():
                all_valyes.append(key)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) in all conditions"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) in all conditions"""
        size = 0
        # Loop through all buckets
        for bucket in self.buckets:
            size += bucket.size
        # Count number of key-value entries in each bucket
        return size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) in best case - if item is at beginning of bucket
        O(n) in worst case - if item is at the end or does not exist in bucket"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # Check if key-value entry exists in bucket
        if entry is None:
            return False
        else:
            return True
        # OR shorter version
        # return (entry is not None)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) in best case (item is first item in bucket),
        O(n) in worst case (item is not in buck)"""
        index = self._bucket_index(key)
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # If found, return value associated with given key
        if entry is not None:
            return entry[1]  # Take value out of key-value pair
        # : Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

    # Modelled from github: ryansmith4
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) in best case (item is first item in bucket),
        O(n) in worst case (item is not in bucket)"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)

        # Check if key-value entry exists in bucket
        if entry is not None:
            # Vital note: this is a method from out Linked List class!
            bucket.delete(entry)
        # If found, update value associated with given key
        entry = (key, value)
        # Otherwise, insert given key-value entry into bucket

        bucket.append(entry)

    # Modelled from github: ryansmith4
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  \Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)

        #  Check if key-value entry exists in bucket
        if entry is not None:
            # If found, delete entry associated with given key
            bucket.delete(entry)
        # Otherwise, raise error to tell user delete failed
        else:
            # Hint: raise KeyError('Key not found: {}'.format(key))
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
