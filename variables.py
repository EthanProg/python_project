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

dic = {};
dic['lookta'] = 'oka';
print(dic);
print(dic['lookta']);

# Both the keys and values methods return views, which you can assign and use like any normal view.
print(list(dic.keys()));
print(list(dic.values()));

