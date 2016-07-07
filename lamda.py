#
#
# filter_ary = [1,2,3,4,5,6]
# result = filter(lambda x: x % 2 == 0, filter_ary)
# print(*result)


map_me = ['a','b','c']
result = map(lambda x: "This letter is %s\n" % x, map_me)
print(*result)