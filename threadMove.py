import  threading
from threading import Lock
from functions import *

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3=threading.Lock()
mutex4=threading.Lock()

# define uma classe para a criacao de threads
class threadMoveTrain():
    def __init__(self):
        self.t_v = threading.Thread(target=self.trem_verde)
        self.t_r = threading.Thread(target=self.trem_roxo)
        self.t_a = threading.Thread(target= self.trem_vermelho)
        self.t_z = threading.Thread(target=self.trem_azul)

        self.t_v.start()
        self.t_r.start()
        self.t_a.start()
        self.t_z.start()

    def trem_verde(self):
        self.L1()
        self.L2()
        self.L3()

    def L1(self):
        drawlinha1()
    def L2(self):
        drawlinha2()

