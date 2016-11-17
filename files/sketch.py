man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == "Other":
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print("The date file is missing")

print(man)
print(other)

try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')

    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('File error')
finally:
    # The locals()BIF returns a collection of
    # names defined in the current scope.
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()
