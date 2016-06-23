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







