import pygame
import random
import time

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Hero(object):
    '''
    Defines a Hero character, its starting position, and legal moves
    '''
    def __init__(self, pos_x, pos_y, spd_x, spd_y, img):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.spd_x = spd_x
        self.spd_y = spd_y
        self.img = pygame.image.load(img).convert_alpha()

    def update_pos(self):
        '''
        Updates direction of hero character
        '''
        self.pos_x += self.spd_x
        self.pos_y += self.spd_y
        if self.pos_x > 450:
            self.spd_x = -2
        if self.pos_x < 30:
            self.spd_x = 2
        if self.pos_y < 30:
            self.spd_y = 2
        if self.pos_y > 420:
            self.spd_y = -2

    def register_keypress(self, event_key):
        '''
        Event handler for Hero character. Changes movement
        direction according to keypress.
        '''
        if event_key == KEY_DOWN:
            self.spd_x = 0
            self.spd_y = +2
        elif event_key == KEY_UP:
            self.spd_x = 0
            self.spd_y = -2
        elif event_key == KEY_RIGHT:
            self.spd_x = 2
            self.spd_y = 0
        elif event_key == KEY_LEFT:
            self.spd_x = -2
            self.spd_y = 0

class Monster(object):
    '''
    Defines a monster character, its starting positions, and legal moves
    '''
    def __init__(self, pos_x, pos_y, spd_x, spd_y, img):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.spd_x = spd_x
        self.spd_y = spd_y
        self.img = pygame.image.load(img).convert_alpha()

    def update_pos(self, width, height, timer):
        '''
        Updates the position of the monster. Returns the current
        timer to ensure that direction is only updated every 2
        seconds
        '''
        self.pos_x += self.spd_x
        self.pos_y += self.spd_y
        if time.time() - timer >= 2:
            new_direction = random.randint(1, 4)
            print "New Direction: %s" % new_direction
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
            print "Monster speed x: %s" % self.spd_x
            print "Monster speed y: %s" % self.spd_y
            timer = time.time()
        if self.pos_x > width:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = 512
        if self.pos_y > height:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = 480
        return timer

def main():
    # DEFINE CONSTANTS
    # declare the size of the canvas
    width = 512
    height = 480
    # initialize the pygame framework
    pygame.init() #pylint: disable=E1101
    # load sounds
    win_tone = pygame.mixer.Sound("sounds/win.wav")
    win_tone_played = 0
    pygame.mixer.init()
    # create screen
    screen = pygame.display.set_mode((width, height))
    # set window caption
    pygame.display.set_caption('Catch The Monster')
    # create a clock
    clock = pygame.time.Clock()
    # INITIALIZE GAME
    bkgrnd_img = \
    pygame.image.load('images/background.png').convert_alpha()
    monster_1 = Monster(30, 30, 0, 3, 'images/monster.png')
    hero_1 = Hero(256, 220, 0, 0, 'images/hero.png')
    direction_timer = time.time()
    # game loop
    stop_game = False
    collision = False
    testing = 0
    while not stop_game:
        # RESET GAME IF COLLISION DETECTED
        if collision:
            # stop moving hero
            hero_1.spd_x, hero_1.spd_y = 0, 0
            # create message to ask if want to play again
            font = pygame.font.Font(None, 25)
            text = font.render('Hit Enter to play again', True, (0, 0, 0))
            # draw items onto screen
            screen.blit(bkgrnd_img, (0, 0))
            screen.blit(text, (200, 220))
            screen.blit(hero_1.img, (hero_1.pos_x, hero_1.pos_y))
            pygame.display.update()
            # Play win tone...just once
            if win_tone_played == 0:
                win_tone.play()
                win_tone_played = 1
            if testing == 1:
                print "testing..."
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        collision = False
                        print "collision: %s" % collision
                        win_tone_played = 0
                        testing = 1
                if event.type == pygame.QUIT: #pylint: disable=E1101
                    # if they closed the window, set stop_game to True
                    # to exit the main loop
                    stop_game = True
        # PLAY GAME UNTIL COLLISION OR QUIT
        else:
            # EVENT HANDLING CODE
            # Reset win tone
            win_tone_played = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: #pylint: disable=E1101
                    hero_1.register_keypress(event.key)
                if event.type == pygame.QUIT: #pylint: disable=E1101
                    # if they closed the window, set stop_game to True
                    # to exit the main loop
                    stop_game = True
            # UPDATE GAME STATE
            hero_1.update_pos()
            direction_timer = monster_1.update_pos(width, height, direction_timer)
            # Detect collision
            if not hero_1.pos_x + 32 < monster_1.pos_x \
            and not monster_1.pos_x + 32 < hero_1.pos_x \
            and not hero_1.pos_y + 32 < monster_1.pos_y \
            and not monster_1.pos_y + 32 < hero_1.pos_y:
                collision = True
            # CUSTOM DISPLAY CODE
            screen.blit(bkgrnd_img, (0, 0))
            screen.blit(hero_1.img, (hero_1.pos_x, hero_1.pos_y))
            screen.blit(monster_1.img, (monster_1.pos_x, monster_1.pos_y))
            pygame.display.update()
            # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit() #pylint: disable=E1101

if __name__ == '__main__':
    main()
