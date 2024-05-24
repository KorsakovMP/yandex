import random
import time
from turtle import *


def draw_row_of_sots():
    """Функция рисует линию сот"""
    for _ in range(3):
        right(60)
        for _ in range(9):
            color(random.choice(('blue', 'red', 'green')))
            forward(30)
            left(60)
        right(120)
        forward(30)

def draw_body():
    """Функция рисует тело черепахи"""
    for _ in range(2):
        forward(130)
        color(random.choice(('blue', 'red', 'green')))
        circle(radius=160, extent=60)
        color(random.choice(('blue', 'red', 'green')))
        circle(radius=80, extent=60)
        color(random.choice(('blue', 'red', 'green')))
        circle(radius=160, extent=60)

def draw_body_parent():
    """Функция рисует узор на черепахе"""
    for _ in range(3):
        draw_row_of_sots()
        left(60)
        forward(30)
        left(120)
        draw_row_of_sots()
        right(60)
        forward(30)
        right(120)

def draw_turtle():
    """Функция рисует черепаху"""
    draw_body()
    goto(-60, 50)
    draw_body_parent()

draw_turtle()
time.sleep(60)
