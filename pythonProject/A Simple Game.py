
def get_input():
    comman = input(": ").split()
    verb_word = comman[0]
    if verb_word in verb_dic:
        verb = verb_dic[verb_word]
    else:
        print(f"unknown verb{verb_word}")
        return
    if len(comman) >= 2:
        noun_w = comman[1]
        print(verb(noun_w))
    else:
        print(verb('nothing'))

def say(noun):
    return f"you said '{noun}'"

verb_dic = {
    'say': say,
}

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self,name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc (self):
        return self.class_name + '\n' + self.desc

class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return f"There is no {noun} here"
verb_dict = {
    "say": say,
    "examine": examine,
}
while True:
    get_input()