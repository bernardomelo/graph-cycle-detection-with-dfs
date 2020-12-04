#Aluno: Bernardo Gomes de Melo
#Código para checar se dado grafo é cíclico ou não
def cycle_check(grafo, inicio):
    cores = {no: "branco" for no in grafo}
    cores[inicio] = "cinza"
    stack = [(None, inicio)]
    while stack:
        (prev, no) = stack.pop()
        for viz in grafo[no]:
            if viz == prev:
                pass
            elif cores[viz] == "cinza":
                return True
            else:
                cores[viz] = "cinza"
                stack.append((no, viz))
    return False

inicio = 0
#grafo = {0:[1,2,6,5], 1:[0], 2:[0], 5:[3,4,0], #grafo da questão
#3:[5,4], 4:[3,5], 6:[0,4], 7:[8], 8:[7],
#9:[10,11,12], 10:[9], 11:[12,9], 12:[11,9]}
grafo = {0:[1,3], 1:[0], 3:[0], 2:[4,5], 4:[2], 5:[2]}
out = cycle_check(grafo,inicio)

if not out:
    print('O grafo em questão:')
    print(grafo)
    print('Não possui ciclos, É acíclico!')
else:
    print('O grafo em questão:')
    print(grafo)
    print('Possui ciclo(s), ele NÃO é acíclico.')

#Caso #1: Grafo cíclico
#input grafo = {0:[1,2,6,5], 1:[0], 2:[0], 5:[3,4,0],
#3:[5,4], 4:[3,5], 6:[0,4], 7:[8], 8:[7],
#9:[10,11,12], 10:[9], 11:[12,9], 12:[11,9]}
#Output do programa:
#O grafo em questão:
#{0: [1, 2, 6, 5], 1: [0], 2: [0], 5: [3, 4, 0], 3: [5, 4], 4: [3, 5], 6: [0, 4], 7: [8], 8: [7], 9: [10, 11, 12], 10: [9], 11: [12, 9], 12: [11, 9]}
#Possui ciclo(s), ele NÃO é acíclico.

#======================================================================================================================================================

#Caso #2: Grafo acíclico
#input grafo = {0:[1,3], 1:[0], 3:[0], 2:[4,5], 4:[2], 5:[2]}
#Output do programa:
#O grafo em questão:
#{0: [1, 3], 1: [0], 3: [0]}
#Não possui ciclos, É acíclico!
