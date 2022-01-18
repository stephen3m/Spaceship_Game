import turtle, math, random
class SpaceCraft(turtle.Turtle):
    '''
    Purpose:
        An object of this class represents a spacecraft in our game
    Instance variables:
        x_cor: x coord of spacecraft
        y_cor: y coord of spacecraft
        vx: x velocity of spacecraft
        vy: y velocity of spacecraft
        fuel: fuel remaining for craft
    Methods:
        move: moves spacecraft to new position
        thrust: pressing the 'Up' arrow causes spacecraft to increase velocity in direction it's pointing, takes one fuel, prints remaining fuel
        left_turn: turns spacecraft left by 15 degrees, takes one fuel, prints remaining fuel
        right_turn: turns spacecraft right by 15 degrees, takes one fuel, prints remaining fuel
    '''
    def __init__(self, x_cor, y_cor, x_vel, y_vel):
        turtle.Turtle.__init__(self)
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.vx = x_vel
        self.vy = y_vel
        self.fuel = 50
        self.left(90)
        self.penup()
        self.speed(0)
        self.setpos(x_cor, y_cor)
    def move(self):
        self.vy -= 0.0486
        new_x_cor = self.xcor() + self.vx
        new_y_cor = self.ycor() + self.vy
        self.setpos(new_x_cor, new_y_cor)
    def thrust(self):
        if self.fuel > 0:
            self.fuel -= 1
            ship_ang = math.radians(self.heading())
            self.vx += math.cos(ship_ang)
            self.vy += math.sin(ship_ang)
            print(str(self.fuel) + ' fuel units remaining')
        else:
            print('Out of fuel')
    def left_turn(self):
        if self.fuel > 0:
            self.fuel -= 1
            self.left(15)
            print(str(self.fuel) + ' fuel units remaining')
        else:
            print('Out of fuel')
    def right_turn(self):
        if self.fuel > 0:
            self.fuel -= 1
            self.right(15)
            print(str(self.fuel) + ' fuel units remaining')
        else:
            print('Out of fuel')

class Meteor(turtle.Turtle):
    '''
    Purpose:
        Object of this class represents a meteor in spacecraft game
    Instance variables:
        x_cor: x coord of meteor
        y_cor: y coord of meteor
        vx: x velocity of meteor
        vy: y velocity of meteor
    Methods:
        move: makes the meteor move in a linear path and bounces off walls
    '''
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('yellow')
        self.speed(0)
        self.penup()
        self.x_cor = random.uniform(-900, 900)
        self.y_cor = random.uniform(30, 900)
        self.vx = random.uniform(3, 9)
        self.vy = random.uniform(3, 9)
        self.setpos(self.x_cor, self.y_cor)
        self.move()
    def move(self):
        newx = self.xcor() + self.vx
        newy = self.ycor() + self.vy
        if newx < 0:
            newx = 0
            self.vx *= -1
        if newx > 900:
            newx = 900
            self.vx *= -1
        if newy < 0:
            newy = 0
            self.vy *= -1
        if newy > 900:
            newy = 900
            self.vy *= -1
        self.setpos(newx, newy)
        turtle.ontimer(self.move, 30)

class Game:
    '''
    Purpose:
        Object of this class represents a spacecraft game: Allows user to play a game that simulates landing a spacecraft while avoiding asteroids
    Instance variables:
        player: spacecraft object
        meteor_ls: list containing the meteor objects
    Methods:
        gameloop: If y coord of spacecraft < 10, if x vel and y vel are both between -4 and 4, "Successful landing!" appears on screen, else "You crashed!" appears on screen
                  Else calls the move method in SpaceCraft and calls itself 30 milliseconds from now
        create_bg: creates background for game
    '''
    def __init__(self):
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        self.create_bg()
        turtle.delay(0)
        x_cor = random.uniform(100, 900)
        y_cor = random.uniform(500, 900)
        x_vel = random.uniform(-5, 5)
        y_vel = random.uniform(-5, 0)
        self.player = SpaceCraft(x_cor, y_cor, x_vel, y_vel)
        self.player.turtlesize(2)
        self.player.color('white')
        self.meteor_ls = []
        for i in range(10):
            a = Meteor()
            self.meteor_ls.append(a)
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_turn, 'Left')
        turtle.onkeypress(self.player.right_turn, 'Right')
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        collided = False
        for m in self.meteor_ls:
            if (abs(m.ycor() - self.player.ycor()) < 20) and (abs(m.xcor() - self.player.xcor()) < 20) and collided == False:
                turtle.hideturtle()
                turtle.penup()
                turtle.setpos(333, 500)
                turtle.pendown()
                turtle.pencolor('white')
                turtle.write('You crashed!', font=('Arial', 25, 'normal'))
                collided = True
        if 5 < self.player.ycor() < 10 or collided == True:
            if collided == True:
                turtle.hideturtle()
                turtle.penup()
                turtle.setpos(333, 500)
                turtle.pendown()
                turtle.pencolor('white')
                turtle.write('You crashed!', font=('Arial', 25, 'normal'))
            elif -4 < self.player.vx < 4 and -4 < self.player.vy < 4:
                turtle.hideturtle()
                turtle.penup()
                turtle.setpos(333, 500)
                turtle.pendown()
                turtle.pencolor('white')
                turtle.write('Successful landing!', font=('Arial', 25, 'normal'))
            else:
                turtle.hideturtle()
                turtle.penup()
                turtle.setpos(333, 500)
                turtle.pendown()
                turtle.pencolor('white')
                turtle.write('You crashed!', font=('Arial', 25, 'normal'))

        else:
            if self.player.xcor() < 0:
                self.player.setpos(1000, self.player.ycor())
                self.player.move()
                turtle.ontimer(self.gameloop, 30)
            elif self.player.xcor() > 1000:
                self.player.setpos(0, self.player.ycor())
                self.player.move()
                turtle.ontimer(self.gameloop, 30)
            else:
                self.player.move()
                turtle.ontimer(self.gameloop, 30)
    def create_bg(self):
        turtle.Screen().bgcolor('darkblue')
        star_cor = [100, 250, 400]
        star = turtle.Turtle()
        star.speed(0)
        for cor in star_cor:
            star.hideturtle()
            star.penup()
            star.setpos(cor, cor * 2.3)
            star.fillcolor('orange')
            star.begin_fill()
            for i in range(5):
                star.forward(75)
                star.right(144)
            star.end_fill()

        spiral = turtle.Turtle()
        spiral.hideturtle()
        spiral.pencolor('white')
        spiral.penup()
        spiral.speed(0)
        spiral.setpos(750, 250)
        spiral.pendown()

        for i in range(100):
            spiral.forward(5+i)
            spiral.right(15)

        circ = turtle.Turtle()
        circ.penup()
        circ.hideturtle()
        circ.speed(0)
        circ.setpos(850, 150)
        circ.pendown()
        circ.fillcolor('red')
        circ.begin_fill()
        circ.circle(50)
        circ.end_fill()
        circ.penup()
        circ.speed(0)
        circ.setpos(580, 325)
        circ.pendown()
        circ.fillcolor('orchid1')
        circ.begin_fill()
        circ.circle(25)
        circ.end_fill()
