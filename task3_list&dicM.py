# List methods
#1 append(): Adds a single element to the end of the list

my_cmp = [1,2,3]
my_cmp.append(4)
print(my_cmp)

#2 extend(): Adds each element of the iterable (eg., another list,tuple,etc.) to the end of the current list.

my_cmp = [1,2]
my_cmp.extend([3,4])
print(my_cmp)

#3 insert(): Insert an item at a specific position in the list. All elements after the specified position are shifted to the right.

my_cmp = [1,3,4]
my_cmp.insert(1,2)
print(my_cmp)
 
#4 remove(): Removes the first item from the list that matches the value.

my_cmp = [1,2,3,4,5,6]
my_cmp.remove(3)
print(my_cmp)

#5 pop(): Removes and returns the item at the specified index.If no index is provided, it removes the last item.

my_cmp = [1,2,3]
item = my_cmp.pop(1)
print(item)
print(my_cmp)

#6 clear(): Removes all elements from the list, leaving it empty.

my_cmp = [1,2,3]
my_cmp.clear()
print(my_cmp)

#7 index: Returns the index of the first occurrence of the specified item between optional start and end indices. Raises a valueError if the item is not found.

my_cmp = [1,2,3,4,2]
print(my_cmp.index(2))

#8 Count(): Returns the number of occurrences of the specified item in the list.

my_cmp = [1,2,3,2,2]
print(my_cmp.count(2))

#9 sort(): Sorts the list in ascending order by default. If reverse=True, the list is sorted in desc order.you can pass a custom sorting key func.

my_cmp = [3,1,4,2]
my_cmp.sort()
print(my_cmp)

#10 reverse(): Reverse the order of elements in the list in place.

my_cmp = [1,2,3,4,5,8]
my_cmp.reverse()
print(my_cmp)

#11 copy(): Returns a shallow copy of the list.It does not modify the original list.

my_cmp = [1,2,3]
new_cmp = my_cmp.copy()
print(new_cmp)

# Dictionary Methods 
#1 get(): Returns the value associated with key if the key is present in the dictionary.Otherwise,it returns the default value,which is None by deault.

my_emp = {'a':1,'b':2}
print(my_emp.get('a'))
print(my_emp.get('c','N/A'))

#2 items(): Returns a view object containing a list of key-value pairs(tuples) in the dictionary.

my_emp = {'a':1,'b':2}
print(my_emp.items())

#3 Keys(): Returns a view object conatining a list of all keys in the dictionary.

my_emp = {'a':1,'b':2}
print(my_emp.keys())

#4 values(): Returns a view object containing a list of all values in the dictionary.

my_emp = {'a':1, 'b':2}
print(my_emp.values())

#5 Update(): updates the dict with key-value pairs from another dictionary or an iterable of key-value pairs. If a key already exists,its value is updates.
my_emp = {'a':1, 'b':2}
my_emp.update({'b':3,'c': 4})
print(my_emp)

#6 pop(): Removes the specified key and returns the corresponding value. if the key is not found, returns the default value(if provided).

my_emp = {'a':1, 'b':2}
value = my_emp.pop('b')
print(value)
print(my_emp)

#7 popitem(): Removes and returns the last inserted key-value pair as a tuple.Raises keyError if the dict is empty.

my_emp = {'a':1, 'b':2}
item = my_emp.popitem()
print(item)
print(my_emp)

#8 clear(): Removes all key-value pairs from the dict, leaving it empty.

my_emp = {'a':1, 'b':2}
my_emp.clear()
print(my_emp)

#9 setdefault(): If the key is in the dict, returns its value.

my_emp = {'a': 1}
value = my_emp.setdefault('b',3)
print(value)
print(my_emp)

#10 copy(): Returns a shallow copy of the dict.

my_emp = {'a':1, 'b':2}
new_emp = my_emp.copy()
print(new_emp)