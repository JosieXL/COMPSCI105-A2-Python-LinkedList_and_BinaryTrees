class NodeDLL:

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def get_data(self):
        return self.__data

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = newdata

    def set_next(self, new_next):
        self.__next = new_next

    def set_prev(self, new_prev):
        self.__prev = new_prev
