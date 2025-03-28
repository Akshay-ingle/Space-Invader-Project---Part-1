import math
import random
import pygame

screen_width = 800 
screen_height= 500
player_start_x= 370
player_start_y= 380
enemy_start_y_min= 50
enemy_start_y_max= 150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collison_distance= 27

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('space invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerimg= pygame.image.load('images.jpg')
playerx=player_start_x
playery=player_start_y
playerx_change=0

enemyimg =[]
enemyx=[]
enemyY=[]
enemyx_change=[]
enemyY_change=[]
num