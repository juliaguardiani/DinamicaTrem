import arcade
import os


def drawRails():
    # TRILHO-RETANGULO
    arcade.draw_rectangle_outline(115, 450, 105, 65, arcade.color.ELECTRIC_GREEN)
    arcade.draw_rectangle_outline(225, 450, 105, 65, arcade.color.PURPLE)
    arcade.draw_rectangle_outline(335, 450, 105, 65, arcade.color.RED)
    arcade.draw_rectangle_outline(225, 380, 325, 65, arcade.color.BLUE)


def drawVelocityBoard(velocidade1, velocidade2, velocidade3, velocidade4):
    arcade.draw_text("Q: Acelera", 50, 70, arcade.color.ELECTRIC_GREEN, 10)
    arcade.draw_text("A: Desacelera", 50, 50, arcade.color.ELECTRIC_GREEN, 10)

    arcade.draw_text("W: Acelera", 180, 70, arcade.color.PURPLE, 10)
    arcade.draw_text("S: Desacelera", 180, 50, arcade.color.PURPLE, 10)

    arcade.draw_text("E: Acelera", 310, 70, arcade.color.RED, 10)
    arcade.draw_text("D: Desacelera", 310, 50, arcade.color.RED, 10)

    arcade.draw_text("R: Acelera", 440, 70, arcade.color.BLUE, 10)
    arcade.draw_text("F: Desacelera", 440, 50, arcade.color.BLUE, 10)

    arcade.draw_text(velocidade1, 50, 120, arcade.color.ELECTRIC_GREEN, 20)
    arcade.draw_text(velocidade2, 180, 120, arcade.color.PURPLE, 20)
    arcade.draw_text(velocidade3, 310, 120, arcade.color.RED, 20)
    arcade.draw_text(velocidade4, 440, 120, arcade.color.BLUE, 20)




