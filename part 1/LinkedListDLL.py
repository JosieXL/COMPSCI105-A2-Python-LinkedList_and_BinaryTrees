#############################################
#	COMPSCI 105 S2 C, 2018              #
#	Assignment 2 Question 1             #
#                                           #
#	@author     Xiaolin Li and xli556   #
#	@version    08/10/2018              #
#############################################
# This is a doubly linked list implementation with tail reference
from NodeDLL import NodeDLL
from LinkedListIterator import LinkedListIterator

class LinkedListDLL:

    def __init__(self):
        self.__head = NodeDLL(None)
        self.__head.set_next(self.__head)
        self.__head.set_prev(self.__head)
        self.__count = 0

    def size(self):
        return self.__count;

    def is_empty(self):
        return self.__count == 0

    def add_before(self, item, curr):
        new_node = NodeDLL(item)
        new_node.set_next(curr)
        new_node.set_prev(curr.get_prev())
        curr.set_prev(new_node)
        new_node.get_prev().set_next(new_node)
        self.__count += 1

    def add_to_head(self, item):
        self.add_before(item, self.__head.get_next())

    def add_to_tail(self, item):
        self.add_before(item, self.__head)

    def remove_from_head(self):
        self.remove(self.__head.get_next())

    def remove_from_tail(self):
        self.remove(self.__head.get_prev())

    def remove(self, curr):
        curr.get_prev().set_next(curr.get_next())
        curr.get_next().set_prev(curr.get_prev())
        self.__count -= 1

    def __iter__(self):
        return LinkedListIterator(self.__head)
