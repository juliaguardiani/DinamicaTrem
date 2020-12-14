import threading  # threads
import time  # tempo (opcional)
import arcade
import os

TREM1 = arcade.color.ELECTRIC_GREEN
TREM2 = arcade.color.PURPLE
TREM3 = arcade.color.RED
TREM4 = arcade.color.BLUE


# define uma classe para a criacao de threads
class train:
    def __init__(self, xc, yc, colour, velocity, width_rail, height_rail, width_train, height_train):
        self.xc = xc
        self.yc = yc
        self.xc_aux = xc
        self.yc_aux = yc
        self.colour = colour
        self.velocity = velocity
        self.width_rail = width_rail
        self.height_rail = height_rail
        self.width_train = width_train
        self.height_train = height_train
        self.count_1 = 1
        self.count_2 = 1
        self.count_3 = 1
        self.count_4 = 1
        self.velocity_aux = velocity
        self.state = "L0"

    def drawTrain(self):
        arcade.draw_rectangle_filled(self.xc, self.yc, self.width_train, self.height_train, self.colour)

    def updateState(self, state):
        self.state = state

    def moveRight(self):
        self.xc = self.xc + self.velocity
        self.height_train = 10
        self.width_train = 20

    def moveDown(self):
        self.yc = self.yc - self.velocity
        self.height_train = 20
        self.width_train = 10

    def moveLeft(self):
        self.xc = self.xc - self.velocity
        self.height_train = 10
        self.width_train = 20

    def moveUp(self):
        self.yc = self.yc + self.velocity
        self.height_train = 20
        self.width_train = 10