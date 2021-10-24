import pygame
from math import sin,cos,pi, radians

from pygame.draw import circle
pygame.init()
win_width = 1000
win_height = 750
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Hardest game on Earth")
font = pygame.font.SysFont('comicsans', 75, True)
font_2 =pygame.font.SysFont('comicsans', 75, True)
font_3 =pygame.font.SysFont('comicsans', 75, True)
Black = (0, 0, 0)
White = (255, 255, 255)
Gray = (128,128,128)
Light_gray = (235,236,240)
Green = (0, 128, 0)
Yellow = (255, 255, 0)
Light_green = (144,238,144)
Red = (255, 0, 0)
Brown = (150, 75, 0)
Blue = (0,0,255)
Light_blue = (135, 206, 235)
Dark_Brown = (101, 67, 33)
Orange = (255,165,0)
Lava_color = (247, 104, 6)
level = 1
e,r = 250, 0
t,u= 400, 700
o,p = 600, 0
g,h = 800, 700
x, y = 0, 350
extra_x, extra_y = 200, 0
extra_y_vel = 19
extra_1_x, extra_1_y = 450, 0
extra_1_y_vel = 16
extra_2_x, extra_2_y = 750, 0
extra_2_y_vel = 17
Death = 0
FPS = 60
r_vel = 13
u_vel = 13
p_vel = 13
h_vel = 13
e_vel = 13
t_vel = 13
o_vel = 13
g_vel = 13
cir_x , cir_y = 475, 225
cir_x_vel = 25
cir_y_vel = 22
vel = 5
current_level = 1
str_level = level
a = True
Right = True
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 950:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN]  and y < 710:
        y += vel
    if a == True:
        r += r_vel
    if r > 700:
        r_vel = -r_vel
    elif r < 0:
        r_vel = -r_vel
    u -= u_vel
    if u < 0:
        u_vel = -u_vel
    if u > 700:
        u_vel = -u_vel

    p += p_vel
    if p > 700:
        p_vel = -p_vel
    if p < 0:
        p_vel = -p_vel

    h -= h_vel
    if h < 0:
        h_vel = -h_vel
    if h > 700:
        h_vel = -h_vel


    win.fill(White)
    pygame.draw.rect(win, Light_gray,(0, 0, 100, 1000))
    Player = pygame.draw.rect(win, Red, (x, y , 50, 50))
    r_block = pygame.draw.rect(win, Light_blue, (e, r , 50, 50))
    u_block = pygame.draw.rect(win, Light_blue, (t, u , 50, 50))
    p_block = pygame.draw.rect(win, Light_blue, (o, p , 50, 50))
    h_block = pygame.draw.rect(win, Light_blue, (g, h , 50, 50))
    win_base = pygame.draw.rect(win, Light_green,(900, 0, 100, 1000))
    text = font.render("You lose! press r to play again", 1, Black)
    text_2 = font_2.render("Level: " + str(str_level), 1, Black)
    text_3 = font_3.render("Death: " + str(Death), 1, Black)
    win.blit(text_2, (0, 0))
    win.blit(text_3, (700, 0))
    pygame.Rect(Player)
    pygame.Rect(win_base)
    pygame.Rect(u_block)
    pygame.Rect(r_block)
    pygame.Rect(p_block)
    pygame.Rect(h_block)

    if Player.colliderect(u_block):
        Right = False
    if Player.colliderect(r_block):
        Right = False
    if Player.colliderect(p_block):
        Right = False
    if Player.colliderect(h_block):
        Right = False
    if level == 2:
        brick = pygame.draw.rect(win, Black, (100, 350 , 800, 50))
        pygame.Rect(brick)
        if Player.colliderect(brick):
            Right = False
        if r_block.colliderect(brick):
            r_vel = 16
            r_vel = -r_vel
        if u_block.colliderect(brick):
            u_vel = -u_vel
        if p_block.colliderect(brick):
            p_vel = -p_vel
        if h_block.colliderect(brick):
            h_vel = 16
            h_vel = -h_vel
    if level == 3:
        u = -1000
        t = -1000
        o = -1000
        p = -1000
        cir = pygame.draw.circle(win, Light_blue, (cir_x,cir_y), 25)
        cir_x -= cir_x_vel
        cir_y += cir_y_vel
        if cir_x > 650:
            cir_x_vel = -cir_x_vel
        if cir_x < 325:
            cir_x_vel = -cir_x_vel
        if cir_y < 0:
            cir_y_vel = -cir_y_vel
        if cir_y > 725:
            cir_y_vel = -cir_y_vel
        u_vel = 30
        p_vel = 30
        if Player.colliderect(cir):
            Right = False
    if level == 4:
        extra_1_block = pygame.draw.rect(win, Light_blue, (extra_x, extra_y , 50, 50))
        extra_y += extra_y_vel
        if extra_y > 700 or extra_y < 0:
            extra_y_vel = -extra_y_vel
        extra_2_block = pygame.draw.rect(win, Light_blue, (extra_1_x, extra_1_y , 50, 50))
        extra_1_y += extra_1_y_vel
        if extra_1_y > 700 or extra_1_y < 0:
            extra_1_y_vel = -extra_1_y_vel
        extra_3_block = pygame.draw.rect(win, Light_blue, (extra_2_x, extra_2_y , 50, 50))
        extra_2_y += extra_2_y_vel
        if extra_2_y > 700 or extra_2_y < 0:
            extra_2_y_vel = -extra_2_y_vel
        pygame.Rect(extra_1_block)
        pygame.Rect(extra_2_block)
        pygame.Rect(extra_3_block)
        if Player.colliderect(extra_3_block):
            Right = False
        if Player.colliderect(extra_1_block):
            Right = False
        if Player.colliderect(extra_2_block):
            Right = False
        p = 225
        h = 450
        t += t_vel
        o += o_vel
        g += g_vel
        e += e_vel
        if t > 850 or t < 120:
            t_vel = -t_vel
        if o > 850 or o < 120:
            o_vel = -o_vel
        if g > 850 or g < 120:
            g_vel = -g_vel
        if e > 850 or e < 120:
            e_vel = -e_vel
        r_vel = 0
        u_vel = 0
        p_vel = 0
        h_vel = 0
    if Right == False:
        Right = True
        Death += 1
        x, y = 0, 350
        r_vel = 14
        u_vel = 14
        p_vel = 14
        h_vel = 14
        vel = 5
        level = current_level
        r_vel = 14
        u_vel = 14
        p_vel = 14
        vel = 5
        h_vel = 14
        x = 0
        y = 400
        e,r = 200, 0
        t,u= 400, 700
        o,p = 600, 0
        g,h = 800, 700
    
    if Player.colliderect(win_base):
        e,r = 200, 0
        t,u= 400, 700
        o,p = 600, 0
        g,h = 800, 700
        x, y = 0, 400
        vel = 5
        level += 1

    str_level = level
    if level > current_level:
        current_level = level

    pygame.display.update()