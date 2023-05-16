import random
import threading
import time


class Agente(threading.Thread):

    def __init__(self, q, s):
        threading.Thread.__init__(self)
        self.ingredientes = None
        self.q = q
        self.s = s


    def poner_ingredientes(self):
        self.ingrediente = random.choice([0, 1, 2])
        if self.ingrediente == 0:
                self.ingredientes = ["papel", "tabaco"]
                self.q.put(self.ingredientes)
                self.s.acquire()
                print('El agente pone el papel y el tabaco')
                time.sleep(2)
        elif self.ingrediente == 1:
                self.ingredientes = ["papel", "cerillas"]
                print('El agente pone el papel y las cerillas')
                self.q.put(self.ingredientes)
                self.s.acquire()
                time.sleep(2)
        elif self.ingrediente == 2:
                self.ingredientes = ["tabaco", "cerillas"]
                self.q.put(self.ingredientes)
                self.s.acquire()
                print('El agente pone el tabaco y las cerillas')
                time.sleep(2)

    def run(self):
        while True:
            if self.q.empty():
                self.poner_ingredientes()
            else:
                 print("El agente recoge los ingredientes")
                 self.q.get()
                 self.s.release()
                 time.sleep(2)
                 

            

class Fumador(threading.Thread):
    def __init__(self, nombre, ingrediente, agente, q, s):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.ingrediente = ingrediente
        self.agente = agente


    def run(self):
        while True:
            if self.ingrediente not in self.agente.ingredientes:
                self.q.get()
                self.s.release()
                print(self.nombre + ' fuma')
                time.sleep(2)
                self.q.put(self.agente.ingredientes)
                self.s.acquire()
                
            else:
                pass
