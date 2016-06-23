# print(not 5 > 2);


# However, if the first if ...:statement is true, the second one at the same level will be evaluated. The
# outcome of a comparison only determines whether the indented code beneath it will be run. Code at
# the same level, or above, won ’ t be stopped without something special happening, such as an error or
# another condition that would prevent the program from continuing to run.


# block by indentation
# i = 5;
# while(i > 0):
#     print(i);
#     i = i -1;

# for i in range(10, 0, -1):
#     print(i);
#
# for i in range(10):
#     print(i);

# sum = 0;
# for a in (1,2,3):
#     sum += a;
# print(sum);


# not flexible as javascript
key_list = {'a': 1}
try:
    if key_list['a'] == 1:
        print('a=%d' % 1)
    if key_list['b'] == 1:
        print("ok")
except KeyError:
    print("error")
except TypeError:
    pass


