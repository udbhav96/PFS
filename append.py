#Try 1 (40 min)
list = [1,2,3,4]
lst = [ ]
item =  5 
def append(list, item):
    lst = [0]*(len(list)+1)
    for i in range(len(list)):
        lst[i]= list[i]
    lst[len(list)] = item 
    return(lst)
print(append(list , item))
'''
This code defines a custom function append that mimics the behavior of the built-in append method for lists. The function takes two arguments: an input list (list) and an item (item) to append to the list. It performs the following steps:

1.Create a New List: A new list lst is created with one additional space to accommodate the new item. This is done by initializing lst with zeros, where the size is one more than the original list's length.
2.Copy Elements: The elements from the original list are copied into the new list using a for loop.
3.Append the Item: The specified item is added to the last position of the new list.
4.Return the New List: The function returns the modified list with the appended item.

'''
'''Concept : 
A placeholder is a temporary value used in a program to reserve space or indicate that a value will be provided later. Placeholders are often used in data structures (like lists or arrays) or during calculations when the actual data is not yet available. They can be any value, such as 0, None, an empty string "", or any custom value.


'''