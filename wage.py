import locale

class Player(object):
    
    def __init__(self, name, status, wage):
        self.name = name
        self.status = status
        self.wage = self.wage_convert(wage)

    def wage_convert(self, wage):
        locale.setlocale(locale.LC_NUMERIC,"gbp")
        wage_alt = wage[1:-4]
        wage = int(locale.atof(wage_alt))
        return wage

    def __str__(self):
        return "(" + str(self.name) + ", " + str(self.status) + ", " + str(self.wage) + ")"

# player = Player("Giorgio Addessi", "Star Player", "£6,250 p/w")
# print(player.__str__())

