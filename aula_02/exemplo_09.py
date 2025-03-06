import threading
import time

contadoralta = 0
contadorbaixa = 0

# Lock para proteger o acesso aos recursos compartilhados
lock = threading.Lock()

# Função para a thread de alta prioridade
def altaPrioridade():
    global contadoralta
    for _ in range(10):  # Limitar o número de iterações
        with lock:
            print("[alta prioridade] usando recurso")
            contadoralta += 1
            time.sleep(0.9)  # Simula um processamento mais longo

# Função para a thread de baixa prioridade
def baixaPrioridade():
    global contadorbaixa
    for _ in range(10):  # Limitar o número de iterações
        with lock:
            print("[baixa prioridade] usando recurso")
            contadorbaixa += 1
            time.sleep(0.8)  # Simula um processamento mais curto

# Função principal para iniciar as threads
def main():
    # Criando as threads
    t1 = threading.Thread(target=altaPrioridade)
    t2 = threading.Thread(target=baixaPrioridade)
    
    # Iniciando as threads
    t1.start()
    t2.start()

    # Aguardando o término das threads
    t1.join()
    t2.join()

    # Imprimir os resultados após a execução das threads
    print(f"Contador Alta Prioridade: {contadoralta}")
    print(f"Contador Baixa Prioridade: {contadorbaixa}")

if __name__ == "__main__":
    main()
