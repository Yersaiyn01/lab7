import pygame
import sys
from datetime import datetime
DARK = (160,160,160)
WHITE = (255,255,255)
pygame.init()
SIZE = 400
CENTER = (SIZE // 2 +50, SIZE // 2+75)
window = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()
class Button:
    def __init__(self, x, y, width, height, text, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.color = (200, 200, 200)  
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
def draw_minute_hand(surface, minute):
    hand_length = SIZE * 0.3  
    angle = minute * 6  
    end_x = CENTER[0] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = CENTER[1] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).y
    pygame.draw.line(surface, DARK, CENTER, (end_x, end_y), 5)

def draw_second_hand(surface, second):
    hand_length = SIZE * 0.4  
    angle = second * 6

    end_x = CENTER[0] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).x
    end_y = CENTER[1] + hand_length * pygame.math.Vector2(0, -1).rotate(angle).y

    pygame.draw.line(surface, DARK, CENTER, (end_x, end_y), 3)
def run():
    pygame.init()
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Test Gaming")
   
    background = pygame.image.load("/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/lab6_zh/il_570xN.1493090144_kbdv.jpg.webp")  
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  

    pygame.mixer.init()
    pygame.mixer.music.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/lab6_zh/grm1.mp3')   
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  
    running = True
    music_paused = False
    button = Button(x=SCREEN_WIDTH // 2 - 75, y=20, width=150, height=50, text='PAUSE')
    while running:
        screen.blit(background,(0,0))
        now=datetime.now()
        draw_minute_hand(screen, now.minute)
        draw_second_hand(screen, now.second)

        button.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button.is_clicked(event):
                if music_paused:
                    pygame.mixer.music.unpause()
                    button.text = 'PAUSE'
                else:
                    pygame.mixer.music.pause()
                    button.text = 'UNPAUSE'
                music_paused = not music_paused
        button.draw(screen)
        pygame.display.flip()

run()
