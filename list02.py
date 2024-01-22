# Lista vazia para armazenar números
numeros = []

# Lista de idades com idades
#         0    1   2   3   4   5   6   7
idades = [15, 22, 14, 31, 20, 22, 22, 15]

# Lista de nomes com nomes
nomes = ['Lucas', 'Abgail', 'Godofredo']

# Lista de cores com cores
#            0         1        2       3          4         5
cores = ['Amarelo', 'Verde', 'Roxo', 'Cinza', 'Vermelho', 'Azul']

# Lista mista com dados de tipos diferentes
mix = [23, 28.45, 'Lucas', True, [1,2,3], ['Godofredo', 'Jurema']]

# Adiciona cor amarelo ao final da lista transformando todas as letras para minúsculas 
cores.append('Amarelo'.lower())

# Adiciona cor amarelo ao final da lista transformando todas as letras para maiúsculas
cores.append('Amarelo'.upper())

# Mostra na tela a soma das idade da lista de idades
print(sum(idades))

# Inverte os elementos da lista de cores
cores.reverse()
print(cores)

# Ordena os elementos da lista de cores
cores.sort()
print(cores)

# Ordena os elementos da lista de idades
idades.sort()
print(idades)

# Junta a lista de nomes com a lista de idades
idades.extend(nomes)
print(idades)
print(nomes)

# Mostra na tela o índice da cor 'Verde' na lista de cores
print(cores.index('Verde'))

# Mostra na tela q quantidade de vezes que a idade 22 aparece na lista de idades
print(f'Números de aparições: {idades.count(22)}')

# Recebe do usuário uma cor para adicionar
corAdd = input('Cor a adicionar: ')

# Recebe do usuário uma cor para remover
corRemove = input('Cor a remover: ')

# Define uma variável para indicar se a cor existe
corExiste = False


# Verificar se a cor a ser removida existe ou não, e remove
for color in cores:
    if color == corRemove:
        corExiste = True
        
if corExiste == True:
    cores.remove(corRemove)
    print('Cor removida!')

else:
    print('Cor não encontrada!')

# Adiciona a cor digitada pelo usuário na posição 2 da lista da cores
cores.insert(2, corAdd)

# Adiciona a cor digitada pelo usuário no final da lista da cores
cores.append(corAdd)

# Remove a última cor da lista de cores
cores.pop()
print(cores)








# corPesquisa = input('Cor a pesquisar: ')

# for color in cores:
#     if corPesquisa == color:
#         print("Encontrouuuu")


# for color in cores:
#     print(color)

# print(idades[len(idades)-1])

# print(len(numeros))
# print(len(idades))

# print(max(idades))
# print(min(idades))

#print(max(cores))