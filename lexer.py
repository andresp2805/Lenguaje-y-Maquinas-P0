
COMMAND = ['defvar','=','move','skip','turn','face','put','pick','move-dir','run-dirs','move-face','null']
for i in range(0,len(COMMAND)):
    COMMAND[i] = COMMAND[i].lower()
    
CONSTANTS = ['Dim','myXpos','myYpos','myChips','myBalloons','balloonsHere','ChipsHere','Spaces']
for i in range(0,len(CONSTANTS)):
    CONSTANTS[i] = CONSTANTS[i].lower()
    
CONTROL_STRUCTURE = ['if','loop','repeat','defun']
for i in range(0,len(CONTROL_STRUCTURE)):
    CONTROL_STRUCTURE[i] = CONTROL_STRUCTURE[i].lower()
    
CONDITION = ['facing?','blocked?','can-put?','can-pick?','can-move?','isZero?','not']
for i in range(0,len(CONDITION)):
    CONDITION[i] = CONDITION[i].lower()

D = [':left', ':right', ':around', ':north', ':south', ':east', ':west', ':balloons', ':chips', ':front', ':back']

def leer_archivo(file_path):
    with open(file_path, 'r') as file:
        contenido = file.read()
    return contenido

def procesar_codigo(codigo):
    codigo = ' '.join(codigo.split())
    codigo = codigo.replace('\n', ' ')
    codigo = codigo.replace(': ', ':')
    codigo = codigo.replace('. ', '.')
    codigo = codigo.replace(' .', '.')
    return codigo.lower()

def obtener_lista_tokens(contenido):
    contenido = contenido.replace('(', ' ( ').replace(')', ' ) ')
    tokens = contenido.split()
    return tokens

def crear_tokens(lista_tokens):
    lista = []
    for i in range(0,len(lista_tokens)):
        if lista_tokens[i] == '(':
            lista.append(('LPAREN' , '('))
        elif lista_tokens[i] == ')':
            lista.append(('RPAREN' , ')'))
        elif lista_tokens[i] in COMMAND:
            lista.append(('COMMAND' , lista_tokens[i]))
        elif lista_tokens[i] in CONSTANTS:
            lista.append(('CONSTANTS' , lista_tokens[i]))
        elif lista_tokens[i] in CONTROL_STRUCTURE:
            lista.append(('CONTROL_STRUCTURE' , lista_tokens[i]))
        elif lista_tokens[i] in CONDITION:
            lista.append(('CONDITION' , lista_tokens[i]))
        elif lista_tokens[i] in D:
            lista.append(('INPUT' , lista_tokens[i]))
        elif is_a_number(lista_tokens[i]) == int:
            lista.append(('INT' , lista_tokens[i]))
        elif is_a_number(lista_tokens[i]) == float:
            lista.append(('FLOAT' , lista_tokens[i]))
        else:
            lista.append(('USER PARAMETER' , lista_tokens[i]))
    return lista

def is_a_number(s):
    try:
        int_value = int(s)
        return int
    except ValueError:
        try:
            float_value = float(s)
            return float
        except ValueError:
            return str