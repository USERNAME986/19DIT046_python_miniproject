import turtle
import random

t = turtle
screen = turtle.getscreen()


def initialize(): 
    global word
    global l1
    l1=[]
    t.speed(0) 
    t.shapesize(1)
    
    t.setworldcoordinates(20,20,80,80)
    t.penup() 
    screen.tracer(1)
    t.pensize(9)
    t.color('blue')
    t.setpos(55,45)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(5)

    t.penup()
    t.setpos(35,30)
    t.left(90)
    for i in range(len(word)):
        screen.tracer(1)
        t.pendown()
        t.pensize(7)
        t.color('black') 
        t.forward(2)
        t.penup()
        t.forward(2)

def drawLetter(word,character): 
    global count
    
    times = [x for x, appearance in enumerate(word) if appearance == character] 
    for i in range(len(times)): 
        t.penup()
        screen.tracer(0)
        t.setpos(36 + 4*(times[i]),31)
        t.write(character, move=False, align='center', font=('Comic Sans', 20, 'normal'))
    count += len(times)
    l1.append(character)

def drawOver():
    screen.tracer(0)
    t.penup()
    t.setpos(50,70)
    t.color('white') 
    t.write('Type a new word!!!', move=False, align='center', font=('Comic Sans', 20, 'normal'))
    t.write('Type a new word!!!', move=False, align='center', font=('Comic Sans', 20, 'normal'))
    t.color('black')
    t.pendown()
    
def newWord():
    screen.tracer(0)
    t.penup()
    t.color('red')
    t.setpos(50,70)
    t.write('Type a new word!!!', move=False, align='center', font=('Comic Sans', 20, 'normal'))
    
def drawBody(): 
    global n
    t.setheading(270)
    t.penup()
    if n == 0: #draws head
        screen.tracer(1)
        t.setpos(45,60)
        t.speed(5)
        t.pensize(5)
        t.right(90)
        t.pendown()
        t.circle(3,360,30)
        t.penup()
    elif n == 1: #draws torso
        screen.tracer(1)
        t.setpos(45,54)
        t.pensize(5)
        t.pendown()
        t.forward(9)
        t.penup()
    elif n == 2: #draws left arm
        screen.tracer(1)
        t.setpos(45,51)
        t.speed(5)
        t.pensize(5)
        t.right(30)
        t.pendown()
        t.forward(3)
        t.left(13)
        t.forward(3)
        t.penup()
    elif n == 3: #draws right arm
        screen.tracer(1)
        t.setpos(45,51)
        t.pensize(5)
        t.left(30)
        t.pendown()
        t.forward(3)
        t.right(13)
        t.forward(3)
        t.penup()
    elif n == 4: #draws left leg
        screen.tracer(1)
        t.setpos(45,45)
        t.pensize(5)
        t.right(20)
        t.pendown()
        t.forward(3)
        t.left(8)
        t.forward(3)
        t.penup()
    elif n == 5: #draws right leg
        screen.tracer(1)
        t.setpos(45,45)
        t.pensize(5)
        t.left(30)
        t.pendown()
        t.forward(3)
        t.right(7)
        t.forward(3)
        t.penup()

def guess(): 
    global word
    global n
    character = t.textinput('Your Guess','What letter are you thinkin\'')
    
    if character in word: 
        if character in l1:
            newWord()   
        else:
            drawOver()
            drawLetter(word,character)
           
    else: 
        drawOver()
        drawBody()
        n += 1

def sub_main():
    global n
    global count
    global word
    n = 0
    count = 0
    initialize()
    done = False    
    while not done:
        if word == 'suger':
            t.penup()
            t.setpos(50,75)
            t.color('brown')
            t.write('it is something sweet and white'  + ' \'', align='center', font=('Comic Sans', 15, 'normal'))
        if word == 'plasma':
            t.penup()
            t.setpos(50,75)
            t.color('brown')
            t.write('it is a state which is critical state of matter'  + ' \'', align='center', font=('Comic Sans', 15, 'normal'))
        if word == 'television':
            t.penup()
            t.setpos(50,75)
            t.color('brown')
            t.write('it is an idiot box'  + ' \'', align='center', font=('Comic Sans', 15, 'normal'))
        if word == 'jenil':
            t.penup()
            t.setpos(50,75)
            t.color('brown')
            t.write('it is the one who is presenting this miniproject'  + ' \'', align='center', font=('Comic Sans', 15, 'normal'))   
        
        if n > 5:
            done = True
            t.penup()
            t.setpos(50,70)
            t.color('brown')
            t.write('You lose.' + 'The word was \'' + word + ' \'', move=False, align='center', font=('Comic Sans', 15, 'normal'))
        elif count > len(word) - 1:
            done = True
            t.penup()
            t.color('green')
            t.setpos(50,70)
            t.write('Amazing! You guessed the word!! \'' + word + '\'. You win!', move=False, align='center', font=('Comic Sans', 15, 'normal'))
        else:
            guess()
        
    return None

def main():
    finished = False
    while not finished:
        global word
        wordList = ['suger','plasma','television','jenil']
        word = wordList[random.randint(0,3)]
        sub_main()
        repeat = t.textinput('','Would you like to play again? (y/n): ')
        if repeat == 'y':
            t.reset()
        else:
            finished = True
    return None

main()
