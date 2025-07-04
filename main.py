import turtle
import random

ekran = turtle.Screen()
ekran.title("let's catch saddam")
ekran.bgcolor("lightgreen")
ekran.setup(width=800, height=500)

ekran.register_shape("saddam1.gif")
saddam = turtle.Turtle()
saddam.shape("saddam1.gif")
saddam.color("red")
saddam.penup()
saddam.speed(0)

oyun_aktif = True

def run_saddam_run():
    global oyun_aktif
    if oyun_aktif:
        x = random.randint(-380, 350)
        y = random.randint(-250, 250)
        saddam.goto(x, y)
        ekran.ontimer(run_saddam_run, t=500)

score = 0
score_screen = turtle.Turtle()
score_screen.hideturtle()
score_screen.penup()
score_screen.goto(-300, 200)
score_screen.color("black")
score_screen.write("Score: 0", font=("Arial", 16, "bold"))

def score_up():
    global score
    score += 1
    score_screen.clear()
    score_screen.write(f"Score: {score}", font=("Arial", 16, "bold"))

saddam.onclick(lambda x, y: score_up())

saniye = 60
timer_count = turtle.Turtle()
timer_count.hideturtle()
timer_count.penup()
timer_count.goto(200, 200)
timer_count.color("black")
timer_count.write("Time: 60", font=("Arial", 15, "bold"))

restart_button = turtle.Turtle()
restart_button.hideturtle()
restart_button.penup()
restart_button.goto(0, -300)
restart_button.shape("triangle")
restart_button.shapesize(stretch_len=6, stretch_wid=2)
restart_button.fillcolor("black")
restart_button.hideturtle()

restart_text = turtle.Turtle()
restart_text.hideturtle()
restart_text.penup()
restart_text.color("purple")

sonuc = turtle.Turtle()
sonuc.hideturtle()
sonuc.penup()
sonuc.goto(0, 0)
sonuc.color("red")

def kronos_tut_zamani_babacim():
    global saniye
    if saniye > 0:
        saniye -= 1
        timer_count.clear()
        timer_count.write(f"Time: {saniye}", font=("Arial", 15, "bold"))
        ekran.ontimer(kronos_tut_zamani_babacim, 1000)
    else:
        bitis_ekrani()

def bitis_ekrani():
    global oyun_aktif
    oyun_aktif = False
    saddam.hideturtle()
    sonuc.clear()

    if score < 10:
        sonuc.write("Game Over! 9-11 going to happen!!!", align="center", font=("Arial", 30, "bold"))
    else:
        sonuc.write("You Win!", align="center", font=("Arial", 30, "bold"))

    restart_text.goto(0, -200)
    restart_text.write("Try again?", align="center", font=("Arial", 20, "bold"))

    restart_button.goto(0, -220)
    restart_button.showturtle()
    restart_button.onclick(restart_game)

def restart_game(x, y):
    global score, saniye, oyun_aktif
    oyun_aktif = True
    score = 0
    saniye = 60

    score_screen.clear()
    score_screen.write(f"Score: {score}", font=("Arial", 16, "bold"))

    timer_count.clear()
    timer_count.write("Time: 60", font=("Arial", 15, "bold"))

    saddam.showturtle()
    sonuc.clear()
    restart_text.clear()
    restart_button.hideturtle()

    run_saddam_run()
    kronos_tut_zamani_babacim()

run_saddam_run()
kronos_tut_zamani_babacim()

turtle.mainloop()
