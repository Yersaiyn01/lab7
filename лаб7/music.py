import pygame
import os
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)
music_folder = '/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/музыка'
background = pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/музыка сурет/images.jpeg')
background = pygame.transform.scale(background, (750, 500))
button_images = { 
    "Play": pygame.transform.scale(pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/музыка сурет/play.png'), (50, 50)),
    "Next": pygame.transform.scale(pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/музыка сурет/next.png'), (50, 50)),
    "Pause": pygame.transform.scale(pygame.image.load('/Users/ersaiynmaralbekuly/Desktop/semester2/pp2/лаб7/музыка сурет/pause.png'), (50, 50))
}
button_positions = {
    "Pause": (245, 400),
    "Play": (345, 400),
    "Next": (445, 400),
}
musics = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0
if not musics:
    print("No MP3 files found in the directory.")
    pygame.quit()
    exit()
def draw_interface():
    screen.fill((255, 255, 255)) 
    screen.blit(background, (0, 0))  
    track_name = musics[current_track]
    text_surface = font.render(track_name, True, (30, 30, 30))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))
    screen.blit(text_surface, text_rect)
    for text, pos in button_positions.items():
        screen.blit(button_images[text], pos)
    pygame.display.flip()
def play_music():
    """Plays the current track."""
    track_path = os.path.join(music_folder, musics[current_track])
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()
    draw_interface()
running = True
draw_interface()  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(musics)
                play_music()
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(musics)
                play_music()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for button, pos in button_positions.items():
                bx, by = pos
                if bx <= mouse_x <= bx + 50 and by <= mouse_y <= by + 50:
                    if button == "Play":
                        play_music()
                    elif button == "Pause":
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    elif button == "Next":
                        current_track = (current_track + 1) % len(musics)
                        play_music()
