import threading
import random
from time import sleep, perf_counter

#  Funções
# função que gera 7000 números aleatórios
def random_numbers():
    array = []
    for i in range(1, 10000):
        number = random.randint(1, 10000)
        array.append(number)
    # ordenacao do array
    return array

# função que ordena os numeros aleatorios com o metodo do python .sort()
def sorted_array():
    array = random_numbers()
    array.sort()
    # print('list', list)
    return array

# função que ordena os numeros aleatorios com o metodo bubble sort implementado
def bubble_sorted_array():
    array = random_numbers()
    for passnum in range(len(array)-1, 0, -1):
        for i in range(passnum):
            if array[i] > array[i+1]:
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux
    return array

# função que retorna um item aleatorio para achar nos arrays
def random_item_for_bsearch():
    for i in range(1, 10000):
        number = random.randint(1, 10000)
    return number

# funcao da busca binária usando o metódo sort
def binary_search_sort_method(array, item):
    print('binary search using the built-in sort method')
    # array = sort_array()
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end)
        guess = array[mid]
        if guess == item:
            print('item to be found in the built-in method:', item)
            print(f'\n yay item found in position {mid} ! \n')
            return mid
        elif guess < item:
            start = mid + 1
        else:
            end = mid - 1
    if guess != item: 
        print('sorry, item not found in built-in sort method, try again :(\n')
    sleep(2)

# funcao da busca binária usando o metódo bubblesort
def binary_search_bubble_sort_method(array, item):
    print('binary search using the bubble sort method')
    # array = bubble_sort_array()
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end)
        guess = array[mid]
        if guess == item:
            print('item to be found in the bubble sort method: ', item)
            print(f'\n yay item found in position!{mid} \n')
            return mid
        elif guess < item:
            start = mid + 1
        else:
            end = mid - 1 
    if guess != item: 
        print('sorry, item not found in bubble sort method, try again :(\n')
    sleep(2)


if __name__ == "__main__":
    start_time = perf_counter()
    thread_bsearch_sort = threading.Thread(target=binary_search_sort_method, args=(sorted_array(), random_item_for_bsearch(), ))
    thread_bsearch_bubblesort = threading.Thread(target=binary_search_bubble_sort_method, args=(bubble_sorted_array(), random_item_for_bsearch(),))

    thread_bsearch_bubblesort.start()
    thread_bsearch_sort.start()

    thread_bsearch_sort.join()
    thread_bsearch_bubblesort.join()
    
    end_time = perf_counter()

    print(f'It took {end_time-start_time: 0.2f} seconds to complete!')
    