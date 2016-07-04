# n Python, every piece of data you see or come into contact with is represented by an object. Each
# of these objects has three components: an identity, a type, and a value. The identity represents the
# location of the object being held in your memory (and therefore is unchangeable), while its type
# tells us what types of data and values it can have. The value, meanwhile, can be changed in an object,
# but only if it is set as a mutable type; if it is set as immutable, then it may not change.

# When you want to find out more about what is available in an object, Python exposes everything that
# exists in an object when you use the dir function:
# s = "ssdasd"
# print(dir(s))


# When a class is invoked, it creates an object bound to a name.


# class FirstClass:
#     """First Class"""
#     def firstMethod(self,ones):
#         return  ones + "ss"
#
# # The (self) portion is actually a variable used to represent the instance of the object.
# ss = FirstClass
# print(ss.firstMethod(ss,"123"))

