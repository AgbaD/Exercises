class Kinder:
    """
    This script is used to know the plants owned by each student as it is arranged
    based on their names i.e alphabetically from a-z.
    """
    def __init__(self):
        self.dict = {'V':'violets','C':'clover','R':'radishes','G':'grass'}
        self.row1 = input("Enter the first row of the arrangement in upper case\n")
        self.row2 = input("Enter the second row of the arrangement in upper case\n")
        print("[window][window][window]")
        print(self.row1)
        print(self.row2)
        self.main()

    def spew(self):
        self.first = []
        a = []
        for i in self.row1:
            if len(a) == 2:
                self.first.append(a)
                a = []
                a.append(i)
            else:
                a.append(i)
        if len(a) != 0:
            self.first.append(a)
        self.second = []
        b = []
        for i in self.row2:
            if len(b) == 2:
                self.second.append(b)
                b = []
                b.append(i)
            else:
                b.append(i)
        if len(b) != 0:
            self.second.append(b)

    def allocate(self):
        names = 'ABCDEFGHIJKL'
        let = [i for i in names]
        self.table = {}
        for i in let:
            u = let.index(i)
            one = self.first[u]
            two = self.second[u]
            v = []
            for val in one:
                v.append(val)
            for val in two:
                v.append(val)
            self.table[i] = v

    def decide(self, name):
        '''The first letter of the name should be in upper case'''
        l = [i for i in name]
        j = l[0]
        k = self.table[j]
        plants = []
        for i in k:
            u = self.dict[i]
            plants.append(u)
        return plants

    def main(self):
        self.spew()
        self.allocate()
        a = int(input('Enter number of test cases:\n'))
        for i in range(a):
            name = input('Enter students name\n')
            plant = self.decide(name)
            for p in plant:
                print(p, end=' ')
            print()


Kinder()