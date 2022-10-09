#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:48:59 2021

@author: arjunbommadevara
"""

import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = (1300, 700)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DRGAON WAR')

COLOR = (255, 140, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = pygame.font.Font(os.path.join('Assets', 'Minecraft.ttf'), 75)

#BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
BORDER = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'wall.png')), (10, HEIGHT))

FPS = 60

DRAGON_SPEED = 9 
FIREBALL_SPEED = 40

DRAGON_WIDTH, DRAGON_HEIGHT = (118, 115)

FIREBALL_WIDTH, FIREBALL_HEIGHT = (110, 105)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))

HEART = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Health.png')), (50, 50))


class RedDragon(pygame.sprite.Sprite):
    
    def __init__(self):
        self.red_drag_sprites = []
        self.red_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'red_dragon_1.png')))
        self.red_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'red_dragon_2.png')))
        self.red_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'red_dragon_3.png')))
        self.red_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'red_dragon_4.png')))
        
        self.curr_red_sprite = 0
        
        self.red_image = self.red_drag_sprites[self.curr_red_sprite]
        
        self.health = 10
        self.max_health = 10
        
    def show_health(self):
        
        for i in range(self.health):
            WINDOW.blit(HEART, (1250 - ((i * 50)+10), 20))
    
    def update(self):
        self.curr_red_sprite += 0.15
        
        if self.curr_red_sprite >= len(self.red_drag_sprites):
            self.curr_red_sprite = 0
            
        self.red_image = self.red_drag_sprites[int(self.curr_red_sprite)]
        
        self.show_health()
class BlueDragon(pygame.sprite.Sprite):
    
    def __init__(self):
        self.blue_drag_sprites = []
        self.blue_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_dragon_1.png')))
        self.blue_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_dragon_2.png')))
        self.blue_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_dragon_3.png')))
        self.blue_drag_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_dragon_4.png')))
        
        self.curr_blue_sprite = 0
        
        self.blue_image = self.blue_drag_sprites[self.curr_blue_sprite]
        
        self.health = 10
        self.max_health = 10
        
    def show_health(self):
        
        for i in range(self.health):
            WINDOW.blit(HEART, ((i * 50)+10, 20))
        
            
    def update(self):
        self.curr_blue_sprite += 0.15
        
        if self.curr_blue_sprite >= len(self.blue_drag_sprites):
            self.curr_blue_sprite = 0
            
        self.blue_image = self.blue_drag_sprites[int(self.curr_blue_sprite)]
        self.show_health()

class RedFireball(pygame.sprite.Sprite):
            
    def __init__(self):
        
            self.red_fire_sprites = []
        
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '1.png')))
            self.red_fire_sprites[0] = pygame.transform.rotate(self.red_fire_sprites[0], 180)
            self.red_fire_sprites[0] = pygame.transform.scale(self.red_fire_sprites[0], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '4.png')))
            self.red_fire_sprites[1] = pygame.transform.rotate(self.red_fire_sprites[1], 180)
            self.red_fire_sprites[1] = pygame.transform.scale(self.red_fire_sprites[1], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '7.png')))
            self.red_fire_sprites[2] = pygame.transform.rotate(self.red_fire_sprites[2], 180)
            self.red_fire_sprites[2] = pygame.transform.scale(self.red_fire_sprites[2], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '10.png')))
            self.red_fire_sprites[3] = pygame.transform.rotate(self.red_fire_sprites[3], 180)
            self.red_fire_sprites[3] = pygame.transform.scale(self.red_fire_sprites[3], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '13.png')))
            self.red_fire_sprites[4] = pygame.transform.rotate(self.red_fire_sprites[4], 180)
            self.red_fire_sprites[4] = pygame.transform.scale(self.red_fire_sprites[4], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '16.png')))
            self.red_fire_sprites[5] = pygame.transform.rotate(self.red_fire_sprites[5], 180)
            self.red_fire_sprites[5] = pygame.transform.scale(self.red_fire_sprites[5], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '19.png')))
            self.red_fire_sprites[6] = pygame.transform.rotate(self.red_fire_sprites[6], 180)
            self.red_fire_sprites[6] = pygame.transform.scale(self.red_fire_sprites[6], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '22.png')))
            self.red_fire_sprites[7] = pygame.transform.rotate(self.red_fire_sprites[7], 180)
            self.red_fire_sprites[7] = pygame.transform.scale(self.red_fire_sprites[7], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '25.png')))
            self.red_fire_sprites[8] = pygame.transform.rotate(self.red_fire_sprites[8], 180)
            self.red_fire_sprites[8] = pygame.transform.scale(self.red_fire_sprites[8], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.red_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'red_fireball', '28.png')))
            self.red_fire_sprites[9] = pygame.transform.rotate(self.red_fire_sprites[9], 180)
            self.red_fire_sprites[9] = pygame.transform.scale(self.red_fire_sprites[9], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            

            
            self.isshot = False
            
            
            self.rfire = 0
            
            self.red_image = self.red_fire_sprites[self.rfire]
        
    def update(self):
        self.rfire += 1
        
        if self.rfire >= len(self.red_fire_sprites):
            self.rfire = 0
            
        self.red_image = self.red_fire_sprites[int(self.rfire)]
    

class BlueFireball(pygame.sprite.Sprite):
            
    def __init__(self,):
        
            self.blue_fire_sprites = []
        
            self.blue_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_fireball', '1.png')))
            self.blue_fire_sprites[0] = pygame.transform.scale(self.blue_fire_sprites[0], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.blue_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_fireball', '7.png')))
            self.blue_fire_sprites[1] = pygame.transform.scale(self.blue_fire_sprites[1], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.blue_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_fireball', '13.png')))
            self.blue_fire_sprites[2] = pygame.transform.scale(self.blue_fire_sprites[2], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.blue_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_fireball', '19.png')))
            self.blue_fire_sprites[3] = pygame.transform.scale(self.blue_fire_sprites[3], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            self.blue_fire_sprites.append(pygame.image.load(os.path.join('Assets', 'blue_fireball', '25.png')))
            self.blue_fire_sprites[4] = pygame.transform.scale(self.blue_fire_sprites[4], (FIREBALL_WIDTH, FIREBALL_HEIGHT))
            
        
            self.isshot = False
            
            self.bfire = 0
            
            
            
            self.blue_image = self.blue_fire_sprites[self.bfire]
        
    def update(self):
        self.bfire += 1
        
        if self.bfire >= len(self.blue_fire_sprites):
            self.bfire = 0
            
        self.blue_image = self.blue_fire_sprites[int(self.bfire)]
        

def blue_movement(keys_pressed, blue):
    
    if keys_pressed[pygame.K_w] and blue.y - DRAGON_SPEED > 0: #up  
        blue.y -= DRAGON_SPEED
    if keys_pressed[pygame.K_a] and blue.x - DRAGON_SPEED > 0: #left 
        blue.x -= DRAGON_SPEED
    if keys_pressed[pygame.K_s] and blue.y + DRAGON_SPEED + 100 < HEIGHT : #down 
        blue.y += DRAGON_SPEED
    if keys_pressed[pygame.K_d] and blue.x + DRAGON_SPEED + 120 < WIDTH//2 - 5: #right 
        blue.x += DRAGON_SPEED

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_UP] and red.y - DRAGON_SPEED > 0: #up 
        red.y -= DRAGON_SPEED
    if keys_pressed[pygame.K_LEFT] and red.x - DRAGON_SPEED > WIDTH//2+5: #left 
        red.x -= DRAGON_SPEED
    if keys_pressed[pygame.K_DOWN] and red.y + DRAGON_SPEED + 100 < HEIGHT: #down  
        red.y += DRAGON_SPEED
    if keys_pressed[pygame.K_RIGHT] and red.x + DRAGON_SPEED + 120 < WIDTH : #right 
        red.x += DRAGON_SPEED


def drawWindow(red, red_dragon, blue, blue_dragon):
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(BORDER, (WIDTH/2 - 5, 0))
    WINDOW.blit(red_dragon.red_image, (red.x, red.y))
    WINDOW.blit(blue_dragon.blue_image, (blue.x, blue.y))
    red_dragon.update()
    blue_dragon.update()

def shootRedFire(pos, red_fireball):
    
    WINDOW.blit(red_fireball.red_image, (pos.x, pos.y))
    red_fireball.update()
    
def shootBlueFire(pos, blue_fireball):
    
    WINDOW.blit(blue_fireball.blue_image, (pos.x, pos.y))
    blue_fireball.update()
    
def draw_winner(text):
    draw_text = FONT.render(text, 1, WHITE)
    WINDOW.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, (HEIGHT//2 - draw_text.get_height()/2)+200))
    pygame.display.update()
    pygame.time.delay(5000)
    
def main():
    
    red_dragon = RedDragon()
    blue_dragon = BlueDragon()
    
    red_fireball = RedFireball()
    blue_fireball = BlueFireball()
    
    red = pygame.Rect(915, 290, DRAGON_WIDTH, DRAGON_HEIGHT)
    blue = pygame.Rect(265, 290, DRAGON_WIDTH, DRAGON_HEIGHT)
    
    run = True
    
    clock = pygame.time.Clock()
    
    
    while run:
        clock.tick(FPS)
        
        # winner_text = ""
        # if blue_dragon.health <= 0:
        #     winner_text = "Red Wins!"
        # elif red_dragon.health <= 0:
        #     winner_text = "Blue Wins!"
            
        # if winner_text != "":
        #     draw_winner(winner_text)
        #     drawWindow(red, red_dragon, blue, blue_dragon)
        #     break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT and not red_fireball.isshot:
                    redfire_pos = pygame.Rect(red.x, red.y, FIREBALL_WIDTH, FIREBALL_HEIGHT)
                    red_fireball.isshot = True
                if event.key == pygame.K_LSHIFT and not blue_fireball.isshot:
                    bluefire_pos = pygame.Rect(blue.x, blue.y, FIREBALL_WIDTH, FIREBALL_HEIGHT)
                    blue_fireball.isshot = True
                
        
        keys_pressed = pygame.key.get_pressed()
        
        red_movement(keys_pressed, red)
        
        blue_movement(keys_pressed, blue)
        
        drawWindow(red, red_dragon, blue, blue_dragon)
        
        
        
        if red_fireball.isshot:
            shootRedFire(redfire_pos, red_fireball)
            if redfire_pos.x - (FIREBALL_SPEED) < 0 :
                red_fireball.isshot = False
            elif (redfire_pos.x < (blue.x + DRAGON_WIDTH) and ((redfire_pos.y > (blue.y-40) and redfire_pos.y < blue.y+59) or (redfire_pos.y > (blue.y+59) and redfire_pos.y < blue.y+70))):
                if blue_dragon.health > 0:
                    blue_dragon.health -= 1
                red_fireball.isshot = False
                redfire_pos = pygame.Rect(red.x, red.y, FIREBALL_WIDTH, FIREBALL_HEIGHT)
            else:
                redfire_pos.x -= FIREBALL_SPEED
                
        
        if blue_fireball.isshot:
            shootBlueFire(bluefire_pos, blue_fireball)
            if bluefire_pos.x + FIREBALL_SPEED > WIDTH:
                blue_fireball.isshot = False
            elif (bluefire_pos.x > red.x and ((bluefire_pos.y > (red.y-40) and bluefire_pos.y < red.y+59) or (bluefire_pos.y > (red.y+59) and bluefire_pos.y < red.y+70))):
                if red_dragon.health > 0:
                    red_dragon.health -= 1
                blue_fireball.isshot = False
                bluefire_pos = pygame.Rect(blue.x, blue.y, FIREBALL_WIDTH, FIREBALL_HEIGHT)
            else:
                bluefire_pos.x += FIREBALL_SPEED
        
        winner_text = ""
        
        if red_dragon.health == 0:
            winner_text = "Blue Dragon Wins!"
        
        if blue_dragon.health == 0:
            winner_text = "Red Dragon Wins!"
            
        if winner_text != "":
            draw_winner(winner_text)
            break

        pygame.display.update()
        
    
    
    pygame.quit()
    
if __name__ == '__main__':
    main()