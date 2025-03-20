import pygame
from datetime import datetime
DARK_GREY = (160, 160, 160)
WHITE = (255, 255, 255)
pygame.init()
SIZE = 400
CENTER = (SIZE // 2, SIZE // 2)
window = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()

def draw_minute_hand(surface, minute):
    hand_length = SIZE * 0.3  
    angle = minute * 6  
    end_x = CENTER[0] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = CENTER[1] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).y
    pygame.draw.line(surface, DARK_GREY, CENTER, (end_x, end_y), 5)

def draw_second_hand(surface, second):
    hand_length = SIZE * 0.4  
    angle = second * 72 

    end_x = CENTER[0] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = CENTER[1] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).y

    pygame.draw.line(surface, DARK_GREY, CENTER, (end_x, end_y), 3)

def main():
    running = True
    while running:
        window.fill(WHITE)  
        now = datetime.now()
        draw_minute_hand(window, now.minute)
        draw_second_hand(window, now.second)
        pygame.display.flip()
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
main()
