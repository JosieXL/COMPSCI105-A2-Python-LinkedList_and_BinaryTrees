from HashTable import HashTable
import random

animal_list = ["aardvark", "bull", "cat", "dog", "elephant", "frog",\
               "goat", "horse"]
print("Test 1")
print("------")
h_table = HashTable()
print("Insertion:")
for i in range(len(animal_list)):
    h_table[i] = animal_list[i]
    print("key:",i,"data:",animal_list[i])
    print(h_table,"count:",len(h_table))
print()
print("Deletion:")
for i in range(len(animal_list)):
    del(h_table[i])
print(h_table,"count:",len(h_table))
print()

print("Test 2")
print("------")
h_table = HashTable()
print("Insertion:")
for i in range(len(animal_list)):
    key = random.randrange(0,1000)
    h_table[key] = animal_list[i]
    print("key:",key,"data:",animal_list[i])
    print(h_table,"count:",len(h_table))
print()
