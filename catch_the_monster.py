'''
Python collision-based pygame. Draws heroes, monsters, and ghosts on a canvas.
Player moves hero with keyboard with goal of hitting monsters and avoiding
ghouls.
'''
import random

import time

import pygame

HEROSPEED = 5
SAFEBUFFER = 50
#...

# Globally disable pylint false-positive warnings for pygames
# missing methods:
# pylint: disable=E1101

class Hero(object):
    '''
    Defines a Hero character, its starting position, and legal moves
    '''
    spd_x = 0
    spd_y = 0
    def __init__(self, pos_x, pos_y, img):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load(img).convert_alpha()
        self.width = 32
        self.height = 32

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

    def move(self):
        self.pos_x += self.spd_x
        self.pos_y += self.spd_y

    def change_direction(self, width, height):
        if self.pos_x > width - 30:
            self.spd_x = -2
        if self.pos_x < 30:
            self.spd_x = 2
        if self.pos_y < 30:
            self.spd_y = 2
        if self.pos_y > height - 30:
            self.spd_y = -2

    def update_pos(self, width, height):
        '''
        Updates direction of hero character
        '''
        Hero.move(self)
        Hero.change_direction(self, width, height)

class Monster(object):
    '''
    Defines a monster character, its starting positions, and legal moves
    '''

    def __init__(self, pos_x, pos_y, spd_x, spd_y, img):
        '''
        Initialize a monster with position, speed, and an image
        '''

        self.img = pygame.image.load(img).convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.spd_x = spd_x
        self.spd_y = spd_y
        self.last_dir_change = time.time()
        self.width = 32
        self.height = 32

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

    # def setInitialPosition(self, width, height, hero):
    #     min_x = hero_1.pos_x - SAFEBUFFER
    #     min_y = hero_1.pos_y - SAFEBUFFER
    #     max_x = hero_1.pos_x + SAFEBUFFER
    #     max_y = hero_1.pos_y + SAFEBUFFER
    #
    #     safe_x = randint(0, width)
    #     safe_y = randint(0, height)
    #
    #     while safe_x >= min_x and safe_x <= max_x and safe_y >= min_y and safe_y <= max_y:
    #         return True

    def move(self):
        self.pos_x += self.spd_x
        self.pos_y += self.spd_y

    def check_bounds(self, width, height):
        '''
        Move monster to other side of screen if he goes offscreen
        '''
        if self.pos_x > width:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = width
        if self.pos_y > height:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = height

    def change_direction(self):
        new_direction = random.randint(1, 4)
        self.spd_x = 3
        self.spd_y = 3
        if new_direction == 1:
            self.spd_x = 0
            self.spd_y = -1 * self.spd_y
        if new_direction == 2:
            self.spd_y = 0
        if new_direction == 3:
            self.spd_x = 0
        if new_direction == 4:
            self.spd_x = -1 * self.spd_x
            self.spd_y = 0
        self.last_dir_change = time.time()

    def update_pos(self, width, height):
        '''
        Updates the position of the monster. Returns the current
        timer to ensure that direction is only updated every 2
        seconds
        '''
        Monster.move(self)
        Monster.check_bounds(self, width, height)
        if time.time() - self.last_dir_change >= 2:
            Monster.change_direction(self)

class Goblin(object):
    '''
    Defines a goblin character, its starting positions, and legal moves
    '''

    def __init__(self, pos_x, pos_y, spd_x, spd_y, img):
        '''
        Initialize a monster with position, speed, and an image
        '''
        self.img = pygame.image.load(img).convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.spd_x = spd_x
        self.spd_y = spd_y
        self.last_dir_change = time.time()
        self.width = 32
        self.height = 32

    def render(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

    # def setInitialPosition(self, width, height, hero):
    #     min_x = hero_1.pos_x - SAFEBUFFER
    #     min_y = hero_1.pos_y - SAFEBUFFER
    #     max_x = hero_1.pos_x + SAFEBUFFER
    #     max_y = hero_1.pos_y + SAFEBUFFER
    #
    #     safe_x = randint(0, width)
    #     safe_y = randint(0, height)
    #
    #     while safe_x >= min_x and safe_x <= max_x and safe_y >= min_y and safe_y <= max_y:
    #         return True

    def move(self):
        self.pos_x += self.spd_x
        self.pos_y += self.spd_y

    def check_bounds(self, width, height):
        '''
        Move monster to other side of screen if he goes offscreen
        '''
        if self.pos_x > width:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = width
        if self.pos_y > height:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = height

    def change_direction(self):
        new_direction = random.randint(1, 4)
        self.spd_x = 3
        self.spd_y = 3
        if new_direction == 1:
            self.spd_x = 0
            self.spd_y = -1 * self.spd_y
        if new_direction == 2:
            self.spd_y = 0
        if new_direction == 3:
            self.spd_x = 0
        if new_direction == 4:
            self.spd_x = -1 * self.spd_x
            self.spd_y = 0
        self.last_dir_change = time.time()

    def update_pos(self, width, height):
        '''
        Updates the position of the monster. Returns the current
        timer to ensure that direction is only updated every 2
        seconds
        '''
        Goblin.move(self)
        Goblin.check_bounds(self, width, height)
        if time.time() - self.last_dir_change >= 2:
            Goblin.change_direction(self)

def detect_collision(character_1, character_2):
    '''
    Determines if a collision has occured between any two characterss. Returns collision as True or returns nothing.
    '''
    return (character_1.pos_x + character_1.width > character_2.pos_x) and \
    (character_2.pos_x + character_2.width > character_1.pos_x) and (character_1.pos_y + character_1.height > character_2.pos_y)and (character_2.pos_y + character_2.height > character_1.pos_y)

def main():
    '''
    Main function plays the game until the user chooses to quit
    by closing the window.
    '''
    # ----DEFINE CONSTANTS----
    # declare the size of the canvas
    width = 512
    height = 480
    # initialize the pygame framework
    pygame.init() #pylint: disable=E1101
    # load music
    pygame.mixer.init()
    background_music = pygame.mixer.Sound("sounds/music.wav")
    background_music.play()
    win_tone = pygame.mixer.Sound("sounds/win.wav")
    lose_tone = pygame.mixer.Sound("sounds/lose.wav")
    win_tone_played = False
    lose_tone_played = False
    # create screen & set caption
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch The Monster')
    # create a clock to enforce max framerates
    clock = pygame.time.Clock()
    # ----INITIALIZE GAME----
    bkgrnd_img = \
    pygame.image.load('images/background.png').convert_alpha()
    # draw characters
    monster_1 = Monster(30, 30, 0, 3, 'images/monster.png')
    goblin_1 = Monster(30, 30, 0, 2, 'images/goblin.png')
    hero_1 = Hero(256, 220, 'images/hero.png')
    # game loop
    stop_game = False
    game_won = False
    game_lost = False
    level = 0
    while not stop_game:
        # ----EVENT HANDLING CODE----
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #pylint: disable=E1101
                # Move hero according to arrow key pressed
                if event.key == pygame.K_DOWN:
                    hero_1.spd_x = 0
                    hero_1.spd_y = 2
                elif event.key == pygame.K_UP:
                    hero_1.spd_x = 0
                    hero_1.spd_y = -2
                elif event.key == pygame.K_RIGHT:
                    hero_1.spd_x = 2
                    hero_1.spd_y = 0
                elif event.key == pygame.K_LEFT:
                    hero_1.spd_x = -2
                    hero_1.spd_y = 0
                # Reset game state on press of return key
                elif event.key == pygame.K_RETURN:
                    game_won = False
                    game_lost = False
                    win_tone_played = False
                    lose_tone_played = False
                    background_music.play()
                    monster_1.pos_x = random.randint(0, width)
                    monster_1.pos_y = random.randint(0, height)
                    goblin_1.pos_x = random.randint(0, width)
                    goblin_1.pos_y = random.randint(0, height)
            # If user closes window, quite game
            if event.type == pygame.QUIT: #pylint: disable=E1101
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True
        # ----UPDATE GAME STATE----
        # detect collision between hero and monster
        if detect_collision(hero_1, monster_1):
            game_won = True
            hero_1.spd_x, hero_1.spd_y = 0, 0
            monster_1.spd_x, monster_1.spd_y = 0, 0
            goblin_1.spd_x, goblin_1.spd_y = 0, 0
            level += 1
        # detect collision between hero and goblins
        elif detect_collision(hero_1, goblin_1):
            game_lost = True
            level = 1
        # if no collisions, update positions as normal
        else:
            hero_1.update_pos(width, height)
            monster_1.update_pos(width, height)
            goblin_1.update_pos(width, height)
        # ----CUSTOM DISPLAY CODE----
        # Always draw background first
        screen.blit(bkgrnd_img, (0, 0))
        # If game over, swap music and display text hint to user
        if game_won or game_lost:
            background_music.stop()
            if game_won:
                if not win_tone_played:
                    win_tone.play()
                    win_tone_played = True
            if game_lost:
                if not lose_tone_played:
                    lose_tone.play()
                    lose_tone_played = True
            font = pygame.font.Font(None, 25)
            text = font.render('Hit Enter to play again', True, (0, 0, 0))
            screen.blit(text, (170, 220))
        # draw hero until game is lost
        if not game_lost:
            hero_1.render(screen)
        # Draw monsters / goblins until game is won
        if not game_won:
            monster_1.render(screen)
            goblin_1.render(screen)
        pygame.display.update()
        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit() #pylint: disable=E1101

if __name__ == '__main__':
    main()
