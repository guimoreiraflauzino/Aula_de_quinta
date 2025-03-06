import random
import concurrent.futures
import numpy as np
import pandas as pd

# Função para calcular a soma e o quadrado dos números em um segmento
def calcular_soma_e_quadrado(start, end, data):
    soma = sum(data[start:end])
    soma_quadrados = sum(x ** 2 for x in data[start:end])
    return soma, soma_quadrados

# Função principal
def main():
    # Gerar 100.000 números aleatórios
    n = 100000
    data = [random.uniform(0, 100) for _ in range(n)]

    # Dividir o trabalho em 3 partes
    num_threads = 3
    chunk_size = n // num_threads
    results = []

    # Usar ThreadPoolExecutor para distribuir o trabalho entre threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(calcular_soma_e_quadrado, i * chunk_size, (i + 1) * chunk_size, data)
            for i in range(num_threads)
        ]
        
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    # Calcular a soma total e a soma dos quadrados
    soma_total = sum(result[0] for result in results)
    soma_quadrados_total = sum(result[1] for result in results)

    # Calcular média e desvio padrão
    media = soma_total / n
    variancia = (soma_quadrados_total / n) - (media ** 2)
    desvio_padrao = np.sqrt(variancia)

    print(f"Média: {media}")
    print(f"Desvio Padrão: {desvio_padrao}")

    # Criar planilha Excel para confirmar o resultado
    df = pd.DataFrame(data, columns=["Valores Aleatórios"])
    df['Média'] = media
    df['Desvio Padrão'] = desvio_padrao

    # Salvar em um arquivo Excel
    df.to_excel("resultados.xlsx", index=False)

if __name__ == "__main__":
    main()
