# Athor : Jeong Seokcheon, Kim Wonjung

import pgzrun
from random import randint

# Basic setting
WIDTH = 500
HEIGHT = 500
PLAYER_SPEED = 5
MONSTER_MAX_SPEED = 10

hp = 100
score = 0
count = 10      # Monster count
monsters = []   # Save monster to list

# Player setting
player = Actor('main')
player.pos = (WIDTH/2, HEIGHT/2)

# Declaration for animation action on keyboard input
player_right_move = True
player_left_move = True

# Create one monster
def makeMonster():
    global monsters, MONSTER_MAX_SPEED
    monster = Actor('monster')
    monster.pos =(randint(0, WIDTH), randint(0, HEIGHT))
    monster.vx = randint(-MONSTER_MAX_SPEED, MONSTER_MAX_SPEED)
    monster.vy = randint(-MONSTER_MAX_SPEED, MONSTER_MAX_SPEED)
    monsters.append(monster)

# Create monster
for n in range(count):
    makeMonster()

# Update screen
def update():
    global hp, score, count, MONSTER_MAX_SPEED

    if(hp > 0):
        score += 1    
        movePlayer()
        
        # Monster moving
        for monster in monsters:
            monster.x  += monster.vx
            monster.y  += monster.vy

            if(monster.left < 0 or monster.right > WIDTH):
                monster.vx = -monster.vx
            if(monster.top < 0 or monster.bottom > HEIGHT):
                monster.vy = -monster.vy
            if(monster.colliderect(player)):
                hp -= 1
    else:
        hp = 0

# Right animation
def move_right():
    global player_right_move, hp
    
    # Change move image
    if(hp > 50):
        if(player_right_move):
            player.image = "main_m"
            player_right_move = False
        else:
            player.image = "main"
            player_right_move = True
    else:
        if(player_right_move):
            player.image = "main_bm"
            player_right_move = False
        else:
            player.image = "main_b"
            player_right_move = True

# Left animation
def move_left():
    global player_left_move, hp
    
    # Change move image
    if(hp > 50):
        if(player_left_move):
            player.image = "main_rm"
            player_left_move = False
        else:
            player.image = "main_r"
            player_left_move = True
    else:
        if(player_left_move):
            player.image = "main_rbm"
            player_left_move = False
        else:
            player.image = "main_rb"
            player_left_move = True

# Player moving
def movePlayer():

    if(keyboard[keys.A]):
        move_left()
        player.left -= PLAYER_SPEED
    elif(keyboard[keys.D]):
        move_right()
        player.left += PLAYER_SPEED

    if(keyboard[keys.W]):
        player.top -= PLAYER_SPEED
    elif(keyboard[keys.S]):
        player.top += PLAYER_SPEED


    # Out of screen event
    if(player.left < 0):
        player.left = 0
    elif(player.right > WIDTH):
        player.right = WIDTH

    if( player.top < 0):
        player.top = 0
    elif(player.bottom > HEIGHT):
        player.bottom = HEIGHT


# Create screen
def draw():
    global count, hp, score
    
    screen.clear()
    screen.fill("gray")
    player.draw()

    # Create monster
    for monster in monsters:
        monster.draw()
    
    # Draw hp, score
    screen.draw.text(str(hp), topright=(WIDTH,5), fontsize=40, color="white", owidth=1, ocolor="red")
    screen.draw.text(str(score),midtop=(WIDTH/2,5), fontsize=40, color="gray25", owidth=1, ocolor="white")

    if(hp == 0):
        screen.draw.text("Score: {0:0}".format(score), midtop=(WIDTH/2,HEIGHT/3), align="Center", fontsize=HEIGHT / 7, color="black", owidth=1, ocolor="white")
        screen.draw.text("RETRY?", midtop=(WIDTH/2,HEIGHT/2), align="Center", fontsize=HEIGHT / 10, color="dodgerblue1", owidth=1, ocolor="white")
        screen.draw.text("PRESS [SPACEBAR]", midtop=(WIDTH/2,HEIGHT/1.7), align="Center", fontsize=HEIGHT / 15, color="dodgerblue1", owidth=1, ocolor="white")
        
        # Retry
        if(keyboard[keys.SPACE]):
            hp = 100
            score = 0
            player.pos = (WIDTH/2, HEIGHT/2)

pgzrun.go()