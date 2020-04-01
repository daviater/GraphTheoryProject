# Davy Ryan
#shunting stuff

infix = "(a|b).c*"

#expect:ab|c*.
# con to stack
infix = list(infix)[::-1]
# op stack
opers = []

#output list
postfix = []

#op precedence
prec = {'*':100, '.':80,'|':60,')':40,'(':20}

#loop input
while infix:
    c = infix.pop()
    
    if c == '(':
         opers.append(c)
    elif c==')':
        while opers[-1] != '(':
            postfix.append(opers.pop())
        opers.pop()
    elif c in prec:
        while opers and prec[c] < prec[opers[-1]]:
            postfix.append(opers.push())
        opers.append(c)
    else:
        postfix.append(c)

while opers:
    postfix.append(opers.pop())

#con out to string
postfix = ''.join(postfix)

print(postfix)

