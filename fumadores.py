from classes import *
from queue import Queue

if __name__ == "__main__":
    q = Queue(1)
    s = threading.Semaphore(0)


    agente = Agente(q, s)
    fumador1 = Fumador('Fumador 1', 'papel', agente, q, s)
    fumador2 = Fumador('Fumador 2', 'tabaco', agente, q, s)
    fumador3 = Fumador('Fumador 3', 'cerillas', agente, q, s)

    agente.start()
    fumador1.start()
    fumador2.start()
    fumador3.start()

    agente.join()
    fumador1.join()
    fumador2.join()
    fumador3.join()
