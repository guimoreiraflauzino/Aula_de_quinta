import threading
import time

contadoralta = 0
contadorbaixa = 0


lock = threading.Lock()


def altaPrioridade():
    global contadoralta
    for _ in range(10):  
        with lock:
            print("[alta prioridade] usando recurso")
            contadoralta += 1
            time.sleep(0.9)  


def baixaPrioridade():
    global contadorbaixa
    for _ in range(10):  
        with lock:
            print("[baixa prioridade] usando recurso")
            contadorbaixa += 1
            time.sleep(0.8)  


def main():
   
    t1 = threading.Thread(target=altaPrioridade)
    t2 = threading.Thread(target=baixaPrioridade)
    
   
    t1.start()
    t2.start()

   
    t1.join()
    t2.join()

    time.sleep(10)

    print(f"Contador Alta Prioridade: {contadoralta}")
    print(f"Contador Baixa Prioridade: {contadorbaixa}")



