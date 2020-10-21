class dad :
    bascitball = 1
    __private = 'this variable is private'
    _protected = 'this variable is protected we can use it in subclasses'

class son(dad) :
    dance = 1
    breakDance = 3
    def isdance(self):
        return f"yes i dance {self.dance}"

class grandson (son) :
    dance = 6
harry = dad()
larry = son()
perry = grandson()

print(larry._dad__private)
print(perry._protected)
print(perry.breakDance)