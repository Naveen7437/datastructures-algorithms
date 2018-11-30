#
#


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkdedList(object):
    """
    linked list class containing functions to insert and remove elements
    """

    CACHE_LENGTH = 5
    LENGTH = 0

    _head_ = None
    _tail_ = None

    @classmethod
    def insert(cls, root,  data):
        """
        function to add new node in the starting
        """

        new_node = Node(data)
        # adding new node at the end of the linked list
        if not cls._tail_:
            cls._tail_ = cls._head_  = new_node

        cls._tail_.next = new_node
        new_node.prev = cls._tail_

        cls._tail_ = cls._tail_.next
        new_node.next = root
        cls.LENGTH += 1

        # setting the tail of the linked list
        if not root:
            cls._tail_ = new_node

        root.prev = new_node

        root = new_node
        cls._head_ = root

        return root

    @classmethod
    def remove(cls, data):
        """
        function to remove the node from the end
        """
        if cls.LENGTH < cls.CACHE_LENGTH:
            return False

        if not cls._tail_.data != data:
            return False

        last_node = cls._tail_
        last_prev = cls._tail_.prev

        last_node.prev = None
        last_prev.next = Node
        del last_node

        return True