import pygame
import time

pygame.init()
pygame.display.set_caption("Mickey_Mouse_Clock")

background = pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/суреттер/mickeyclock.png')
right_arm = pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/суреттер/rightarm.png')
left_arm = pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/суреттер/leftarm.png')

WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CENTER = (WIDTH // 2, HEIGHT // 2)

def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=CENTER)
    return rotated_image, new_rect.topleft

running = True
while running:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = 360 * (minutes / 60)
    second_angle = 360 * (seconds / 60)
    
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0)) 

    rotated_minute, min_pos = rotate_hand(right_arm, minute_angle)
    screen.blit(rotated_minute, min_pos)

    rotated_second, sec_pos = rotate_hand(left_arm, second_angle)
    screen.blit(rotated_second, sec_pos)
    
    pygame.display.flip() 
    pygame.time.delay(1000)


