def sani(x):
    return x + 1

class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return (sorted(set([sani(t) for t in self]))[0:3])

vera = AthleteList('vela')
vera.append("123")
vera.extend([1,3,4])