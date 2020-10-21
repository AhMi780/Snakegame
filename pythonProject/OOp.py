class Employees :

    def __init__(self, first , last , pay, role):

        self.first = first
        self.last = last
        self.pay = pay
        self.role = role

    def full_Name(self):
        return f"{self.first} {self.last} "

    def emp_details(self):
        return f" The name is {self.full_Name()}. The Employe pay is {self.pay}. emp role is {self.role}"

emp1 = Employees("Usama","Kaleem",300000,"Intermediat")
naseeb = Employees('naseeb', 'ali',40000,'Senior worker')


print(emp1.emp_details())

class player:
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The name is {self.name}.The game is {self.game}"


class coolProgrammer(Employees,player ):
    languag = "c++"

    def prnt_language(self):
        print(self.languag)


naseeb = player('naseeb', ['Cricket','gulli danda'])

# abizee = coolProgrammer('abizee', 75000, )
saman = coolProgrammer('saman','baba',70000,'Cool Programmer')
cool1 = Employees('fiaz', 'musalli', 60000,'Manager')
cool2 = Employees('hamza', 'jutt', 5000 , 'worker')
cool3 = Employees('Ahmad', 'Ch', 25000 ,'Supervoiser')

print(naseeb.print_details())
print(saman.emp_details())














