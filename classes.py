def sani(x):
    return x + 1


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([sani(x) for x in self.times]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return (Athlete(temp1.pop(0), temp1.pop(0), temp1))
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return (None)
