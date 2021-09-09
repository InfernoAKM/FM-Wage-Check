import locale

class Player(object):
    
    def __init__(self, name, status, wage):
        self.name = name
        self.status = status
        self.wage = self.wage_convert(wage)

    # Converts string to int
    def wage_convert(self, wage):
        locale.setlocale(locale.LC_NUMERIC,"gbp")
        wage_alt = wage[1:-4]
        wage = int(locale.atof(wage_alt))
        return wage

    # Getters
    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_wage(self):
        return self.wage
    
    # Setters
    def set_name(self, name):
        self.name = name

    def set_status(self, status):
        self.status = status

    def set_wage(self, wage):
        self.wage = self.wage_convert(wage)
    
    # Print
    def __str__(self):
        return str(self.name) + ", " + str(self.status) + ", " + "£{:,}".format(self.wage)

