import pygame
from pygame.locals import *
import os
pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
sky = pygame.image.load("./img/sky.png")
tile_size = 50
pygame.display.update()
world_map = [
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),
    (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)
]
running = True
def load_sprites():
    # Set the path of the image directory
    img_dir = ".\img"
    # Load all images in the directory
    images = {}
    for img_file in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_file).replace("\\","/")
        if os.path.isfile(img_path):
            images[img_file] = pygame.image.load(img_path)

    # Test if the images have been loaded successfully
    for img_name, img in images.items():
        print(f"{img_name} loaded successfully with size {img.get_size()}")
    return images

sprites = load_sprites()
def draw_tiles(data):
    row_count = 0
    for row in data:
        col_count = 0
        for tile in row:
            screen.blit(sprites[tile],tile*tile_size)
            col_count +=1
        row_count+=1
print (sprites)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(sky,(0,0))
    draw_tiles(world_map)
    pygame.display.update()
pygame.quit()
