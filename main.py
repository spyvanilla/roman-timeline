import sys
import os

import pygame

pygame.font.init()
game_font = pygame.font.Font('Cloude_Regular_1.02.ttf',30)

width,height = 800,600

window = pygame.display.set_mode((width, height))
name = pygame.display.set_caption('Roman Empire Timeline')

map_limit = 0
obstacle_view = 0

arrow = pygame.image.load(os.path.join('arrow.png')).convert_alpha()
arrows = [(300,300),(900,300)]

black = (0,0,0)
white = (255,255,255)

player = pygame.Rect(10,250,10,10)
player_velocity = 5

square_width = 0
square_height = 0

square_positions = [
    [(250,360),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(260,321)],
    [(850,960),['Decoy title','Decoy text 1','Decoy text 2','Decoy text 3','Decoy text 4','Decoy text 5'],(860,321)]
]

line_position = 10

def open_animation():
    global square_width,square_height

    if square_width == 100 and square_height == 100:
        return True

    square_width += 10
    square_height += 10

def movement(keys_pressed):
    global square_width,square_height,map_limit,obstacle_view,line_position

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

def draw(display_square=None):
    start_pos = (0,290)
    end_pos = (8000-map_limit,290)

    window.fill(black)
    
    for arr in arrows:
        window.blit(arrow,(arr[0]-obstacle_view,arr[1]))

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
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys_pressed = pygame.key.get_pressed()
        display_square = movement(keys_pressed)
        draw(display_square)

if __name__ == '__main__':
    main()