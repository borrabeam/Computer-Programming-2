import tkinter as tk
import tkinter.ttk as ttk
from turtle import RawTurtle
from tkinter import messagebox
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500


class Turtle(RawTurtle):

    def __init__(self, canvas, speed=3):
        super().__init__(canvas)
        self.screen.setworldcoordinates(0, CANVAS_HEIGHT - 1, CANVAS_WIDTH - 1, 0)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(10, CANVAS_HEIGHT / 2)
        self.speed = speed
        self.waypoint = None
        self.screen.tracer(False)  # disable turtle's built-in animation

    def animate(self):
        if self.waypoint is not None:
            x, y = self.waypoint
            if self.distance(x, y) >= self.speed:
                self.setheading(self.towards(x, y))
                self.forward(self.speed)
        self.screen.update()

    def set_waypoint(self, x, y):
        self.waypoint = (x, y)


class Home:
    def __init__(self, canvas, size, pos):
        self.canvas = canvas
        self.size = size
        self.pos = pos
        x, y = pos
        self._id = canvas.create_rectangle(
            x - size / 2, y - size / 2, x + size / 2, y + size / 2,
            outline="red", width=3)

    def contains_turtle(self, turtle):
        x, y = self.pos
        size = self.size
        x1, x2 = x - size / 2, x + size / 2
        y1, y2 = y - size / 2, y + size / 2
        tx, ty = turtle.pos()
        return x1 <= tx <= x2 and y1 <= ty <= y2


class BasicEnemy:

    def __init__(self, canvas, size=30, pos=(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)):
        self.canvas = canvas
        self.size = size
        self._id = canvas.create_oval(0, 0, size, size)
        self.pos = pos
        self.set_color("yellow")
        self.render()

    def set_color(self, color):
        self.canvas.itemconfigure(self._id, fill=color)

    def render(self):
        x, y = self.pos
        self.canvas.moveto(self._id, x - self.size / 2, y - self.size / 2)

    def animate(self):
        pass

    def hits_turtle(self, turtle):
        x, y = self.pos
        return turtle.distance(x, y) < self.size / 2


class MovingEnemy(BasicEnemy):

    def __init__(self, canvas, size=30, speed=2):
        super().__init__(canvas, size=size)
        self.speed = speed
        self.set_color("orange")
        self._coro = self.script()

    def move(self, x, y):
        self.pos = (x, y)

    def animate(self):
        if self._coro is None:
            return
        try:
            next(self._coro)
            self.render()
        except StopIteration:
            self._coro = None

    def script(self):
        while True:
            x, y = self.pos
            newx = x + random.randint(-self.speed, self.speed)
            newy = y + random.randint(-self.speed, self.speed)
            newx = min(max(newx, 0), CANVAS_WIDTH)
            newy = min(max(newy, 0), CANVAS_HEIGHT)
            self.move(newx, newy)
            yield


class FencingEnemy(MovingEnemy):

    def __init__(self, canvas, size=30, speed=2, fence=(50, 50, 100, 100)):
        super().__init__(canvas, size=size, speed=speed)
        self.fence = fence
        self.set_color("red")

    def script(self):
        x1, y1, x2, y2 = self.fence
        while True:
            for x in range(x1, x2, self.speed):
                self.move(x, y1)
                yield
            for y in range(y1, y2, self.speed):
                self.move(x2, y)
                yield
            for x in range(x2, x1, -self.speed):
                self.move(x, y2)
                yield
            for y in range(y2, y1, -self.speed):
                self.move(x1, y)
                yield
    # Add your code so that the enemy moves in a rectangular pattern
    # whose top-left corner is (x1,y1) and bottom-right corner is (x2,y2).
    # The enemy must also move at the speed defined by the 'speed' attribute.


class ScatterEnemy(MovingEnemy):

    def __init__(self, canvas, size=50, pos=(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2),speed=4):
        super().__init__(canvas,size,speed)
        self.pos = pos
        self.set_color("black")
        self.script(turtle)

    def script(self,turtle):
        while True:
            if self.explode():
                self.canvas.delete(self._id)

    def explode(self,turtle):
        x, y = self.pos
        if turtle.distance(x, y) < 50:
            return True


class TurtleAdventure(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.create_widgets()
        self.turtle = Turtle(self.canvas)
        self.canvas.bind("<Button-1>", lambda e: self.turtle.set_waypoint(e.x, e.y))
        self.is_animating = False
        self.home = Home(self.canvas, size=30, pos=(CANVAS_WIDTH - 100, CANVAS_HEIGHT / 2))
        self.enemies = [
            BasicEnemy(self.canvas, size=50, pos=(300, 200)),
            BasicEnemy(self.canvas, size=30, pos=(600, 300)),
            MovingEnemy(self.canvas, size=30),
            MovingEnemy(self.canvas, size=20, speed=5),
            FencingEnemy(self.canvas, size=20, speed=5, fence=(200, 100, 500, 300)),
            FencingEnemy(self.canvas, size=20, fence=(
            CANVAS_WIDTH - 150, CANVAS_HEIGHT // 2 - 50, CANVAS_WIDTH - 50, CANVAS_HEIGHT // 2 + 50)),
            ScatterEnemy(self.canvas, size=50, pos=(300,600))
        ]

    def toggle_animation(self):
        self.is_animating = not self.is_animating
        if self.is_animating:
            self.btn_start_top.config(text="Stop")
            self.animate()
        else:
            self.btn_start_top.config(text="Start")

    def animate(self):
        self.turtle.animate()
        if self.is_animating:  # schedule the next update
            timer = self.after(33, self.animate)
        if self.home.contains_turtle(self.turtle):
            self.after_cancel(timer)
            messagebox.showinfo(title="Turtle Game",
                                message="Turtle is home!  You win.")
            root.destroy()
            return
        for enemy in self.enemies:
            enemy.animate()
            if enemy.hits_turtle(self.turtle):
                self.after_cancel(timer)
                messagebox.showinfo(title="Turtle Game",
                                    message="Turtle is dead!  You lose.")
                root.destroy()
                return

    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
                                width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2,
                         sticky="news", padx=10, pady=10)
        self.btn_start_top = ttk.Button(self, text="Start",
                                        command=self.toggle_animation)
        self.btn_start_top.grid(row=1, column=0, pady=10)
        ttk.Button(self, text="Quit", command=root.destroy).grid(
            row=1, column=1, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Turtle's Adventure")

    # do not allow window resizing
    root.resizable(False, False)
    app = TurtleAdventure(root)
    root.mainloop()
