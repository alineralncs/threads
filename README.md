# Implementação de Threads em python
## Primeira atividade prática de Sistemas Operacionais - Aline Rose Alencar Santos


#### Busca Binária
A busca binária é um algoritmo de busca que recebe uma lista ordenada. Assim, a ideia é que a procura por um determinado item irá começar no meio. Se o elemento for esse, então o algoritmo retornará a sua posição, mas se não, utilizamos o fato da ordenação da lista pra eliminar a parte que sabemos que o item não está. Então, se o item for menor que o elemento do meio, então levamos em consideração que a parte inferior ao meio. Da mesmo forma para caso o item for maior que o elemento do meio, consideramos então a parte superior ao item. 

#### Ideia da implementação das threads
Utilizando o conceito da busca foi feito então a implementação de threads de duas funções de busca binárias diferentes. Essas recebem dois argumentos: uma lista ordenada de 10.000 números aleatórios e um item aleatório.

A primeira thread ***thread_bsearch_sort*** chama a função **binary_search_sort_method** que recebe 
o array de números aleatórios ordenados (na função orted_array) por o metódo sort() do python e recebe também um item aleatório para buscar nesse array. 

A segunda thread ***thread_bsearch_bubblesort*** chama a função **binary_search_bubble_sort_method** que recebe o array de números aleatórios ordenados (na função bubble_sorted_array) utilizando o método bubble sort e recebe também um item aleatório para buscar nesse array. 

Como eu utilizei número aleatórios, é possível que o item gerado para ser buscado no array não esteja lá, por isso, rode novamente caso queira achar um item diferente em uma lista diferente :)
