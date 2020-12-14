import arcade
import os
from functions import *
from train import *
import threading

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
mutex4 = threading.Lock()
mutex5 = threading.Lock()


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        # xc, yc, colour, velocity, width_rail, height_rail, width_train, height_train
        self.train1 = train(65, 425, arcade.color.ELECTRIC_GREEN, 1, 105, 65, 10, 20)
        self.train2 = train(185, 482, arcade.color.PURPLE, 3, 105, 65, 20, 10)
        self.train3 = train(293, 482, arcade.color.RED, 2, 105, 65, 20, 10)
        self.train4 = train(75, 412, arcade.color.BLUE, 0.5, 325, 65, 20, 10)

        trem_verde = threading.Thread(target=self.trem_verde)
        trem_roxo = threading.Thread(target=self.trem_roxo)
        trem_vermelho = threading.Thread(target=self.trem_vermelho)
        trem_azul = threading.Thread(target=self.trem_azul)

        trem_verde.start()
        trem_roxo.start()
        trem_vermelho.start()
        trem_azul.start()

        self.velocidade1 = str(self.train1.velocity) + "Km/h"
        self.velocidade2 = str(self.train1.velocity) + "Km/h"
        self.velocidade3 = str(self.train1.velocity) + "Km/h"
        self.velocidade4 = str(self.train1.velocity) + "Km/h"

        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Visualizacao  da dinamica dos trens", 35, 550, arcade.color.BLACK, 20)
        arcade.draw_text("Painel de controle de velocidade", 35, 180, arcade.color.BLACK, 20)

        # desenhando os trens
        self.train1.drawTrain()
        self.train2.drawTrain()
        self.train3.drawTrain()
        self.train4.drawTrain()

        # TRILHO-RETANGULO
        drawRails()

        # VELOCIMETRO
        drawVelocityBoard(self.velocidade1, self.velocidade2, self.velocidade3, self.velocidade4)

    def trem_verde(self):
        while (True):
            while self.train1.yc < 485:
                self.train1.moveUp()
                self.train1.updateState("L1")
                time.sleep(0.02)

            while self.train1.xc < 170:
                self.train1.moveRight()
                self.train1.updateState("L2")
                time.sleep(0.02)

            mutex1.acquire()

            while self.train1.yc > 420:
                self.train1.moveDown()
                self.train1.updateState("L3")
                time.sleep(0.02)

            mutex2.acquire()
            mutex1.release()

            while self.train1.xc > 65:
                self.train1.moveLeft()
                self.train1.updateState("L4")
                time.sleep(0.02)

            mutex2.release()

            self.train1.xc = 65
            self.train1.yc = 425
            time.sleep(0.02)

    def trem_roxo(self):
        while (True):
            while self.train2.xc < 278:
                self.train2.moveRight()
                self.train2.updateState("L7")
                time.sleep(0.02)
            mutex4.acquire()

            while self.train2.yc > 420:
                self.train2.moveDown()
                self.train2.updateState("L5")
                time.sleep(0.02)

            mutex3.acquire()
            mutex4.release()

            while self.train2.xc > 170:
                self.train2.moveLeft()
                self.train2.updateState("L6")
                time.sleep(0.02)

            mutex1.acquire()
            mutex3.release()

            while self.train2.yc < 485:
                self.train2.moveUp()
                self.train2.updateState("L3")
                time.sleep(0.02)
            mutex1.release()

            self.train2.xc = 185
            self.train2.yc = 482
            time.sleep(0.02)

    def trem_vermelho(self):
        while (True):
            while self.train3.xc < 385:
                self.train3.moveRight()
                self.train3.updateState("L8")
                time.sleep(0.02)
            while self.train3.yc > 420:
                self.train3.moveDown()
                self.train3.updateState("L9")
                time.sleep(0.02)
            mutex5.acquire()
            while self.train3.xc > 280:
                self.train3.moveLeft()
                self.train3.updateState("L10")
                time.sleep(0.02)
            mutex5.release()
            mutex4.acquire()
            while self.train3.yc < 485:
                self.train3.moveUp()
                self.train3.updateState("L5")
                time.sleep(0.02)
            mutex4.release()

            self.train3.xc = 293
            self.train3.yc = 482
            time.sleep(0.02)

    def trem_azul(self):
        while (True):
            mutex3.acquire()
            mutex2.acquire()
            mutex5.acquire()
            while self.train4.xc < 178:
                self.train4.updateState("L4")
                self.train4.moveRight()
                time.sleep(0.02)
            mutex2.release()

            while self.train4.xc < 281:
                self.train4.moveRight()
                self.train4.updateState("L6")
                time.sleep(0.02)
            mutex3.release()
            while self.train4.xc < 385:
                self.train4.updateState("L10")
                self.train4.moveRight()
                time.sleep(0.02)
            mutex5.release()
            while self.train4.yc > 348:
                self.train4.moveDown()
                self.train4.updateState("L12")
                time.sleep(0.02)
            while self.train4.xc > 65:
                self.train4.moveLeft()
                self.train4.updateState("L13")
                time.sleep(0.02)
            while self.train4.yc < 415:
                self.train4.moveUp()
                self.train4.updateState("L11")
                time.sleep(0.02)
            self.train4.xc = 75
            self.train4.yc = 412
            time.sleep(0.02)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q and self.train1.velocity <= 5:
            self.train1.velocity = self.train1.velocity + 0.25
        elif key == arcade.key.A and self.train1.velocity >= 1:
            self.train1.velocity = self.train1.velocity - 0.25

        if key == arcade.key.W and self.train2.velocity <= 5:
            self.train2.velocity = self.train2.velocity + 0.25
        elif key == arcade.key.S and self.train2.velocity >= 1:
            self.train2.velocity = self.train2.velocity - 0.25

        if key == arcade.key.E and self.train3.velocity <= 5:
            self.train3.velocity = self.train3.velocity + 0.25
        elif key == arcade.key.D and self.train3.velocity >= 1:
            self.train3.velocity = self.train3.velocity - 0.25

        if key == arcade.key.R and self.train4.velocity <= 5:
            self.train4.velocity = self.train4.velocity + 0.25
        elif key == arcade.key.F and self.train4.velocity >= 1:
            self.train4.velocity = self.train4.velocity - 0.25

    def update(self, delta_time):
        self.velocidade1 = str(self.train1.velocity * 10) + "Km/h"
        self.velocidade2 = str(self.train2.velocity * 10) + "Km/h"
        self.velocidade3 = str(self.train3.velocity * 10) + "Km/h"
        self.velocidade4 = str(self.train4.velocity * 10) + "Km/h"


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


# arcade.finish_render()

if __name__ == "__main__":
    main()