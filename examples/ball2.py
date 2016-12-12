import pygame

class Ball(object):
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

    def update(self, width, height):
        self.x += self.speed
        self.y += self.speed
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0

    def display(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    ball_list = [
        Ball(50, 50, 5, 50),
        Ball(300, 200, 8, 30),
        Ball(100, 300, 12, 60),
        Ball(200, 200, 2, 40)
    ]

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Ball Example')

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        for ball in ball_list:
            ball.update(width, height)

        # fill background color
        screen.fill(blue_color)
        for ball in ball_list:
            ball.display(screen)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # update the canvas display with the currently drawn frame
        pygame.display.update()

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
