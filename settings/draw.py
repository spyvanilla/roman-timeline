import os
import json

import pygame

pygame.font.init()
title_font = pygame.font.Font('Cloude_Regular_1.02.ttf',100)
header_font = pygame.font.Font('Cloude_Regular_1.02.ttf',50)
game_font = pygame.font.Font('Cloude_Regular_1.02.ttf',30)

white = (255,255,255)
black = (0,0,0)

high_empire_arrows = [
    (300,300),
    (479,300),
    (658,300),
    (900,300),
    (1079,300),
    (1258,300)
]
high_empire_periods = [
    [game_font.render('7600 A.C',1,white),(200,270)],
    [game_font.render('7500 A.C',1,white),(800,270)],
    [game_font.render('7400 A.C',1,white),(1400,270)]
]

low_empire_arrows = [
    (300,300),
    (479,300),
    (658,300),
    (837,300),
    (1016,300)
]
low_empire_periods = [
    [game_font.render('453 D.C',1,white),(200,270)],
    [game_font.render('395 D.C',1,white),(1116,270)]
]

with open('square_positions.json','r',encoding='utf-8') as file:
    data = json.load(file)
    high_empire_square_positions = data['high_empire_square_positions']
    low_empire_square_positions = data['low_empire_square_positions']

    for position,player_pos in enumerate(high_empire_square_positions):
        high_empire_square_positions[position][0] = tuple(player_pos[0])
        high_empire_square_positions[position][2] = tuple(player_pos[2])

    for position,player_pos in enumerate(low_empire_square_positions):
        low_empire_square_positions[position][0] = tuple(player_pos[0])
        low_empire_square_positions[position][2] = tuple(player_pos[2])

class Draw:
    def __init__(self,window,width,height,high_empire_button,low_empire_button):
        self.window = window
        self.width = width
        self.height = height
        self.high_empire_button = high_empire_button
        self.low_empire_button = low_empire_button

        self.arrow = pygame.image.load(os.path.join('Images/arrow.png')).convert_alpha()
        self.colosseum = pygame.transform.scale(pygame.image.load(os.path.join('Images/colosseum.png')),(800,600)).convert()

        self.button = pygame.image.load(os.path.join('Images/button.png')).convert_alpha()

    def fade(self):
        fade = pygame.Surface((self.width,self.height))
        fade.fill(black)

        for alpha in range(0,300):
            fade.set_alpha(alpha)
            self.redraw_menu()
            self.window.blit(fade,(0,0))

            pygame.display.update()
            pygame.time.delay(3)

    def redraw_menu(self):
        title = title_font.render('O Império Romano',1,white)
        header = header_font.render('Choose your campaign',1,white)

        button1_text = header_font.render('Alto Império',1,black)
        button2_text = header_font.render('Baixo Império',1,black)

        self.window.blit(self.colosseum,(0,0))

        self.window.blit(title,(400-title.get_width()//2,5))
        self.window.blit(header,(400-header.get_width()//2,55))

        self.window.blit(self.button,(32,350))
        self.window.blit(self.button,(506,350))

        self.window.blit(button1_text,(self.high_empire_button.x+112-button1_text.get_width()//2,self.high_empire_button.y+42-button1_text.get_height()//2))
        self.window.blit(button2_text,(self.low_empire_button.x+112-button2_text.get_width()//2,self.low_empire_button.y+42-button2_text.get_height()//2))

    def menu(self):
        title = title_font.render('O Império Romano',1,white)
        header = header_font.render('Choose your campaign',1,white)

        button1_text = header_font.render('Alto Império',1,black)
        button2_text = header_font.render('Baixo Império',1,black)

        self.window.blit(self.colosseum,(0,0))

        self.window.blit(title,(400-title.get_width()//2,5))
        self.window.blit(header,(400-header.get_width()//2,55))

        self.window.blit(self.button,(32,350))
        self.window.blit(self.button,(506,350))

        self.window.blit(button1_text,(self.high_empire_button.x+112-button1_text.get_width()//2,self.high_empire_button.y+42-button1_text.get_height()//2))
        self.window.blit(button2_text,(self.low_empire_button.x+112-button2_text.get_width()//2,self.low_empire_button.y+42-button2_text.get_height()//2))

        pygame.display.update()

    def draw(self,player,map_limit,obstacle_view,square_width,square_height,empire,display_square=None):
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

        self.window.fill(black)
        self.window.blit(title,(25-obstacle_view,5))
        
        for arr in arrows:
            self.window.blit(self.arrow,(arr[0]-obstacle_view,arr[1]))

        for period in periods:
            period_rect = pygame.Rect(period[1][0]-obstacle_view,period[1][1],5,20)
            pygame.draw.rect(self.window,white,period_rect)
            self.window.blit(period[0],(period_rect.x-period[0].get_width()//2,240))

        pygame.draw.line(self.window,white,start_pos,end_pos,width=10)
        pygame.draw.rect(self.window,white,player)

        if display_square is not None:
            square = pygame.Rect(display_square[0][0]-obstacle_view,display_square[0][1],square_width,square_height)
            pygame.draw.rect(self.window,white,square,border_radius=10)

            if len(display_square) > 1:
                title = game_font.render(display_square[1][0],1,black)

                self.window.blit(title,(square.x+100-title.get_width()//2,square.y+20-title.get_height()//2))

                for position,text in enumerate(display_square[1][1:]):
                    text = game_font.render(text,1,black)
                    self.window.blit(text,(square.x+2,square.y+40+position*10-text.get_height()//2))

        pygame.display.update()