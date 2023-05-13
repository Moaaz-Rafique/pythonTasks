from lab6LexicalAnalizer import lab6Q2
from treelib import Node, Tree


def validate(s, c, n, currentIndex, tree, index=0):
    print(f"\n{s},{currentIndex}")
    if len(s) < 1:
        return False
    if s[-1] == "$":
        if currentIndex == len(n) - 1:
            return True
    if s[-1] in c.keys():
        x = c[s[-1]]
        curr_key = s.pop()
        for y in x:
            j = len(y) - 1
            i = len(y) - 1
            index += 1
            while i >= 0:
                ch = y[i]
                s.append(ch)
                # tree.create_node(ch, ch[1:-1] + str(currentIndex), parent=curr_key)
                tree.show()
                try:
                    print(curr_key[1:-1] + str(currentIndex))
                    tree.create_node(ch[1:-1] + str(index), ch[1:-1] + str(index),
                                     parent=curr_key[1:-1] + str(index - 1))
                except:
                    try:
                        tree.remove_node(ch[1:-1] + str(index))
                        tree.create_node(ch[1:-1] + str(index), ch[1:-1] + str(index),
                                         parent=curr_key[1:-1] + str(index - 1))
                    except:
                        print("sheeeesh")

                i = i - 1
            if validate(s, c, n, currentIndex, tree, index):
                return True
            else:
                index -= 1
                for k in range(j):
                    if (len(s) > 1):
                        s.pop()
                        # s.pop()
        return False
    else:
        terminal = s.pop()
        if terminal == n[currentIndex]:
            currentIndex = currentIndex + 1
            index -= 1
            return validate(s, c, n, currentIndex, tree, index)
    return False


c = dict()
c["<Body>"] = [["<Statement>", "<Body>"], []]
c['<Statement>'] = [["<Initialize>"], ["<Operation>"], ["<CondStat>"], ["<Loop>"], ["<Print>"]]  # , ["<FunctionCall>"]

c["<Initialize>"] = [["Init", "Identifier", "Assignment", "<Expr>"]]
c["<Operation>"] = [["Identifier", "Assignment", "<Expr>"]]
c["<Expr>"] = [["<Term>", "<Expr2>"]]
c["<Expr2>"] = [["MSO", "<Term>", "<Expr2>"], []]
c["<Term>"] = [["<Factor>", "<Term2>"]]
c["<Term2>"] = [["MFO", "<Factor>", "<Term2>"], []]
c["<Factor>"] = [["LeftParenthesis", "<Expr>", "RightParenthesis"], ["Identifier"], ["Literal"]]

c["<CondStat>"] = [["<If>", "<Else>"]]
c["<If>"] = [["If", "LeftParenthesis", "<RelExpr>", "RightParenthesis", "LeftCurly", "<Body>", "RightCurly"]]
c["<Else>"] = [["Else", "LeftCurly", "<Body>", "RightCurly"], []]

c["<Bool>"] = [['<RelExpr>'], ['True'], ['False']]
c["<RelExpr>"] = [['<Expr>', 'RelOp', '<Expr>'], ["<Expr>"]]

c["<Loop>"] = [['For', "LeftParenthesis", '<Y2>', "RightParenthesis", "LeftCurly", "<Body>", "RightCurly"]]
c["<Y2>"] = [['<Initialize>', 'SemiColon', '<RelExpr>', 'SemiColon', '<Operation>']]

c["<Print>"] = [["Print", "LeftParenthesis", "<Expr>", "RightParenthesis"]]


tok = open("lexemes.txt", "r").read()
tok = tok.split('\n')
tokArray = []

for i in range(len(tok)):
    x = tok[i][2:-2].split(r",")
    tokArray.append(x)
lexSeq = []
for t in tokArray:
    lexSeq.append(t[0])
print(lexSeq)
lexSeq.append("$")
inp = [lexSeq]  #

ans = []
for n in inp:
    s = ["$", "<Body>"]
    tree = Tree()
    tree.create_node("<Body>", "Body0")

    currentIndex = 0
    try:
        print('Valid cfg',validate(s, c, n, currentIndex, tree))
        # ans.append((n, validate(s, c, n, currentIndex, tree)))
    except RecursionError:
        print("\nDepth Exceeded \n Invalid Code\nSyntax Error")

for a in ans:
    print(a)

# print("Tree----------")
# tree.show()
