import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 50

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    ball = Ball(250, 250)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        ball.update()

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        #,###############################
        ball.render(screen)
        font = pygame.font.Font(None, 25)
        text = font.render('Use arrow keys to move the ball smoothly', True, (0, 0, 0))
        screen.blit(text, (80, 230))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
