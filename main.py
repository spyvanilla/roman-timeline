import sys

import pygame

from settings.draw import Draw
from settings.movement import Movement

width,height = 800,600

window = pygame.display.set_mode((width, height))
name = pygame.display.set_caption('Paulão Pintão')

black = (0,0,0)
white = (255,255,255)

high_empire_button = pygame.Rect(48,431,224,84)
low_empire_button = pygame.Rect(521,431,224,84)

player = pygame.Rect(10,250,10,10)

def main():
    draw = Draw(window,width,height,high_empire_button,low_empire_button)
    movement = Movement(player)

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
                    draw.fade()
                    screen = 2
                    empire = 1
                    click = False

            if low_empire_button.collidepoint((mx,my)):
                if click == True:
                    draw.fade()
                    screen = 3
                    empire = 2
                    click = False

            if click == True:
                click = False
            draw.menu()

        elif screen == 2:
            keys_pressed = pygame.key.get_pressed()
            map_limit,obstacle_view,square_width,square_height,display_square = movement.movement(keys_pressed,empire)
            draw.draw(player,map_limit,obstacle_view,square_width,square_height,empire,display_square)

            if map_limit == 500 and keys_pressed[pygame.K_RETURN]:
                screen = 1
                movement.reset()

        elif screen == 3:
            keys_pressed = pygame.key.get_pressed()
            map_limit,obstacle_view,square_width,square_height,display_square = movement.movement(keys_pressed,empire)
            draw.draw(player,map_limit,obstacle_view,square_width,square_height,empire,display_square)

            if map_limit == 500 and keys_pressed[pygame.K_RETURN]:
                screen = 1
                movement.reset()

if __name__ == '__main__':
    main() #AI RÉGUA MESSI MÍDIA