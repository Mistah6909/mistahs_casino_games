import pygame
import random
import platform
import os
import sys
os1 = platform.system()

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
card_ints = []
pygame.init()
player_cards = []
player_val = 0
ai1_cards = []
ai2_cards = []
ai3_cards = []
blackjack_run = False
bj_dealer_turn = False
bj_player_turn = False
music_volume_int = 50
sfx_volume_int = 50
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
#game over screen
game_over = font.render('Game Over!',True,black,white)
blackjack_bust_text = font.render("You busted!",True,black,white)
blackjack_lose_text = font.render("You lost!", True,black,white)
play_again = font.render("play again",True,black,white)
back_to_main = font.render("Back to menu",True,black,white)
#title stuff
title = font.render('mistahs casino and card games', True, black, white)
start = font.render('start', True, black, white)
options = font.render('Options', True, black, white)
quit = font.render('Quit', True, black, white)
games = font.render("Games", True, black, white)
#games
bj = font.render("Black Jack", True, black, white)
games_quit = font.render("Return to title screen", True, black, white)
poker = font.render("Poker", True, black, white)
music_volume = font.render("Music Volume", True, black, white)
plus = font.render("+", True, black, white)
minus = font.render("-", True, black, white)
#options
volume_dis = font.render(str(music_volume_int), True, black, white)
options_back = font.render("Back to title", True, black, white)
sfx_volume = font.render("SFX Volume", True, black, white)
sfx_volume_dis = font.render(str(sfx_volume_int), True, white, black)
sfx_minus = font.render("-", True, black, white)
sfx_plus = font.render("+", True, black, white)
#blackjack'
bj_back = font.render("Back to main menu",True,white,black)
player_hit = font.render("hit",True,black,white)
player_hold = font.render("hold",True,black,white)
player_value_dis = font.render(str(player_val),True,black,white)
#game_over_
#blackjack
bj_back_rect = bj_back.get_rect()
player_hit_rect = player_hit.get_rect()
player_hold_rect = player_hold.get_rect()
player_value_dis_rect = player_value_dis.get_rect()
#options rects
options_back_rect = options_back.get_rect()
volume_int_rect = volume_dis.get_rect()
music_volume_rect = music_volume.get_rect()

#game rects
games_quit_rect = games_quit.get_rect()
bj_rect = bj.get_rect()
poker_rect = poker.get_rect()

#title_rects
games_rect = games.get_rect()
quit_rect = quit.get_rect()
start_rect = start.get_rect()
title_rect = title.get_rect()
options_rect = options.get_rect()
plus_rect = plus.get_rect()
minus_rect = minus.get_rect()
sfx_volume_rect = sfx_volume.get_rect()
sfx_minus_rect = sfx_minus.get_rect()
sfx_plus_rect = sfx_plus.get_rect()
#black jack
player_hold_rect.center = (100000,100000)
player_hit_rect.center = (100000,100000)
player_value_dis_rect.center = (100000,100000)
bj_back_rect.center = (100000,100000)
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
sfx_volume_rect.center = (100000, 100000)
sfx_minus_rect.center = (100000, 100000)
sfx_plus_rect.center = (100000, 100000)
music_volume_rect.center = (100000, 100000)
plus_rect.center = (100000, 100000)
minus_rect.center = (100000, 100000)
volume_int_rect.center = (100000, 100000)
options_back_rect.center = (100000, 100000)
def install():
  os1 = platform.system()
  #these if statements check to see what os is running since shell command syntax is dependent on OS
  if pygame in sys.modules :
    pass
  else:
    os.system('cmd /k pip install requirements.txt')
def load_game_over():
    game_over.center = ()
def clear_all():
    title_rect.center = (100000, 100000)
    start_rect.center = (100000, 100000)
    title_rect.center = (100000, 100000)
    quit_rect.center = (100000, 100000)
    options_rect.center = (100000, 100000)
    games_rect.center = (100000, 100000)
    bj_rect.center = (100000, 100000)
    games_quit_rect.center = (1000000, 100000)
    poker_rect.center = (100000, 100000)
    player_hit_rect.center = (100000,100000)
    player_hold_rect.center = (100000,100000)



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
    poker_rect.center = (100000, 100000)


def options_load():
    options_rect.center = (500, 200)
    music_volume_rect.center = (500, 300)
    volume_int_rect.center = (500, 325)
    plus_rect.center = (575, 325)
    minus_rect.center = (425, 325)
    options_back_rect.center = (100, 100)
    sfx_volume_rect.center = (500,350)


def options_clear():
    options_rect.center = (1000000, 100000)
    music_volume_rect.center = (1000000, 100000)
    volume_int_rect.center = (1000000, 100000)
    plus_rect.center = (1000000, 100000)
    minus_rect.center = (1000000, 100000)
    options_back_rect.center = (1000000, 100000)


def blackjack_load():
    player_hit_rect.center = (500,600)
    player_hold_rect.center = (600,600)
    player_value_dis_rect.center = (550,700)
    games_quit_rect.center = (46, 41)
    bj_back_rect.center = (50,40)




def clear_black_jack():
    player_hit_rect.center = (100000,100000)
    player_hold_rect.center = (100000,100000)
    player_value_dis_rect.center = (100000,100000)

while running:

    volume_dis = font.render(str(music_volume_int), True, black, white)
    sfx_volume_dis = font.render(str(sfx_volume_int), True, white, black)
    player_value_dis = font.render(str(player_val), True, black, white)
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
    screen.blit(music_volume, music_volume_rect)
    screen.blit(minus, minus_rect)
    screen.blit(plus, plus_rect)
    screen.blit(options_back, options_back_rect)
    screen.blit(volume_dis, volume_int_rect)
    screen.blit(player_hold,player_hold_rect)
    screen.blit(player_hit,player_hit_rect)
    screen.blit(player_value_dis,player_value_dis_rect)
    screen.blit(bj_back,bj_back_rect)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            print(mouse_pos)
            # title screen
            if bj_back_rect.collidepoint(mouse_pos):
                clear_black_jack()
                load_title()
            if start_rect.collidepoint(mouse_pos):
                clear_title()
                load_games()
            if quit_rect.collidepoint(mouse_pos):
                pygame.quit()
            if games_quit_rect.collidepoint(mouse_pos):
                clear_games()
                load_title()
            if options_rect.collidepoint(mouse_pos):
                options_load()
                clear_title()
            # options
            if minus_rect.collidepoint(mouse_pos) and music_volume_int > 0:
                music_volume_int = music_volume_int - 1
                volume_dis = font.render(str(music_volume_int), True, black, white)
            if plus_rect.collidepoint(mouse_pos) and music_volume_int < 100:
                music_volume_int = music_volume_int + 1
                volume_dis = font.render(str(music_volume_int), True, black, white)
            if sfx_minus_rect.collidepoint(mouse_pos):
                sfx_volume_int = sfx_volume_int - 1
                volume_dis = font.render(str(sfx_volume_int), True, black, white)
            if sfx_plus_rect.collidepoint(mouse_pos):
                volume_dis = font.render(str(sfx_volume_int), True, black, white)
                sfx_volume_int = sfx_volume_int + 1
            if options_back_rect.collidepoint(mouse_pos):
                options_clear()
                load_title()
            #games menu
            if bj_rect.collidepoint(mouse_pos):
                blackjack_load()
                clear_games()
                blackjack_run = True
                bj_player_turn = True
                print(blackjack_run)
                print(bj_player_turn)
            if player_hit_rect.collidepoint(mouse_pos) and blackjack_run == True:
                player_cards.append(random.choice(cards))
                player_val = 0
                for x in player_cards:
                    if x == "K":
                        player_val = player_val + 13
                    if x == "Q":
                        player_val = player_val + 12
                    if x == "J":
                        player_val = player_val + 11
                    if x == "A" and player_val < 21:
                        player_val = player_val + 1
                    if x != "K" and "Q" and "J" and "A" :
                        player_val = player_val + x
                    elif x == "A" and player_val < 21:
                        player_val = player_val + 1
                    if player_val > 21:
                        pass

            if player_hold_rect.collidepoint(mouse_pos) and blackjack_run == True:
                pass


    pygame.display.flip()
