import time
import sys

class Leaderboard:
    """
    The is a script for checking the rank of a player after a number of games
    assuming the board is already comtaining a number of players with their ranks
    already stated. When the scores are being entered, it should be done with the
    values seperated by spaces ' ' and not any other character.
    """

    def __init__(self):
        n = int(input("Enter the number of players\n"))
        sc = input("Enter the scores of each player in decending order\n")
        
        self.board = [int(i) for i in sc.split(" ")]

        if len(self.board) != n:
            print('Number of scores do not correspond')
            time.sleep(2)
            sys.exit()
        
        b = set(self.board)
        a = list(b)
        self.table = []
        while len(a) != 0:
            m = max(a)
            self.table.append(m)
            a.remove(m)

        m = int(input('Enter the number of games palyed by Alice\n'))
        sco = input("Enter Alice game scores\n")

        lst = [int(i) for i in sco.split(" ")]
        if len(lst) != m:
            print('Number of scores do not correspond')
            time.sleep(2)
            sys.exit()

        ans = []
        for i in lst:
            u = self.rank(i)
            ans.append(u)

        for val in ans:
            print(val)

    def add_score(self, score):
        if score in self.table:
            pass
        else:
            for val in self.table:
                if score > val:
                    a = self.table.index(val)
                    self.table.insert(a,score)
                    break
                else:
                    pass
            if score < self.table[-1]:
                self.table.append(score)

    def rank(self, score):
        r_rank = 0
        self.add_score(score)
        for val in self.table:
            if val is score:
                a = self.table.index(val)
                r_rank = a+1
                break
        return r_rank

    
Leaderboard()

