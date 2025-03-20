import pygame

pygame.init()
pygame.display.set_caption("Draw_Circle")
Width = 800
Height = 800
screen = pygame.display.set_mode((Width, Height))
Radius = 25
Ball_speed = 20
ball_x = Width// 2  
ball_y = Height // 2
running = True
while running:
    pygame.time.delay(25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    screen.fill((255,255,255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - Radius - Ball_speed >= 0:
        ball_x -= Ball_speed
    if keys[pygame.K_RIGHT] and ball_x + Radius + Ball_speed <= Width:
        ball_x += Ball_speed
    if keys[pygame.K_UP] and ball_y - Radius - Ball_speed >= 0:
        ball_y -= Ball_speed
    if keys[pygame.K_DOWN] and ball_y + Radius + Ball_speed <= Height:
        ball_y += Ball_speed 
    pygame.draw.circle(screen, (255, 0, 0), (ball_x,ball_y), Radius)
 