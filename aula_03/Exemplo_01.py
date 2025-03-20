import random
import threading
import time

# Função principal do QuickSort com uso de threads
def quicksort_thread(arr, result, index):
    if len(arr) <= 1:
        result[index] = arr
        return

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô

    # Criação de threads para ordenar left e right simultaneamente
    left_result = [None]
    right_result = [None]

    # Funções para ordenar left e right
    def sort_left():
        quicksort_thread(left, left_result, 0)

    def sort_right():
        quicksort_thread(right, right_result, 0)

    # Threads para ordenar as sublistas
    left_thread = threading.Thread(target=sort_left)
    right_thread = threading.Thread(target=sort_right)

    left_thread.start()
    right_thread.start()

    # Aguardar as threads terminarem a execução
    left_thread.join()
    right_thread.join()

    # Combina os resultados após as threads terminarem
    result[index] = left_result[0] + [pivot] + right_result[0]

# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort com threads
def quicksort_main_com_threads():
    numeros = gerar_numeros_aleatorios()
    
    print("Primeiros 10 números antes da ordenação:", numeros[:10])

    result = [None]  # Lista que armazenará o resultado final
    start_time = time.time()
    quicksort_thread(numeros, result, 0)
    end_time = time.time()
    
    print("Primeiros 10 números após a ordenação:", result[0][:10])
    print(f"Tempo com threads: {end_time - start_time:.4f} segundos")
    return result[0]

# Função principal para testar o QuickSort sem threads
def quicksort_main_sem_threads():
    numeros = gerar_numeros_aleatorios()

    print("Primeiros 10 números antes da ordenação:", numeros[:10])

    start_time = time.time()
    numeros_ordenados = quicksort(numeros)
    end_time = time.time()

    print("Primeiros 10 números após a ordenação:", numeros_ordenados[:10])
    print(f"Tempo sem threads: {end_time - start_time:.4f} segundos")
    return numeros_ordenados

# Função de ordenação QuickSort tradicional (sem threads)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô
    return quicksort(left) + [pivot] + quicksort(right)

# Função principal para iniciar o programa
if __name__ == "__main__":
    # Testando com threads
    print("=== QuickSort com Threads ===")
    result_com_threads = quicksort_main_com_threads()

    # Testando sem threads
    print("\n=== QuickSort sem Threads ===")
    result_sem_threads = quicksort_main_sem_threads()

    # Verificar se os resultados são iguais
    assert result_com_threads == result_sem_threads, "Os resultados não são iguais!"
    print("\nOs resultados com e sem threads são iguais.")
