
# Note: if the file did exist,
# Python would have deleted it and created a new one, so be careful when using this technique! In a
# moment, you learn to check to see if a file exists priorto creating one.
# def make():
#     a = open("test.txt","w")
#     a.write("first write")
#     a.close()
#
# make()


# A function can call itself safely because Python keeps track of the arguments and local variables in each
# running instance of the function, even if one is called from another. In this case, when split_fully calls
# itself, the outer (first) instance doesn ’ t lose its value of nameeven though the inner (second) instance
# assigns a different value to it, because each has its own copy of the variable name. When the inner
# instance returns, the outer instance continues with the same variable values it had when it made the
# recursive call.

# def test(parm):
#     print(parm)
#     if (parm == 0):
#         return 0
#     else:
#         return test(parm - 1)
#
# print(test(2))


# import shutil
#
# shutil.move("test.txt","test.txt.bak")
