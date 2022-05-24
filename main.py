import pygame

pygame.init()
player_cards = []
ai1_cards = []
ai2_cards = []
ai3_cards = []

title_screen = 1
volume_int = 50
# lists
size = [900, 900]
white = [255, 255, 255]
black = [0, 0, 0]
# config
screen = pygame.display.set_mode()
sprites = pygame.sprite.Group()
pygame.display.set_caption("Mistahs Casino & Card Games")
running = True
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.display.toggle_fullscreen()
# font stuff
font = pygame.font.Font('rg.ttf', 25)
title = font.render('mistahs casino and card games', True, black, white)
start = font.render('start', True, black, white)
options = font.render('Options', True, black, white)
quit = font.render('Quit', True, black, white)
games = font.render("Games", True, black, white)
bj = font.render("Black Jack", True, black, white)
games_quit = font.render("Return to title screen", True, black, white)
poker = font.render("Poker", True, black, white)
volume = font.render("Volume", True, black, white)
plus = font.render("+", True, black, white)
minus = font.render("-", True, black, white)
volume_dis = font.render(str(volume_int), True, black, white)
options_back = font.render("Back to title", True, black, white)

options_back_rect = options_back.get_rect()
volume_int_rect = volume_dis.get_rect()
volume_rect = volume.get_rect()
games_quit_rect = games_quit.get_rect()
bj_rect = bj.get_rect()
games_rect = games.get_rect()
quit_rect = quit.get_rect()
start_rect = start.get_rect()
title_rect = title.get_rect()
options_rect = options.get_rect()
poker_rect = poker.get_rect()
plus_rect = plus.get_rect()
minus_rect = minus.get_rect()
# title screen
options_rect.center = (500, 300)
start_rect.center = (500, 250)
title_rect.center = (500, 200)
quit_rect.center = (500, 350)
# games menu
games_rect.center = (100000, 100000)
bj_rect.center = (100000, 100000)
games_quit_rect.center = (100000, 1000000)
poker_rect.center = (100000, 100000)
# options menu
volume_rect.center = (100000, 100000)
plus_rect.center = (100000, 100000)
minus_rect.center = (100000, 100000)
volume_int_rect.center = (100000, 100000)
options_back_rect.center = (100000, 100000)


def load_title():
    options_rect.center = (500, 300)
    start_rect.center = (500, 250)
    title_rect.center = (500, 200)
    quit_rect.center = (500, 350)


def clear_title():
    title_rect.center = (100000, 100000)
    start_rect.center = (100000, 100000)
    title_rect.center = (100000, 100000)
    quit_rect.center = (100000, 100000)
    options_rect.center = (100000, 100000)


def load_games():
    games_rect.center = (500, 50)
    bj_rect.center = (500, 200)
    poker_rect.center = (350, 200)
    games_quit_rect.center = (200, 50)


def clear_games():
    games_rect.center = (100000, 100000)
    bj_rect.center = (100000, 100000)
    games_quit_rect.center = (1000000, 100000)


def options_load():
    options_rect.center = (500, 200)
    volume_rect.center = (500, 300)
    volume_int_rect.center = (500, 325)
    plus_rect.center = (575, 325)
    minus_rect.center = (425, 325)
    options_back_rect.center = (100, 100)


def options_clear():
    options_rect.center = (1000000, 100000)
    volume_rect.center = (1000000, 100000)
    volume_int_rect.center = (1000000, 100000)
    plus_rect.center = (1000000, 100000)
    minus_rect.center = (1000000, 100000)
    options_back_rect.center = (1000000, 100000)


def load_black_jack():
    pass


while running:
    volume_dis = font.render(str(volume_int), True, black, white)
    pos = pygame.mouse.get_pos()
    screen.fill(white)
    sprites.update()
    sprites.draw(screen)
    clock.tick(50)
    screen.blit(title, title_rect)
    screen.blit(start, start_rect)
    screen.blit(options, options_rect)
    screen.blit(quit, quit_rect)
    screen.blit(games, games_rect)
    screen.blit(bj, bj_rect)
    screen.blit(games_quit, games_quit_rect)
    screen.blit(poker, poker_rect)
    screen.blit(volume, volume_rect)
    screen.blit(minus, minus_rect)
    screen.blit(plus, plus_rect)
    screen.blit(options_back, options_back_rect)
    screen.blit(volume_dis, volume_int_rect)

    x = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            print(x)
            # title screen
            if start_rect.collidepoint(x):
                clear_title()
                load_games()
            if quit_rect.collidepoint(x):
                pygame.quit()
            if games_quit_rect.collidepoint(x):
                clear_games()
                load_title()
            if options_rect.collidepoint(x):
                options_load()
                clear_title()
            # options
            if minus_rect.collidepoint(x) and volume_int > 0:
                volume_int = volume_int - 1
                volume_dis = font.render(str(volume_int), True, black, white)
            if plus_rect.collidepoint(x) and volume_int < 100:
                volume_int = volume_int + 1
                volume_dis = font.render(str(volume_int), True, black, white)
            if options_back_rect.collidepoint(x):
                options_clear()
                load_title()
    pygame.display.flip()

