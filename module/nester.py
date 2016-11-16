""" this a comment """

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

# 方法重载
# 这一点要强于javascript
# NO!!!
# 类javascript 不支持重载 后面定义的方法会覆盖原来的
def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)