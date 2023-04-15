from classes import *

if __name__ == "__main__":

    agente = Agente()
    fumador1 = Fumador('Fumador 1', 'papel', agente)
    fumador2 = Fumador('Fumador 2', 'tabaco', agente)
    fumador3 = Fumador('Fumador 3', 'cerillas', agente)

    agente.start()
    fumador1.start()
    fumador2.start()
    fumador3.start()

    agente.join()
    fumador1.join()
    fumador2.join()
    fumador3.join()
