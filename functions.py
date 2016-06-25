#!/usr/bin/env python 3.1
#You can do two things to make your programs easy to run. The first line of all of your Python files
#should look like above:

# To create a named function that will contain your code, you use the word def, which you can think of as
# defininga functional block of code.

# def in_te():
#     return 1
# print(in_te())

# docstring
# pString = [1,2,3]
# def test_doc(parm):
#     """this is a doc"""
#     parm = parm[1:2]
      # Like other language, python pass object, operation on object will affect the original object
#     parm = pString.pop(0)
#     return parm
#
# print("%s" % test_doc.__doc__)
#
# print("%s" % test_doc.__code__)
#
# print(test_doc(pString))
#
# print(pString)

# The parameters that you intend to be used could be expecting different types than what they are given
# when the function is called. For example, you could write a function that expects to be given a dictionary
# but by accident is instead given a list, and your function will run until an operation unique to a
# dictionary is accessed. Then the program will exit because an exception will be generated. This is
# different from some other languages, which try to ensure that the type of each parameter is known, and
# can be checked to be correct.
# more like javascript

# print(type("adsda"))

# If you write a function with more than one parameter and you want to have both required and optional
# parameters, you have to place the optionals at the end of your list of parameters. This is because once
# you ’ ve specified that a parameter is optional; it may or may not be there. From the first optional
# parameter, Python can ’ t guarantee the presence of the remaining parameters — those to the right of your
# optional parameters. In other words, every parameter after the first default parameter becomes optional.
# This happens automatically, so be careful and be aware of this when you use this feature.

# support dynamically add element
ingredient = {'a':1}
ingredient['b'] = 2;
print(ingredient)
for ins in ingredient.keys():
    print(ingredient[ins])




