import turtle
import random

ekran = turtle.Screen()
ekran.title("let's catch saddam")
ekran.bgcolor("lightgreen")
ekran.setup(width=800, height=500)


ekran.register_shape("saddam1.gif")
saddam=turtle.Turtle()
saddam.shape("saddam1.gif")
saddam.color("red")
saddam.penup()
saddam.speed(0)


def run_saddam_run():
    x = random.randint(-380,+350)
    y = random.randint(-250,+250)
    saddam.goto(x,y)
    ekran.ontimer(run_saddam_run,t=500)
run_saddam_run()

score=0
score_screen=turtle.Turtle()
score_screen.hideturtle()
score_screen.penup()
score_screen.goto(-300,+200)
score_screen.color("black")
score_screen.write("Score:0",font=("arial",16,"bold"))

def score_up():
    global score
    score+=1
    score_screen.clear()
    score_screen.write(f"score:{score}",font=("Arial",16,"bold"))
saddam.onclick(lambda x,y:score_up())

saniye = 60
timer_count = turtle.Turtle()
timer_count.hideturtle()
timer_count.penup()
timer_count.goto(200, 200)
timer_count.color("black")
timer_count.write("Time: 60", font=("Arial", 15, "bold"))

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
    saddam.hideturtle()
    sonuc = turtle.Turtle()
    sonuc.hideturtle()
    sonuc.penup()
    sonuc.goto(0, 0)
    sonuc.color("red")
    if score < 10:
        sonuc.write("Game Over! 9-11 going to happen!!!", align="center", font=("Arial", 30, "bold"))
    else:
        sonuc.write("You Win!", align="center", font=("Arial", 30, "bold"))

kronos_tut_zamani_babacim()


turtle.mainloop()