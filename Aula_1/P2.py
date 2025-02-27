import os
import time
import threading

def tarefa ():
    print('iniciando...')
    time.sleep(9)
    print('fim...')

t= threading.Thread(target=tarefa)
t.start()
t.join() 
print('t principal finalizada...')

tA = threading.Thread(target=tarefa)
tB = threading.Thread(target=tarefa)

tA.start()
tB.start()
tA.join()
tB.join()

print('a')
