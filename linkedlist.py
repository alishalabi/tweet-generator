#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        # linked_list_length = 0
        # Think about if the LL() is_empty() == True
        if self.is_empty():
            return 0

        # Think about if the LL() only has a head & tail
        # and head and tail are the same node
        if self.head.data == self.tail.data:
            return 1

        # Think about it has a head and a tail
        # and stuff inbetween
        else:
            linked_list_length = 1
            current_node = self.head

            while current_node != self.tail:
                linked_list_length += 1
                current_node = current_node.next
            return linked_list_length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        # If linked list is empty:
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            # self.prepend(new_node.data)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # # TODO: Loop through all nodes to find item where quality(item) is True
        # while node is not None:
        #     # TODO: Check if node's data satisfies given quality function
        #     if quality(node.data) == True:
        #         return node.data
        word_found = False
        current_node = self.head
        while word_found == False:
            if quality(current_node) != current_node.data:
                current_node = current_node.next
            else:
                word_found = True
                return current_node
            return word_found

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # # TODO: Loop through all nodes to find one whose data matches given item
        # for node in self:
        #     # TODO: Update previous node to skip around node with matching data
        #     break
        #     # TODO: Otherwise raise error to tell user that delete has failed
        #     # Hint: raise ValueError('Item not found: {}'.format(item))
        # Case: Item to remove is head
        if self.head == item:
            self.head = self.head.next
            return self

        # Case: Item to remove is not head or tail
        previous_node = self.head
        if previous_node.next == item:
            previous_node.next = previous_node.next.next
            return self
        else:
            previous_node = previous_node.next

        # Case: Item to remove is tail
        if self.tail == item:
            penultimate_node = self.head
            if penultimate_node.next.next == None:
                penultimate_node.next = None
                return self
            else:
                penultimate_node = penultimate_node.next

        # Case: None of the above
        else:
            return ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
