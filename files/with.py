# The withstatement, when used with files, can
#     dramatically reduce the amount of code you have to write, because it negates
# the need to include a finallysuite to handle the closing of a potentially
# opened data file.

# When you use with, you no longer have to worry about closing any opened
# files, as the Python interpreter automatically takes care of this for you. The
#     withcode on the the right is identicalin function to that on the left. At Head
# First Labs, we know which approach we prefer.

# The with statement takes advantage of a Python technology
# called the context management protocol.

try:
    with open('its.txt', "w") as data:
        print("It's ...", file=data)
except IOError as err:
    print('File error: ' + str(err))
