import random
import threading
import time
from queue import Queue

class Agente(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.ingredientes = None

    def poner_ingredientes(self):
        self.ingrediente = random.choice([0, 1, 2])
        if self.ingrediente == 0:
                self.ingredientes = ["papel", "tabaco"]
                q.put(self.ingredientes)
                s.acquire()
                print('El agente pone el papel y el tabaco')
                time.sleep(2)
        elif self.ingrediente == 1:
                self.ingredientes = ["papel", "cerillas"]
                print('El agente pone el papel y las cerillas')
                q.put(self.ingredientes)
                s.acquire()
                time.sleep(2)
        elif self.ingrediente == 2:
                self.ingredientes = ["tabaco", "cerillas"]
                q.put(self.ingredientes)
                s.acquire()
                print('El agente pone el tabaco y las cerillas')
                time.sleep(2)

    def run(self):
        while True:
            if q.empty():
                self.poner_ingredientes()
            else:
                 print("El agente recoge los ingredientes")
                 q.get()
                 s.release()
                 time.sleep(2)
                 

            

class Fumador(threading.Thread):
    def __init__(self, nombre, ingrediente, agente):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.ingrediente = ingrediente
        self.agente = agente

    def run(self):
        while True:
            if self.ingrediente not in self.agente.ingredientes:
                q.get()
                s.release()
                print(self.nombre + ' fuma')
                time.sleep(2)
                q.put(self.agente.ingredientes)
                s.acquire()
                
            else:
                pass


q = Queue(1)
s = threading.Semaphore(0)