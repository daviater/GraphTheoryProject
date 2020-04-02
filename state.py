#Davy Ryan

class State:

    edges = []
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

def shunt(infix):
    infix = list(infix)[::-1]
    opers=[]
    postfix=[]
    prec={'*':100,'.':80,'|':60,')':40,'(':20}
    while infix:
        c=infix.pop()
        if c=='(':
            opers.append(c)
        elif c==')':
            while opers[-1] != '(':
                postfix.append(opers.pop())
            opers.pop()
        elif c in prec:
            while opers and prec[c] < prec[opers[-1]]:
                 postfix.append(opers.pop())
            opers.append(c)
        else:
            postfix.append(c)
    while opers:
        postfix.append(opers.pop())
    postfix=''.join(postfix)
    return postfix

def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        c = postfix.pop()
        if c == '.':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            frag2.accept.edges.append(frag1.start)
            newfrag = Frag(frag2.start, frag1.accept)
            nfa_stack.append(newfrag)
        elif c == '|':
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            newfrag = Frag(start, accept)
            nfa_stack.append(newfrag)
        elif c == '*':
            frag = nfa_stack.pop()
            accept = State()
            start = State(edges=[frag.start, accept])
            frag.accept.edges.append(frag.start)
            frag.accept.edges.append(accept)
            newfrag = Frag(start, accept)
            nfa_stack.append(newfrag)
        else:
            accept = State()
            initial = State(label=c,edges=[accept])
            newfrag = Frag(initial, accept)
            nfa_stack.append(newfrag)
    return nfa_stack.pop()

def followes(state, current):
    if state not in current:
        current.add(state)
        if state.label is None:
            for x in state.edges:
                followes(x,current)

def match(regex,s):
    nfa = regex_compile(regex)

    current = set()

    followes(nfa.start, current)
    
    previous = set()

    for c in s:
        previous = current
        current = set()
        for st in previous:
            if st.label is not None:
                if st.label == c:
                    followes(st.edges[0], current)

    return nfa.accept in current

print(match("a.b|b*", "bbbbbbbbbbb"))
