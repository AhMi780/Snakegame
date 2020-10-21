class Queu:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return f"Queue({self._hiddenlist})"


x = Queu([1, 2, 3])
print(x)
x.push(0)
print(x)
x.pop()
print(x)

print(x._hiddenlist)

# ==============================================================================
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)