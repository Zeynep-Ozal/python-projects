import tkinter as tk
import random


SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
global score
score =0



class Snake:
    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinate = []
        self.squares = []

        for i in range (0,3):
            self.coordinate.append([0,0])

        for x,y in self.coordinate:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill = 'green', tag ="snake")
            self.squares.append(square)


class Food:

   def __init__(self):

        a = random.randint(0,  13)*50
        b = random.randint(0, 13)*50
        self.coordinate = [a, b]
        canvas.create_oval(a, b, a+50, b+50, fill="red",tag = "food")

def change_directoin(new_direction):

    global direction

    if new_direction == "up":
        if direction!= "down":
            direction = "up"
    elif new_direction == "down":
        if direction!= "up":
            direction = "down"
    elif new_direction == "left":
        if direction!= "right":
            direction = "left"
    elif new_direction == "right":
        if direction!= "left":
            direction = "right"

def next_move(snake,food):

    x,y = snake.coordinate[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinate.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x+50, y+50, fill = "green")
    snake.squares.insert(0, square)


    if x==food.coordinate[0]and y==food.coordinate[1]:

        global score

        score+= 1

        del food.coordinate[1]
        canvas.delete("food")

        label.config(text = "score : {}".format(score))

        food = Food()

    else:
        del snake.coordinate[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if x>=14*50 or x<0:

        canvas.delete("all")
        del snake.coordinate[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

        canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text="    GAME OVER\nYOUR SCORE IS {}".format(score), font=200, fill="red")

    elif y>=14*50 or y<0:

        canvas.delete("all")
        del snake.coordinate[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text="    GAME OVER \nYOUR SCORE IS {}".format(score), font = 200, fill = "red")

    root.after(SPEED,next_move,snake, food)


def start_button():

    start_label. destroy()
    button.destroy()
    global label
    label = tk.Label(root, text="score : {}".format(score))
    label.pack()

    global canvas
    canvas = tk.Canvas(root, bg="black", height=700, width=700)
    canvas.pack()

    food = Food()
    snake = Snake()

    next_move(snake, food)



root = tk.Tk()

#root
root.title("snake game")
root.resizable(False,False)
root.geometry("700x750")

global direction

direction = 'down'

start_label = tk.Label(root,text = "SNAKE GAME")
start_label.place(width = 700,y =700)
start_label.pack()
button = tk.Button(root, text = "start game", command= start_button)
button.pack()



root.bind('<Left>', lambda event:change_directoin("left"))
root.bind('<Right>', lambda event :change_directoin('right'))
root.bind('<Up>', lambda event:change_directoin('up'))
root.bind('<Down>', lambda event:change_directoin('down'))

root.mainloop()

