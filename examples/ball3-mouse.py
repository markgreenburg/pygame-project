import pygame

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = 50

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radius > width:
            self.speed_x = -5
        if self.y + self.radius > height:
            self.speed_y = -5
        if self.x - self.radius < 0:
            self.speed_x = 5
        if self.y - self.radius < 0:
            self.speed_y = 5

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
    ball_list = [
        Ball(50, 50)
    ]

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                ball_list.append(Ball(x, y))
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

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        #,###############################
        for ball in ball_list:
            ball.render(screen)

        font = pygame.font.Font(None, 25)
        text = font.render('Click to add a ball', True, (0, 0, 0))
        screen.blit(text, (80, 230))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
