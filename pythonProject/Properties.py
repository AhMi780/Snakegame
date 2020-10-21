class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    # one common use of property to make a attribure read-only
    @property
    def pineAppleAllowed(self):
        x = 10
        return x


piza = Pizza(['cheese', 'tomato', ])

print(piza.pineAppleAllowed)


# ===================================================

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def isadult(self):
        if self.age >= 18: return True
        return False


ali = Person(18)

print(ali.isadult)
