#Davy Ryan

class State:

    edges = []
     
    #none means epsilon
    label = None

    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

        
class Frag:
    start = None
    accept = None

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

myinstance = State(label='a', edges=[])
myotherinstance = State(edges=[myinstance])
myfrag = Frag(myinstance, myotherinstance)
print(myinstance.label)
print(myotherinstance.edges[0])
print(myfrag)
