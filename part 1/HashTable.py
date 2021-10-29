#############################################
#	COMPSCI 105 S2 C, 2018              #
#	Assignment 2 Question 3             #
#                                           #
#	@author     Xiaolin Li and xli556   #
#	@version    09/10/2018              #
#############################################

class HashTable:
    def __init__(self):
        self.__size = 7 #I change 5 to 7 to fit for the test case
        self.__slots = [None] * self.__size
        self.__data = [None] * self.__size
        self.__deleted = "\0"
        self.__count = 0

    def hash_function(self, key, size):
        return key % size

    def secondary_hashfunction(self, key, size):
        return size - (key % (size - 1) + 1)
    
    def rehash(self, old_hash,step, size):
        return (old_hash + step) % size

    def get(self, key):
        start_slot = self.hash_function(key,len(self.__slots))
        position = start_slot

        while self.__slots[position] != None:
            if self.__slots[position] == key:
                return self.__data[position]
            else:
                position = self.rehash(position, len(self.__slots))
                if position == start_slot:
                    return None
        return None

    def put(self,key,data):
        if self.load() < 0.75:
            hash_value = self.hash_function(key, self.__size)
            if self.__slots[hash_value] == None or \
               self.__slots[hash_value] == self.__deleted:
                self.__slots[hash_value] = key
                self.__data[hash_value] = data
                self.__count += 1
            elif self.__slots[hash_value] == key:
                self.__data[hash_value] = data
                self.__count += 1
            else:
                secondary_value = self.secondary_hashfunction(key, self.__size)
                next_slot = self.rehash(hash_value, secondary_value, self.__size)
                while self.__slots[next_slot] != None\
                      and self.__slots[next_slot] != self.__deleted \
                      and self.__slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, secondary_value, self.__size)
                    if next_slot == hash_value and self.__count == self.__size:
                        return
                if self.__slots[next_slot] == None or \
                   self.__slots[next_slot] == self.__deleted:
                    self.__slots[next_slot] = key
                    self.__data[next_slot] = data
                    self.__count += 1
                else:
                    self.__data[next_slot] = data
                    self.__count += 1
        else:
            #first implement the slots and data from original hash table to two empty lists(slot_list1 and data_list1)
            slot_list1 = []
            data_list1 = []
            for i in range(len(self.__slots)):
                key1 = self.__slots[i]
                data1 = self.__data[i]
                if key1 != None:
                    slot_list1 += [key1]
                    data_list1 += [data1]
            new_size = self.resize(self.__size)
            new_count = 0
            self.__size = new_size
            self.__slots = [None]*new_size
            self.__data = [None]*new_size
            self.__count = new_count
            #Then, first put those original data and slots from the lists to the resized hash table
            for j in range(len(slot_list1)):
                self.put(slot_list1[j],data_list1[j])
            #Then, put the new key and data into the resized hash table
            self.put(key,data)
            

    def delete(self, key):
        start_slot = self.hash_function(key, len(self.__slots))
        position = start_slot
        key_in_slot = self.__slots[position]

        while key_in_slot != None:
            if key_in_slot == key:
                self.__slots[position] = self.__deleted
                self.__data[position] = self.__deleted
                self.__count -= 1
                return None	
            else:
                position = self.rehash(position, len(self.__slots))
                key_in_slot = self.__slots[position]
                if position == start_slot and self.__count == self.__size:
                    return None

    def __delitem__(self, key):
        return self.delete(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __getitem__(self,key):
        return self.get(key)

    def __len__(self):
        return self.__count

    def __contains__(self, key):
        return self.get(key) != None

    def load(self):
        #"+1"assume the new slot and data is put inside the hash table, then check the load factor if the hash table size need to be resized
        load_factor = (self.__count+1) / self.__size
        return load_factor

    #check if a number is prime or not
    def is_prime(self, num):
        if num >= 2:
            for y in range(2, num):
                if num % y == 0:
                    return False
        return True

    def get_nearest_prime(self,num):
        for i in range(2*num, num, -1):
            if self.is_prime(i) == True:
                new_size = i
                break
        return new_size
        
    def resize(self, num):
        return self.get_nearest_prime(num)

    #The original str_rep is "[", then I change it to "{" for the test case
    def __repr__(self):
        str_rep = "{"
        for i in range(len(self.__slots)):
            key = self.__slots[i]
            data = self.__data[i]
            info = ""
            if key == None or key == self.__deleted:
                info = ""
            else:
                if data == None:
                    info = str(key) + ":None"
                else:
                    info = str(key) + ":" + str(data)
            str_rep += info + ", "
        return str_rep[:-2] + "}"
                
