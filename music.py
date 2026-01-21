import pygame
import sys
import time
import random

pygame.init()

WIDTH, HEIGHT = 820, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerua Made by Amlan Dey")

FONT = pygame.font.SysFont("Georgia", 40, bold=True)
colors = [
  
    (30, 30, 60),    # dark navy / midnight blue
    (50, 50, 80),    # muted indigo
    (80, 80, 100),   # grayish blue
    (60, 40, 50),    # desaturated burgundy / deep maroon
    (70, 90, 100),   # muted teal / stormy color
    (40, 40, 40)     # dark gray / almost black
]


lyrics = [
        "Duniya Bhula ke..",
        "Tumse mila hun..",
        "Nikli haa dil se ye duaaa..<3",
        "Rang de tu mohe...Geruaan",
        "Radhe ki dil se ha duaan",
        "Rang de tu mohe...Geruaan<3"
    ]

def typewriter_text(text, color, bg_color, char_delay=0.1, duration=1.1):
    current_text = ""
    for char in text:
        current_text += char
        text_surface = FONT.render(current_text, True, color)
        text_surface = text_surface.convert_alpha()
        rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        screen.fill(bg_color)           # clear screen to bg
        screen.blit(text_surface, rect) # draw current text
        pygame.display.flip()           # update screen
        time.sleep(char_delay)          # wait for next char
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    # Hold the full line
    time.sleep(duration)


    for alpha in range(255, -1, -5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, rect)
        pygame.display.flip()
        time.sleep(0.02)

durations = [0.9, 0.9, 2.2, 2.5, 2.8, 3.5]

for i, line in enumerate(lyrics):
    bg = random.choice(colors)
    typewriter_text(line, (255, 255, 255), bg, char_delay=0.09, duration=durations[i])

pygame.quit()
