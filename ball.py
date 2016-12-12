import pygame

class Ball(object):
    def __init__(self, x_coord, y_coord, speed, radius):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed_x = speed
        self.speed_y = speed
        self.radius = radius
    def update(self, width, height):
        self.x_coord += self.speed_x
        self.y_coord += self.speed_y
        # fill background color
        if self.x_coord + self.radius > width or self.x_coord - self.radius < 0:
            self.speed_x = self.speed_x * -1
        if self.y_coord + self.radius > height or self.y_coord - self.radius < 0:
            self.speed_y = self.speed_y * -1
    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x_coord, self.y_coord), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init() #pylint: disable=E1101

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    balls = [
        Ball(50, 50, 25, 50),
        Ball(100, 200, 12, 20),
        Ball(50, 50, 30, 50),
        Ball(20, 200, 20, 20),
        Ball(100, 4, 25, 50),
        Ball(100, 200, 18, 20)
        ]

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT: #pylint: disable=E1101
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        for ball in balls:
            ball.update(width, height)

        screen.fill(blue_color)
        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in balls:
            ball.render(screen)
        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
