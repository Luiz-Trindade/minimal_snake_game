from os import system as S
from random import randint as R
import keyboard
from time import sleep

table = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]

sx = 0
sy = 0

fx = R(0, 8)
fy = R(0, 8)

direction = "RIGHT"

score = 0
speed = 0.5

def update():
    try: S("clear")
    except: S("cls")
    for i in range(len(table)):
        for j in range(len(table)):
            table[i][j] = " "
def view():
    for i in table:
        print("".join(i))
    print(f"[SCORE: {score}]")
    print("----------------------------------------------")
    print("|Simple Snake Game.                          |")
    print("|Created By: Luiz Gabriel Magalhães Trindade.|")
    print("|Distributed Under The GPL3 Lincense.        |")
    print("----------------------------------------------")

def snake():
    global sx, sy, direction
    if direction == "UP":
        sy -= 1
    elif direction == "DOWN":
        sy += 1
    elif direction == "LEFT":
        sx -= 1
    elif direction == "RIGHT":
        sx += 1
    table[sy][sx] = "🐍"

def food():
    global fx, fy
    table[fy][fx] = "🍎"

def verify_position():
    global sx, sy, fx, fy, direction, score, speed
    if fx == sx and fy == sy:
        score += 1
        speed -= 0.01
        fx = R(0, 8)
        fy = R(0, 8)
    elif sx < 0:
        sx = 9
    elif sy < 0:
        sy = 9
    elif sx > 9:
        #sx = 0
        exit()
    elif sy > 9:
        #sy = 0
        exit()
    else: pass

def controls(e):
    global sx, sy, direction
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "w":
            direction = "UP"
        elif e.name == "s":
            direction = "DOWN"
        elif e.name == "a":
            direction = "LEFT"
        elif e.name == "d":
            direction = "RIGHT"

keyboard.on_press_key("w", controls)
keyboard.on_press_key("s", controls)
keyboard.on_press_key("a", controls)
keyboard.on_press_key("d", controls)

while True:
    update()
    snake()
    food()
    view()
    verify_position()
    sleep(speed)
