from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_main = []
        self.create_snake()
        self.head = self.snake_main[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_snake_body(position)

    def add_snake_body(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_main.append(snake)

    def extend_snake(self):
       self.add_snake_body(self.snake_main[-1].position())


    def move(self):
        for body in range(len(self.snake_main) - 1, 0, -1):
            x_body = self.snake_main[body - 1].xcor()
            y_body = self.snake_main[body - 1].ycor()
            self.snake_main[body].goto(x_body, y_body)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading()!= RIGHT:
         self.head.setheading(LEFT)

    def reset(self):
       for body in self.snake_main:
          body.goto(1000, 1000)
       self.snake_main.clear()
       self.create_snake()
       self.head = self.snake_main[0]

