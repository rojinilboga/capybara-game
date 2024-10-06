#importing the libraries
import pgzrun
from random import randint

TITLE = "CAPYBARA SHOT GAME!!!"
WIDTH = 600
HEIGHT = 600

#creating the capybara
capybara =Actor("capybara")

msg = ""

def draw():
    screen.clear()
    screen.fill(color =("#D6CA98") )

    capybara.draw()

pgzrun.go()