from LinkedListDLL import LinkedListDLL

my_list = LinkedListDLL()
for node in my_list:
    print(node, end=" ")
print()
for x in range(1,10):
    if x % 2 == 0:
        my_list.add_to_head(x)
    else:
        my_list.add_to_tail(x)
print("Contents:", end=" ")
for node in my_list:
    print(node,end=" ")
print()
my_list.remove_from_head()
my_list.remove_from_tail()
my_list.remove_from_tail()
print("Contents:",end=" ")
for node in my_list:
    print(node, end=" ")
print()
