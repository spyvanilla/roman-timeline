import json

import pygame

high_empire_limit = 800
low_empire_limit = 1000

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

class Movement:
    def __init__(self,player):
        self.player = player
        self.player_velocity = 5

        self.square_width = 0
        self.square_height = 0

        self.map_limit = 0
        self.obstacle_view = 0

        self.line_position = 10
        self.current_direction = 1

        self.current_sprite = 0
        self.movement_count = 0

    def reset(self):
        self.player.x = 10

        self.square_width = 0
        self.square_height = 0

        self.map_limit = 0
        self.obstacle_view = 0

        self.line_position = 10

    def open_animation(self):
        if self.square_width == 200 and self.square_height == 200:
            return True

        self.square_width += 20
        self.square_height += 20

    def change_sprite(self):
        self.current_sprite += 1

        if self.current_sprite > 11:
            self.current_sprite = 0

    def movement(self,keys_pressed,empire):
        if empire == 1:
            square_positions = high_empire_square_positions
            empire_limit = high_empire_limit
        else:
            square_positions = low_empire_square_positions
            empire_limit = low_empire_limit

        if keys_pressed[pygame.K_a]:
            if self.current_direction == 1:
                self.current_direction = 0
                self.current_sprite = 0
                self.movement_count = 0

            if self.player.x == 390:
                self.map_limit -= self.player_velocity
                self.obstacle_view -= self.player_velocity
                self.line_position -= self.player_velocity

                if self.map_limit <= 0:
                    self.player.x = 385
                    self.line_position = 385
                    self.map_limit = 0
            else:
                if self.player.x >= -75:
                    self.player.x -= self.player_velocity
                    self.line_position -= self.player_velocity
            self.movement_count += 1

            if self.movement_count == 6:
                self.change_sprite()
                self.movement_count = 0

        if keys_pressed[pygame.K_d]:
            if self.current_direction == 0:
                self.current_direction = 1
                self.current_sprite = 0
                self.movement_count = 0

            if self.player.x == 390:
                self.map_limit += self.player_velocity
                self.obstacle_view += self.player_velocity
                self.line_position += self.player_velocity

                if self.map_limit >= empire_limit:
                    self.player.x = 395
                    self.map_limit = empire_limit
            else:
                if self.player.x <= 670:
                    self.player.x += self.player_velocity
                    self.line_position += self.player_velocity
            self.movement_count += 1

            if self.movement_count == 6:
                self.change_sprite()
                self.movement_count = 0

        for square_position in square_positions:
            if self.line_position >= square_position[0][0] and self.line_position <= square_position[0][1]:
                display = self.open_animation()

                if display is not None:
                    return self.map_limit,self.obstacle_view,self.square_width,self.square_height,self.current_direction,self.current_sprite,[square_position[2],square_position[1]]
                return self.map_limit,self.obstacle_view,self.square_width,self.square_height,self.current_direction,self.current_sprite,[(square_position[2])]
        else:
            self.square_width = 0
            self.square_height = 0

        return self.map_limit,self.obstacle_view,self.square_width,self.square_height,self.current_direction,self.current_sprite,None