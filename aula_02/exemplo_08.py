import threading
import time 
contador = 0
lock = threading.Lock()  # Criando o lock

def incrementar():
    global contador
    for _ in range(1000000):
        time.sleep(0.0000000000000000000000000000001)
        with lock:  # Garantindo que apenas uma thread acesse a variável de cada vez
            contador += 1

threads = [threading.Thread(target=incrementar) for _ in range(10)]
for t in threads: 
    t.start()

for t in threads: 
    t.join()

print(f"contador final: {contador}")

