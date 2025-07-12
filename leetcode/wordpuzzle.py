import pygame
import random
import requests

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
gray = (200, 200, 200)
blue = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)
letter_font = pygame.font.Font(None, 72)

# Game variables
clock = pygame.time.Clock()
word_list = requests.get(
    "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt").text.lower().splitlines()
letters = [random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6)]
used_letters = []
free_switch = True
score = 0
input_word = ""
last_word = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, letter in enumerate(letters):
                rect = pygame.Rect(100 + i * 50, 100, 40, 40)
                if rect.collidepoint(event.pos):
                    input_word += letter
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_word = input_word[:-1]
            elif event.key == pygame.K_RETURN:
                if input_word in word_list and (not last_word or input_word[0] == last_word[-1]) and len(input_word) > 2:
                    score += len(input_word)
                    last_word = input_word
                    input_word = ""
                    letters += [random.choice("abcdefghijklmnopqrstuvwxyz")
                                              for _ in range(2)]
                else:
                    print("Invalid word. Try again.")
                    input_word = ""
            elif event.key == pygame.K_s:
                if free_switch:
                    letters = [random.choice(
                        "abcdefghijklmnopqrstuvwxyz") for _ in range(6)]
                    free_switch = False
                else:
                    letters = letters[:-1] + \
                        [random.choice("abcdefghijklmnopqrstuvwxyz")]
        elif event.type == pygame.MOUSEMOTION:
            for i, letter in enumerate(letters):
                rect = pygame.Rect(100 + i * 50, 100, 40, 40)
                if rect.collidepoint(event.pos):
                    # draw red border around hovered letter
                    pygame.draw.rect(screen, (255, 0, 0), rect, 2)

                    screen.fill(white)

                    # Draw letters
                    for i, letter in enumerate(letters):
                        text=letter_font.render(letter, True, blue)
                        screen.blit(text, (100 + i * 50, 100))

                    # Draw input word
                    text=font.render(input_word, True, gray)
                    screen.blit(text, (100, 300))

                    # Draw score
                    text=font.render("Score: " + str(score), True, gray)
                    screen.blit(text, (100, 400))

                    # Draw switch letters button
                    if free_switch:
                        text=font.render("Switch Letters (FREE)", True, gray)
                    else:
                        text=font.render("Switch Letters (-1 letter)", True, gray)
                    screen.blit(text, (500, 500))

                    pygame.display.flip()
                    clock.tick(60)

                pygame.quit()
