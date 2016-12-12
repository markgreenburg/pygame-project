import pygame

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()
    # create screen
    screen = pygame.display.set_mode((width, height))
    # set window caption
    pygame.display.set_caption('Simple Example')

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    hero_image = pygame.image.load('images/hero.png').convert_alpha()

    # create a clock
    clock = pygame.time.Clock()

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

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(hero_image, (250, 250))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
