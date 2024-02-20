import lexer as lx

def nombre_archivo():
    nombre_archivo = 'texto.txt'
    #str(input("Ingrese el nombre del archivo: "))
    try: 
        lista = lx.crear_tokens(lx.obtener_lista_tokens(lx.procesar_codigo(lx.leer_archivo(nombre_archivo))))
        return lista
    except FileNotFoundError:
        return 'Nombre de archivo no valido'

def defvar():
    lista = nombre_archivo()
    lista2 = []
    for i in range(0,len(lista)):
        if lista[i][0] == 'LPAREN':
            if lista[i+1][1] == 'defvar':
                if lista[i+2][0] == 'USER PARAMETER':
                    if lista[i+3][0] == 'INT':
                        if lista[i+4][0] == 'RPAREN':
                            lista2.append(lista[i][1]+lista[i+1][1]+' '+lista[i+2][1]+' '+lista[i+3][1]+lista[i+4][1])
    return lista2

print(defvar())
