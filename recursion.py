# def print_lol(the_list):
#     for each_item in the_list:
#         if isinstance(each_item, list):
#             print_lol(each_item)
#         else:
#             print(each_item)

import nester

from nester import print_lol

m_array = ['a','b','c',['d',['e','f']]]

# namespace
# nester.print_lol(m_array)
#
# print_lol(m_array)
nester.print_lol(m_array,3);