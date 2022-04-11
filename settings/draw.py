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
    (837,300),
    (1016,300),
    (1195,300)
]
high_empire_periods = [
    [game_font.render('27 A.C',1,white),(200,270)],
    [game_font.render('3 D.C',1,white),(1295,270)]
]
high_empire_end = 1500

low_empire_arrows = [
    (300,300),
    (479,300),
    (658,300),
    (837,300),
    (1016,300),
    (1195,300),
    (1374,300)
]
low_empire_periods = [
    [game_font.render('453 D.C',1,white),(200,270)],
    [game_font.render('395 D.C',1,white),(1474,270)]
]
low_empire_end = 1700

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
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('Images/background.png')),(800,600)).convert()
        self.button = pygame.image.load(os.path.join('Images/button.png')).convert_alpha()

        self.rightwalking1 = pygame.image.load(os.path.join('Right Sprites/rightwalking1.png')).convert_alpha()
        self.rightwalking2 = pygame.image.load(os.path.join('Right Sprites/rightwalking2.png')).convert_alpha()
        self.rightwalking3 = pygame.image.load(os.path.join('Right Sprites/rightwalking3.png')).convert_alpha()
        self.rightwalking4 = pygame.image.load(os.path.join('Right Sprites/rightwalking4.png')).convert_alpha()
        self.rightwalking5 = pygame.image.load(os.path.join('Right Sprites/rightwalking5.png')).convert_alpha()
        self.rightwalking6 = pygame.image.load(os.path.join('Right Sprites/rightwalking6.png')).convert_alpha()
        self.rightwalking7 = pygame.image.load(os.path.join('Right Sprites/rightwalking7.png')).convert_alpha()
        self.rightwalking8 = pygame.image.load(os.path.join('Right Sprites/rightwalking8.png')).convert_alpha()
        self.rightwalking9 = pygame.image.load(os.path.join('Right Sprites/rightwalking9.png')).convert_alpha()
        self.rightwalking10 = pygame.image.load(os.path.join('Right Sprites/rightwalking10.png')).convert_alpha()
        self.rightwalking11 = pygame.image.load(os.path.join('Right Sprites/rightwalking11.png')).convert_alpha()
        self.rightwalking12 = pygame.image.load(os.path.join('Right Sprites/rightwalking12.png')).convert_alpha()

        self.rightwalking = [
            self.rightwalking1,
            self.rightwalking2,
            self.rightwalking3,
            self.rightwalking4,
            self.rightwalking5,
            self.rightwalking6,
            self.rightwalking7,
            self.rightwalking8,
            self.rightwalking9,
            self.rightwalking10,
            self.rightwalking11,
            self.rightwalking12
        ]

        self.leftwalking1 = pygame.image.load(os.path.join('Left Sprites/leftwalking1.png')).convert_alpha()
        self.leftwalking2 = pygame.image.load(os.path.join('Left Sprites/leftwalking2.png')).convert_alpha()
        self.leftwalking3 = pygame.image.load(os.path.join('Left Sprites/leftwalking3.png')).convert_alpha()
        self.leftwalking4 = pygame.image.load(os.path.join('Left Sprites/leftwalking4.png')).convert_alpha()
        self.leftwalking5 = pygame.image.load(os.path.join('Left Sprites/leftwalking5.png')).convert_alpha()
        self.leftwalking6 = pygame.image.load(os.path.join('Left Sprites/leftwalking6.png')).convert_alpha()
        self.leftwalking7 = pygame.image.load(os.path.join('Left Sprites/leftwalking7.png')).convert_alpha()
        self.leftwalking8 = pygame.image.load(os.path.join('Left Sprites/leftwalking8.png')).convert_alpha()
        self.leftwalking9 = pygame.image.load(os.path.join('Left Sprites/leftwalking9.png')).convert_alpha()
        self.leftwalking10 = pygame.image.load(os.path.join('Left Sprites/leftwalking10.png')).convert_alpha()
        self.leftwalking11 = pygame.image.load(os.path.join('Left Sprites/leftwalking11.png')).convert_alpha()
        self.leftwalking12 = pygame.image.load(os.path.join('Left Sprites/leftwalking12.png')).convert_alpha()

        self.leftwalking = [
            self.leftwalking1,
            self.leftwalking2,
            self.leftwalking3,
            self.leftwalking4,
            self.leftwalking5,
            self.leftwalking6,
            self.leftwalking7,
            self.leftwalking8,
            self.leftwalking9,
            self.leftwalking10,
            self.leftwalking11,
            self.leftwalking12
        ]

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

    def draw(self,player,map_limit,obstacle_view,square_width,square_height,current_direction,current_sprite,empire,display_square=None):
        if empire == 1:
            title = title_font.render('Alto Império',1,white)
            arrows = high_empire_arrows
            periods = high_empire_periods
            empire_end = high_empire_end
        else:
            title = title_font.render('Baixo Império',1,white)
            arrows = low_empire_arrows
            periods = low_empire_periods
            empire_end = low_empire_end

        if current_direction == 1:
            walking = self.rightwalking
        else:
            walking = self.leftwalking
        end = title_font.render('Fim',1,white)

        start_pos = (0,290)
        end_pos = (8000-map_limit,290)

        self.window.blit(self.background,(0,0))
        self.window.blit(title,(25-obstacle_view,5))
        self.window.blit(end,(empire_end-obstacle_view,5))

        for arr in arrows:
            self.window.blit(self.arrow,(arr[0]-obstacle_view,arr[1]))

        for period in periods:
            period_rect = pygame.Rect(period[1][0]-obstacle_view,period[1][1],5,20)
            pygame.draw.rect(self.window,white,period_rect)
            self.window.blit(period[0],(period_rect.x-period[0].get_width()//2,240))

        pygame.draw.line(self.window,white,start_pos,end_pos,width=10)
        self.window.blit(walking[current_sprite],(player.x,172))

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