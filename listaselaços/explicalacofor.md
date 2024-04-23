O laço de repetição for é utilizado para percorrer uma sequência de elementos, como uma lista, e executar um bloco de código para 
cada elemento dessa sequência. Ele é muito útil quando você precisa realizar uma operação para cada item em uma coleção de dados, 
como por exemplo, exibir todos os itens de uma lista, somar todos os elementos de uma lista, entre outras operações.Por exemplo, no
 contexto da aula, o laço for foi utilizado para percorrer a lista de restaurantes cadastrados e exibir o nome de cada restaurante.
 
Dessa forma, a cada iteração do laço, o nome de um restaurante era exibido na tela.Para fixar o conceito, você pode criar um
exercício prático utilizando o laço for. Que tal criar um programa que percorre uma lista de números e exibe o dobro de cada 
número? Isso pode te ajudar a entender melhor como o laço for funciona na prática. Experimente criar esse programa e veja como o
 laço for pode ser útil em situações reais.

 # Definindo a lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizando o laço for para percorrer a lista e exibir o dobro de cada número
for numero in numeros:
    print(f'O dobro de {numero} é {numero * 2}')