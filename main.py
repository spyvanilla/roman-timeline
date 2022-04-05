import sys
import os

import pygame

pygame.font.init()
title_font = pygame.font.Font('Cloude_Regular_1.02.ttf',100)
header_font = pygame.font.Font('Cloude_Regular_1.02.ttf',50)
game_font = pygame.font.Font('Cloude_Regular_1.02.ttf',30)

width,height = 800,600

window = pygame.display.set_mode((width, height))
name = pygame.display.set_caption('Roman Empire Timeline')

map_limit = 0
obstacle_view = 0

arrow = pygame.image.load(os.path.join('arrow.png')).convert_alpha()

colosseum = pygame.transform.scale(pygame.image.load(os.path.join('colosseum.png')),(800,600)).convert()

button = pygame.image.load(os.path.join('button.png')).convert_alpha()
high_empire_button = pygame.Rect(48,431,224,84)
low_empire_button = pygame.Rect(521,431,224,84)

black = (0,0,0)
white = (255,255,255)

player = pygame.Rect(10,250,10,10)
player_velocity = 5

square_width = 0
square_height = 0

high_empire_arrows = [
    (300,300),
    (479,300),
    (658,300)
]
high_empire_square_positions = [
    [(250,360),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(260,321)],
    [(429,539),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(439,321)],
    [(608,718),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(618,321)]
]
high_empire_periods = [
    [game_font.render('7600 A.C',1,white),(200,270)],
    [game_font.render('7500 A.C',1,white),(800,270)]
]

low_empire_arrows = [
    (300,300),
    (479,300),
    (658,300)
]
low_empire_square_positions = [
    [(250,360),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(260,321)],
    [(429,539),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(439,321)],
    [(608,718),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(618,321)]
]
low_empire_periods = [
    [game_font.render('7600 A.C',1,white),(200,270)],
    [game_font.render('7500 A.C',1,white),(800,270)]
]

line_position = 10

def open_animation():
    global square_width,square_height

    if square_width == 100 and square_height == 100:
        return True

    square_width += 10
    square_height += 10

def fade():
    fade = pygame.Surface((width,height))
    fade.fill(black)

    for alpha in range(0,300):
        fade.set_alpha(alpha)
        redraw_menu()
        window.blit(fade,(0,0))

        pygame.display.update()
        pygame.time.delay(3)

def redraw_menu():
    title = title_font.render('O Império Romano',1,white)
    header = header_font.render('Choose your campaign',1,white)

    button1_text = header_font.render('Alto Império',1,black)
    button2_text = header_font.render('Baixo Império',1,black)

    window.blit(colosseum,(0,0))

    window.blit(title,(400-title.get_width()//2,5))
    window.blit(header,(400-header.get_width()//2,55))

    window.blit(button,(32,350))
    window.blit(button,(506,350))

    window.blit(button1_text,(high_empire_button.x+112-button1_text.get_width()//2,high_empire_button.y+42-button1_text.get_height()//2))
    window.blit(button2_text,(low_empire_button.x+112-button2_text.get_width()//2,low_empire_button.y+42-button2_text.get_height()//2))

def menu():
    title = title_font.render('O Império Romano',1,white)
    header = header_font.render('Choose your campaign',1,white)

    button1_text = header_font.render('Alto Império',1,black)
    button2_text = header_font.render('Baixo Império',1,black)

    window.blit(colosseum,(0,0))

    window.blit(title,(400-title.get_width()//2,5))
    window.blit(header,(400-header.get_width()//2,55))

    window.blit(button,(32,350))
    window.blit(button,(506,350))

    window.blit(button1_text,(high_empire_button.x+112-button1_text.get_width()//2,high_empire_button.y+42-button1_text.get_height()//2))
    window.blit(button2_text,(low_empire_button.x+112-button2_text.get_width()//2,low_empire_button.y+42-button2_text.get_height()//2))

    pygame.display.update()

def movement(keys_pressed,empire):
    global square_width,square_height,map_limit,obstacle_view,line_position

    if empire == 1:
        square_positions = high_empire_square_positions
    else:
        square_positions = low_empire_square_positions

    if keys_pressed[pygame.K_a]:
        if player.x == 390:
            map_limit -= player_velocity
            obstacle_view -= player_velocity
            line_position -= player_velocity

            if map_limit <= 0:
                player.x = 385
                line_position = 385
                map_limit = 0
        else:
            if player.x >= 5:
                player.x -= player_velocity
                line_position -= player_velocity

    if keys_pressed[pygame.K_d]:
        if player.x == 390:
            map_limit += player_velocity
            obstacle_view += player_velocity
            line_position += player_velocity
        else:
            player.x += player_velocity
            line_position += player_velocity

    for square_position in square_positions:
        if line_position >= square_position[0][0] and line_position <= square_position[0][1]:
            display = open_animation()

            if display is not None:
                return square_position[2],square_position[1]
            return [(square_position[2])]
    else:
        square_width = 0
        square_height = 0

def draw(empire,display_square=None):
    if empire == 1:
        title = title_font.render('Alto Império',1,white)
        arrows = high_empire_arrows
        periods = high_empire_periods
    else:
        title = title_font.render('Baixo Império',1,white)
        arrows = low_empire_arrows
        periods = low_empire_periods

    start_pos = (0,290)
    end_pos = (8000-map_limit,290)

    window.fill(black)
    window.blit(title,(25-obstacle_view,5))
    
    for arr in arrows:
        window.blit(arrow,(arr[0]-obstacle_view,arr[1]))

    for period in periods:
        period_rect = pygame.Rect(period[1][0]-obstacle_view,period[1][1],5,20)
        pygame.draw.rect(window,white,period_rect)
        window.blit(period[0],(period_rect.x-period[0].get_width()//2,240))

    pygame.draw.line(window,white,start_pos,end_pos,width=10)
    pygame.draw.rect(window,white,player)

    if display_square is not None:
        square = pygame.Rect(display_square[0][0]-obstacle_view,display_square[0][1],square_width,square_height)
        pygame.draw.rect(window,white,square,border_radius=10)

        if len(display_square) > 1:
            title = game_font.render(display_square[1][0],1,black)

            window.blit(title,(square.x+50-title.get_width()//2,square.y+20-title.get_height()//2))

            for position,text in enumerate(display_square[1][1:]):
                text = game_font.render(text,1,black)
                window.blit(text,(square.x+50-text.get_width()//2,square.y+40+position*10-text.get_height()//2))

    pygame.display.update()

def main():
    screen = 1
    click = False
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if screen == 1:
            mx,my = pygame.mouse.get_pos()

            if high_empire_button.collidepoint((mx,my)):
                if click == True:
                    fade()
                    screen = 2
                    empire = 1
                    click = False

            if low_empire_button.collidepoint((mx,my)):
                if click == True:
                    fade()
                    screen = 3
                    empire = 2
                    click = False

            if click == True:
                click = False
            menu()

        elif screen == 2:
            keys_pressed = pygame.key.get_pressed()
            display_square = movement(keys_pressed,empire)
            draw(empire,display_square)

        elif screen == 3:
            keys_pressed = pygame.key.get_pressed()
            display_square = movement(keys_pressed,empire)
            draw(empire,display_square)

if __name__ == '__main__':
    main()