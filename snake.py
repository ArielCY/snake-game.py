from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)] # tuple, in python, constants are named with caps
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: # first letter of class name should be capitalized

    def __init__(self): # initialize a new snake object
        self.segments = [] # segments is attribute relative to snake class
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self): # a method relative to snake class # Create Snake
        for position in START_POSITION:
            self.add_segment(position)
            # new_segment = Turtle("square")  # turtle is created at center(0,0)
            # new_segment.color("white")
            # new_segment.penup()  # no line is draw, we can only see turtle piece
            # new_segment.goto(position)  # turtle move to certain position
            # self.segments.append(new_segment)

    # create a snake by create 3 segment from turtle
    # # origin (0, 0)
    # segment_1 = Turtle("square")
    # segment_1.color("white")

    # # (-20, 0)
    # segment_2 = Turtle("square")
    # segment_2.color("white")
    # segment_2.goto(-20, 0)

    # # (-40, 0)
    # segment_3 = Turtle("square")
    # segment_3.color("white")
    # segment_3.goto(-40, 0)

    def add_segment(self, position):
        new_segment = Turtle("square")  # turtle is created at center(0,0)
        new_segment.color("white")
        new_segment.penup()  # no line is draw, we can only see turtle piece
        new_segment.goto(position)  # turtle move to certain position
        self.segments.append(new_segment)

    # create a snake by create 3 segment from turtle
    # # origin (0, 0)
    # segment_1 = Turtle("square")
    # segment_1.color("white")

    # # (-20, 0)
    # segment_2 = Turtle("square")
    # segment_2.color("white")
    # segment_2.goto(-20, 0)

    # # (-40, 0)
    # segment_3 = Turtle("square")
    # segment_3.color("white")
    # segment_3.goto(-40, 0)

    def extend(self):  # add new segment to snake
        self.add_segment(self.segments[-1].position()) # adding segment to the last one

    def move(self): # another method associated with snake class
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE) #self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)# self.segments[0].setheading(90) head is used frequently

    def down(self):
        # pass is used to do testing for only one turn, eg: up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        # send snake to place we can't see while we still have access to snake
        for seg in self.segments:
            self.segments.goto(1000,1000) # dead snake will disappear off the screen
        self.segments.clear() # remove all item from the list
        self.create_snake()
        self.head = self.segments[0]
