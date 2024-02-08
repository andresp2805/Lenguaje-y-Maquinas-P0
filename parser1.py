import lexer as lx

lista_prueba = [{'LPAREN': '('}, {'COMMAND': 'defvar'}, {'NAME': 'rotate'}, {'INT: ': '3'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'if'}, {'LPAREN': '('}, {'CONDITION': 'can-move?'}, {'INPUT': ':north'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'move-dir'}, {'INT: ': '1'}, {'INPUT': ':north'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'null'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'if'}, {'LPAREN': '('}, {'CONDITION': 'not'}, {'LPAREN': '('}, {'CONDITION': 'blocked?'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'move'}, {'INT: ': '1'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'null'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'turn'}, {'INPUT': ':left'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'defvar'}, {'NAME': 'one'}, {'INT: ': '1'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'defun'}, {'NAME': 'foo'}, {'LPAREN': '('}, {'PARAMETER': 'c'}, {'PARAMETER': 'p'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'put'}, {'INPUT': ':chips'}, {'PARAMETER': 'c'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'put'}, {'INPUT': ':balloons'}, {'PARAMETER': 'p'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'move'}, {'NAME': 'rotate'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'NAME': 'foo'}, {'INT: ': '1'}, {'INT: ': '3'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'defun'}, {'NAME': 'goend'}, {'LPAREN': '('}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'if'}, {'LPAREN': '('}, {'CONDITION': 'not'}, {'LPAREN': '('}, {'CONDITION': 'blocked?'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'LPAREN': '('}, {'COMMAND': 'move'}, {'NAME': 'one'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'NAME': 'goend'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'null'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'defun'}, {'NAME': 'fill'}, {'LPAREN': '('}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'repeat'}, {'CONSTANTS': 'spaces'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'if'}, {'LPAREN': '('}, {'CONDITION': 'not'}, {'LPAREN': '('}, {'CONDITION': 'iszero?'}, {'CONSTANTS': 'mychips'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'put'}, {'INPUT': ':chips'}, {'INT: ': '1'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'CONTROL_STRUCTURE': 'defun'}, {'NAME': 'pickallb'}, {'LPAREN': '('}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'pick'}, {'INPUT': ':balloons'}, {'CONSTANTS': 'balloonshere'}, {'RPAREN': ')'}, {'RPAREN': ')'}, {'LPAREN': '('}, {'COMMAND': 'run-dirs'}, {'INPUT': ':left'}, {'STR': ':up'}, {'INPUT': ':left'}, {'STR': ':down'}, {'INPUT': ':right'}, {'RPAREN': ')'}]

def contar_parentesis(lista):
    derecho = 0
    izquierdo = 0
    for j in lista:
        for i in j.values():
            if i == '(':
                izquierdo += 1
            elif i == ')':
                derecho += 1
    if derecho != izquierdo:
        return False
    else:
        return True
contar_parentesis(lista_prueba)


