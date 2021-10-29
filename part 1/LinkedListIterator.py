#############################################
#	COMPSCI 105 S2 C, 2018              #
#	Assignment 2 Question 1             #
#                                           #
#	@author     Xiaolin Li and xli556   #
#	@version    08/10/2018              #
#############################################
from NodeDLL import NodeDLL

class LinkedListIterator:
    def __init__(self, head):
        self.__current = head
        

    def __next__(self):
        value = self.__current.get_next().get_data()
        #check if the value is the dummy head node
        #base-case: there only one node which is the dummy head node        
        if value == None:
            raise StopIteration
        else:
            self.__current = self.__current.get_next()
            return value
