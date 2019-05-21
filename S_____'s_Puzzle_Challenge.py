import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import random
random.seed()

print "Welcome to S_____'s Puzzle Challenge!"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
raw_input("Press enter to advance through text.")
cls()
print "You are a regular kid who loves video games and dislikes doing any real work."
raw_input("")
print "Unfortunately, you really want to buy a game you heard about at school but you recently spent all your money on a hat you didn't really want anyways."
raw_input("")
print "Looks like you'll mope around like you usually do."
raw_input("")
cls()
print "But it seems like today is your lucky day and you find a 5 dollar bill stuck under a stack of 23 bricks."
raw_input("")
print "You call a friend over to help with the bricks and make a deal."

def reset():
    global x
    x = 23
    print "You each take turns taking 1 to 3 bricks, starting with you."
    print "Whoever takes the last brick wins and gets to keep the 5 dollar bill."

raw_input("")
def bricks():
    global x
    print ""
    print "There are",x,"remaining bricks." 
    s = raw_input("How many bricks will you take? ")
    print ""
    truth = 1
    try:
        int(s)
    except ValueError:
        truth = 0
    if truth != 0:
        s = int(s)
        if (s == 1 or s == 2 or s == 3) and s<=x:
            print "You take",s,"brick(s)." 
            x = x-s
            print "There are/is",x,"remaining brick(s)."
            print ""
            if x <= 0:
                print "You win! You take the 5 dollar bill aand put it in your pocket. Press Enter to continue."
                raw_input("")
            else:
                if x%4 == 0:
                    j = random.randint(1,3)
                else:
                    j = x%4
                print "Your friend takes",j,"brick(s)."
                x = x-j
                print "There are/is",x,"remaining brick(s)."
                print ""
                if x == 0:
                    print "You lose. Press Enter to retry."
                    raw_input("")
                    cls()
                    reset()
                    bricks()
                else:
                    bricks()
        else:
            print "Please choose a valid number."
            raw_input("")
            bricks()
    else:
        print "Please choose a valid number."
        raw_input("")
        bricks()
reset()
bricks()
cls()

print "Even after finding $5, you are still need 10 more dollars to buy the video game."
raw_input("")
print "After walking around looking for more easy money, you see a large group gathered around some sort of stand."
raw_input("")
print "Upon closer examination, it looks like people are gambling money on some sort of game involving bricks."
raw_input("")
print "You decide that this would be an easy way to earn 5 more dollars so you give the host your $5 and ask about the rules."
raw_input("")
cls()
print "The game starts with 512 bricks placed on top of the money."

def reset2():
    global y
    y = 512
    print "You each take turns taking either half of the bricks, rounded up, or just one brick. Starting with your opponent, of course."
    print "Not so easy anymore now is it?"
    print "Whoever takes the last brick wins and gets to keep the money."

raw_input("")
def check(i):
    global n
    n = 0
    m = i
    while m%2 == 0:
        m = m/2
        n = n+1
def bricks2():
    global y
    global n
    print ""
    print "There are",y,"remaining bricks."
    check(y)
    if y==1:
        k = 1
    elif n%2 == 0:
        if y%2 == 0:
            k = y/2
        else:
            check(y-1)
            if n%2 != 0:
                k = 1
            else:
                k = (y+1)/2
    else:
        l = random.randint(0,1)
        if l == 0:
            if y%2==0:
                k = y/2
            else:
                k = (y+1)/2
        else:
            k = 1
    print "Your opponent takes",k,"bricks." 
    y = y-k
    print "There are/is",y,"remaining brick(s)."
    print ""
    if y == 0:
        print "You Lose. Press Enter to retry."
        raw_input("")
        cls()
        reset2()
        bricks2()
    else:
        s = raw_input("How many bricks will you take (h for half. o for one)? ").lower()
        print ""
        if s == "h":
            if y%2==0:
                k = y/2
            else:
                k = (y+1)/2
            print "You take",k,"brick(s)." 
            y = y-k
            print "There are/is",y,"remaining brick(s)."
            print ""
            if y != 0:
                bricks2()
        elif s == "o":
            k = 1
            print "You take one brick." 
            y = y-k
            print "There are/is",y,"remaining brick(s)."
            print ""
            if y != 0:
                bricks2()
        else:
            print "For choosing an invalid option everybody else calls you a cheater and you lose. Press Enter to retry."
            raw_input("")
            cls()
            reset2()
            bricks2()       
reset2()
bricks2()
print "You win! Press Enter to continue."
raw_input("")
cls()

print "As you reach out to claim your prize, the host takes the money and runs! You've been swindled!"
raw_input("")
print "With no options left you decide to turn to government funding."
print "You're sure that if you can win the favor of the absolute monarch that rules over your country,"
print "the mad king would gladly give you money for a video game."
raw_input("")
print "Out of boredom the king agrees to give you the money as long as you can survive his challenge..."
def boxes():
    cls()
    print "The king presents two boxes to you, one with 10 bottles of grape drink and another with 10 bottles of poison."
    print "You may put however many bottles of either drink in any box, with the condition that each box has at least one drink."
    print ""
    print "The king then selects a box at random and then a bottle at random, and you must drink from that bottle."
    print ""
    a = raw_input("How many bottles of grape drink will you put in the first box? ")
    b = raw_input("How many bottles of poison will you put in the first box? ")
    print "You put the rest in the other box."
    print ""
    truth2 = 1
    try:
        int(a)
    except ValueError:
        truth2 = 0
    try:
        int(b)
    except ValueError:
        truth2 = 0
    if truth2 != 0:
        a = int(a)
        b = int(b)
        if a >=0 and b >=0 and a+b> 0 and a <=10 and b <=10:
            if (int(a) == 1 and int(b) == 0) or (int(a) == 9 and int(b) == 10):
                print "The king laughs maniacally and says 'Fortune favors those who help themselves!'"
                print "He hands you a bottle of grape drink. You drink from it and feel very sleepy."
                raw_input("")
            else:
                print "The king laughs sadistically and says 'Fortune does not favor those who refuse to help themselves!'"
                print "He hands you a bottle of poison. You drink from it and lose consciousness immediately"
                raw_input("")
        else:
            print "Please choose valid numbers."
            raw_input("")
            boxes()
    else:
        print "Please choose valid numbers."
        raw_input("")
        boxes()
    
boxes()
cls()

print "You wake up on what appears to be a tropical island."
raw_input("")
print "After waiting around on island for a few days, you finally spot a ship."
raw_input("")
print "It's a pirate ship, but you are so desperate to get back home that you're willing to join the crew."
raw_input("")
print "The captain doesn't seem to find any use for you but makes a bet with you anyways."
def setpirate():
    cls()
    global c
    c = random.randint(1,1000)
    global g
    g = 10
    print "If you can guess the captain's favourite number between 1 and 1000 in at most 10 guesses he'll let you become the new captain!"
def pirate():
    global g
    global c
    truth3 = 1
    print ""
    guess = raw_input("What's your guess? ")
    try:
        int(guess)
    except ValueError:
        truth3 = 0
    if truth3 !=0:
        guess = int(guess)
        if guess <=1000 and guess >= 1:
            if guess > c:
                g = g-1
                if g > 0:
                    print "Your guess is too high."
                    print g,"guesses remaining."
                    print ""
                    pirate()
                else:
                    print "You lose. Press Enter to try again."
                    raw_input("")
                    setpirate()
                    pirate()
            elif guess < c:
                g = g-1
                if g > 0:
                    print "Your guess is too low."
                    print g,"guesses remaining."
                    print("")
                    pirate()
                else:
                    print "You run out of guesses. You lose. Press Enter to try again"
                    raw_input("")
                    setpirate()
                    pirate()
            else:
                print "Good guess, you win! Press Enter to continue."
                raw_input("")
        else:
            print "Please choose a valid number."
            raw_input("")
            pirate()
    else:
        print "Please choose a valid number."
        raw_input("")
        pirate()
        
setpirate()
pirate()
cls()

print "You become the captain of the pirates and sail the seas."
raw_input("")
print "One day, you come across a treasure chest with 100 gold coins."
print "Your crew of four other pirates tasks you with dividing the treasure amongst the crew."
raw_input("")

def division():
    cls()
    r = 100
    w = 0
    print "Pirates have an interesting system for dividing gold."
    print ""
    print "The first in command divides the gold however he wishes. Then a vote is held between all the pirates (the captain votes for himself, obviously)."
    print "If the majority disagree with the distribution, then the first in command is thrown overboard and everyone else moves up the command chain."
    print ""
    print "Pirates are as such: they are very greedy, but also very bloodthirsty, with only their greed surpassing their desire to kill."
    print ""
    print "What a nice crew."
    print ""
    a = raw_input("How many coins will you give yourself? ")
    b = raw_input("How many coins will you give second in command? ")
    c = raw_input("How many coins will you give third in command? ")
    d = raw_input("How many coins will you give fourth in command? ")
    e = raw_input("How many coins will you give fifth in command? ")
    truth4 = 1
    try:
        int(a)
    except ValueError:
        truth4 = 0
    try:
        int(b)
    except ValueError:
        truth4 = 0
    try:
        int(c)
    except ValueError:
        truth4 = 0
    try:
        int(d)
    except ValueError:
        truth4 = 0
    try:
        int(e)
    except ValueError:
        truth4 = 0
    if truth4 != 0:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        if a+b+c+d+e == 100 and a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0:
            if b >= 99:
                w = w+1
            if c >= 1:
                w = w+1
            if d >= 2:
                w = w+1
            if e >= 1:
                w = w+1
            if w > 1:
                if a == 98:
                    print "Wow you found the best solution! How did you figure it out?"
                    print "You keep 98 gold coins! Press Enter to continue."
                    raw_input("")
                else:
                    print "You gather enough votes for your distribution to be accepted!"
                    print "You keep",a,"gold coin(s)! Press Enter to continue."
                    raw_input("")
            else:
                print "The pirates vote against you and you are thrown overboard. Press Enter to retry."
                raw_input("")
                division()
        else:
            print "Please enter valid numbers that add to 100."
            raw_input("")
            division()
    else:
        print "Please enter valid values that add to 100."
        raw_input("")
        division()
division()
cls()

print "Upon returning to your home country, you realize that the exchange rate on gold coins is horrible."
print "Looks like you will need to get a job to earn the $15 anyways."
raw_input("")

print "You find a job offering for census taking."
print "In order to get the job you'll need to at least two out of three questions correctly."
raw_input("")

def setqcount():
    global q
    global f
    q = 0
    f = random.randint(0,90)
def seteggs():
    global e
    global tries
    tries = 13
    e = 2
def q1():
    global q
    cls()
    print "The first question is this:"
    answer = raw_input("Using the numbers 3, 3, 7 and 7 is it possible with the basic operations (+, -, *, /) to create 24?(y/n) ").lower()
    if answer == "y":
        q = q+1
        print "You are correct! Press Enter to continue."
        raw_input("")
    elif answer == "n":
        print "You are incorrect. Press Enter to continue."
        raw_input("")
    else:
        print "Please enter a valid response"
        raw_input("")
        q1()
def q2():
    global q
    cls()
    print "Here is the second question:"
    print "Players A and B each bet one marble at a time on a fair coin flip. The winner of the flip keeps both marbles. They play until one player runs out of marbles."
    answer = raw_input("If A starts with 13 marbles and B starts with 7 marbles, what is the probability (in percent) that A will eventually take all of B's marbles? ")
    if answer == "65" or answer == "65%":
        print "That is correct. Press Enter to continue."
        q = q+1
        raw_input("")
    elif q == 1:
        print "That is incorrect. Press Enter to continue."
        raw_input("")
    else:
        print "That is incorrect. Press Enter to retry."
        raw_input("")
        q2()

def m():
    cls()
    global q
    if q == 2:
        print "Congratulations! You got the job! Press Enter to continue."
        raw_input("")
    else:
        print "In this next challenge you start with 2 eggs and a 90 floor building."
        print "You drop eggs from the floors of the buildings until you find the highest floor at which an egg can be dropped without breaking."
        print "you have at most 13 drops."
    q3()
def q3():
    global q
    global f
    global e
    global tries
    truth5 = 1
    truth6 = 1
    if tries == 0 or e == 0:
        print ""
        r = raw_input("Which floor is the maximum safe dropping floor? ")
        try:
            int(r)
        except ValueError:
            truth6 = 0
        if truth6!=0:
            r = int(r)
            if r == f:
                print "Correct! You got the job! Press Enter to continue."
                raw_input("")
            else:
                print "Incorrect. Press Enter to retry."
                seteggs()
                setqcount()
                raw_input("")
                m()
                q3()
        else:
            print "Please choose a valid number."
            raw_input("")
            q3()
    else:
        print ""
        d = raw_input("From which floor do you drop the egg? ")
        try:
            int(d)
        except ValueError:
            truth5 = 0
        if truth5!=0:
            d = int(d)
            if d > f:
                print "The egg breaks."
                e = e - 1
                print e,"egg(s) remaining."
                tries = tries - 1
                print tries,"drops remaining."
                q3()
            else:
                print "The egg is unaffected."
                tries = tries - 1
                print tries,"drops remaining."
                q3()
        else:
            print "Please choose a valid number."
            raw_input("")
            q3()
    
seteggs()
setqcount()
q1()
q2()
m()
cls()

print "You start your job and take census of a local area. All is going well until..."
raw_input("")
print "You come across a woman who wont give up personal information as easily as everyone else."\

def ages():
    cls()
    print "You want to know the ages of her children"
    print "She says she has three children whose ages multiply to 72 and add to her house address"
    raw_input("")
    print "It's not enough information"
    raw_input("")
    print "Right before she closes the door to her house she says she needs to take her eldest daughter to music lessons"
    a = raw_input("What is the age of her eldest duaghter? ")
    b = raw_input("What is the age of her second daughter? ")
    c = raw_input("What is the age of her third daughter? ")
    if a == "8" and b == "3" and c == "3":
        print "You figured out their ages! Press Enter to continue."
        raw_input("")
    else:
        print "Those are not the right numbers. Press Enter to try again."
        raw_input("")
        ages()

ages()
cls()

print "After a week of taking the census of a local area, you take the paycheck and quit your job."
raw_input("")
print "You then buy the game with the money you earned"
raw_input("")
print "'S_____'s Puzzle Challenge- HD edition'- wow the graphics are great..."
print "But the gameplay is bad. The original was much better."
raw_input("")
print "You throw your newly bought video game into the garbage and you're pretty much back to where you started."
raw_input("")
cls()

print "Congratulations! You beat S_____'s Puzzle Challenge!"
print "I hope you had a fun time." 

raw_input("") #Stops from closing at the end

