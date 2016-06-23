# filler = ("1",'2','3','4');
# print(filler[0]);
#

# tuple 元组 类似javascript中的数组，定义元素可以嵌套转换成多维数组

# oneElementInTuple = ('1');
# print(oneElementInTuple[0])

# A tuple can have any kind of data in it, but after you ’ ve created one it can ’ t be changed
# Tuples are immutable because they are supposed to be used for ordered groups of things that will not
# be changed while you ’ re using them

# tumple = ('a','b');
# print(tumple);
# tumple[0] = 'c';
# print(tumple);
# Traceback (most recent call last):
# File "D:/python_project/variables.py", line 16, in <module>
# tumple[0] = 'c';
# TypeError: 'tuple' object does not support item assignment



# List
# The primary difference in using a list versus using a tuple is that a list can be modified after it has
# been created

# If you want to add more than one item to the end of a list — for instance, the contents of a tuple or of
# another list — you can use the extendmethod to append the contents of a list all at once

# list1 = ['a','b','c'];
# list1.extend(['e','f']);
# print(list1);


# dictionary
# A  dictionaryis similar to lists and tuples. It ’ s another type of container for a group of data. However,
# whereas tuples and lists are indexed by their numeric order, dictionaries are indexed by namesthat you
# choose.

# dic = {};
# dic['lookta'] = 'oka';
# print(dic);
# print(dic['lookta']);

# Both the keys and values methods return views, which you can assign and use like any normal view.
# print(list(dic.keys()));
# print(list(dic.values()));

# Python offers an interesting feature of strings. Sometimes, it is useful to be able to treat a string as though
# it were a list of individual characters.
# slicing
# stringAsArray = ['lalala','ahhaha'];
# print("%s",stringAsArray[0][0]);

# Remember that, like tuples, strings are immutable. When you are slicing strings, you are actually creating
# new strings that are copies of sections of the original string.

# print(True == 1);
# print(False == 0);

# Fortunately, Python provides a shortcut that enables you to access the last element of a
# sequence by using the number – 1, and the next - to - last  element  with  – 2, letting you reverse the order of
# the list by using negative numbers from – 1 to the number that is the negative length of the list (– 5 in the
# case of the last_names list).

# last_names = [ "Douglass","Jefferson","Williams"];
# print(last_names[-1]);
# print(last_names[-2]);

# slice_tuple = ('a','b','c','d','e','f');
# print(slice_tuple[2:6]);
# slice_list = ['a','b','c','d','e','f'];
# print(slice_list[2:6]);
#
# list_new = [];
# list_new.append(slice_list);
# print(list_new);
#
# slice_list.extend(['g']);
# print(slice_list);



# To keep your lists from becoming unwieldy, a method called popenables you to remove a specific
# reference to data from the list after you ’ re done with it. When you ’ ve removed the reference, the position
# it occupied will be filled with whatever the next element was, and the list will be reduced by as many
# elements as you ’ ve  popped.

# this is better than stack!

# pop_list = [1,2,3,4,5];
# q = pop_list.pop(0);
# print(q);
# print(pop_list);
# q = pop_list.pop(1);
# print(q);
# print(pop_list);

# Sets are similar to dictionaries in Python, except that they consist of only keys with no associated values.
# Essentially, they are a collection of data with no duplicates. They are very useful when it comes to
# removing duplicate data from data collections.

# Sets come in two types: mutableand immutable frozensets.The difference between the two is that with a
#     mutable set, you can add, remove, or change its elements, while the elements of an immutable frozenset
# cannot be changed after they have been initially set.


# Summary #
# In this chapter, you learned how to manipulate many core types that Python offers. These types are
# tuples,  lists,  dictionaries,  sets, and three special types: None, True, and False. You ’ ve also learned a special
# way that strings can be treated like a sequence. The other sequence types are tuples and lists.
# A  tupleis a sequence of data that ’ s indexed in a fixed numeric order, starting at zero. The references in
# the tuple can ’ t be changed after the tuple is created, nor can it have elements added or deleted. However,
# if a tuple contains a data type that has changeable elements, such as a list, the elements of that data type
# are not prevented from changing. Tuples are useful when the data in the sequence is better off not
# changing, such as when you want to explicitly prevent data from being accidentally changed.
# A  listis another type of sequence, which is similar to a tuple except that its elements can be modified.
# The length of the list can be modified to accommodate elements being added using the append method,
# and the length can be reduced by using the popmethod. If you have a sequence whose data you want to
# append to a list, you can append it all at once with the extendmethod of a list.
# Dictionariesare yet another kind of indexed grouping of data. However, whereas lists and tuples are
# indexed by numbers, dictionaries are indexed by values that you choose. To explore the indexes, which
# are called keys, you can invoke the keysmethod. To explore the data that is referred to, called the values,
# you can use the valuesmethod. Both of these methods return lists.
# Setsare a collection of items (0 or more), that contain no duplicates. In theory, they are similar to
# dictionaries, except that they only have keys, and no values associated with those keys. One use for sets
# is to remove any duplicates from a collection of data. They are also good at mimicking finite
# mathematical sets.
# Other data types are True,  False, and None.  Trueand Falseare a special way of looking at 1 and 0, but
# when you want to test whether something is true or false, explicitly using the names Trueand False is
# always the right thing to do. Noneis a special value that is built into Python that only equals itself, and it
# is what you receive from functions that otherwise would not return any value (such as True,  False,  a
# string, or other values).







