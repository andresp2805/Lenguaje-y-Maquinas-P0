import lexer as lx
lista = lx.crear_tokens(lx.obtener_lista_tokens(lx.procesar_codigo(lx.leer_archivo('texto.txt'))))
print(lista)
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
