import re

classes = [('Keyword', r'for|if|else|while|elif|def'),
            ('Init', r'init'),
           ('Datatypes', r'int|str|complex|list|range|bool'),
           ('Punctuators', r'\(|\)|\{|\}|\[|\]|,|;|:'), 
           ('Assignment', r'='), ('RO_le', r'<='),
           ('RO_l', r'<'), ('RO_g', r'>|>=|<>'),
           ('LO_OR', r'OR|AND|NOT'),
           ('MO_plus', r'\+|\%|-|\*|\/'),
           ('Increment', r'\+\+'), ('Dectrement', r'\--'),
           ('Literal', r'([\d]+)|([\d]*.[\d]+)|\"(.+?)\"|(true)|(false)'), 
           ('Identifier', r'[A-Za-z_]+'),
           ('Whitespace', r'[\n]|[ \t]+'), 
           ('Unknown', r'.')]
tokens_join = '|'.join('(?P<%s>%s)' % x for x in classes)
# print(tokens_join)
lin_start = 0

token = []
lexeme = []
lexemeList = []
cleanCodeFile = open('cleanCode.txt', 'r')
code = cleanCodeFile.read()
cleanCodeFile.close()

for m in re.finditer(tokens_join, code):
    print(m.lastgroup)
    token_type = m.lastgroup
    token_lexeme = m.group(token_type)
    # print(f"[{token_type}, {token_lexeme}]")

    if token_type == 'Whitespace':
        continue
    else:
        token.append(token_type)
        lexeme.append(token_lexeme)
        lexemeList.append(f"< {token_type},{token_lexeme} >")
        # lexemeList.append(token_lexeme)

        # return token, lexeme, row, column
lexemes = '\n'.join(lexemeList)
lexemesFile = open("lexemes.txt", 'w')
lexemesFile.write(lexemes)
lexemesFile.close()