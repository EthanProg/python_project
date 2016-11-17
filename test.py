# m = ['1','2'];
# print(m);
# m.extend(['3','4']);
# print(m);
# m.insert(0,1991);
# # for each in m:
# #     print(each)
# def printll(l):
#     print(l);
# printll(isinstance(m,list));
# x = "Hello World. You will never see this."
# print(x)

# print("hello, %s %d" % ("world!",13));

# xx = "asd:sdasd:asd";
# yy = xx.split(":",1);
# print(yy[1])

# import os
# os.path.exists("");

# Concentrate on what your code needs to do.

# def sani(x):
#     return x + 1
#
# xlist = [1,2,3,4]
#
# # What’s interesting is that the transformation has been reduced to a single line
# # of code. Additionally, there’s no need to specify the use of the append()
# # method as this action is implied within the list comprehension. Neat, eh?
#
# resout = [sani(each_x) for each_x in xlist]
#
# print(resout)


x = [1,2,3]
x.extend([4,5,6])
print(x)