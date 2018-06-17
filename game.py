import pygame
while True:
    import pygame

    pygame.init()

    window_w = 800
    window_h = 600

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    FPS = 120

    window = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption("Game: ")
    clock = pygame.time.Clock()


    def game_loop():

        block_size = 10

        velocity = [1, 2, 3, 4]

        pos_x = window_w / 2
        pos_y = window_h / 2

        pos_x1 = 2
        pos_y1 = 2

        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pos_x += velocity[0]
            pos_y += velocity[1]
            pos_x1 += velocity[2]
            pos_y1 += velocity[3]
            if pos_x + block_size > window_w or pos_x < 0:
                velocity[0] = -velocity[0]

            if pos_y + block_size > window_h or pos_y < 0:
                velocity[1] = -velocity[1]

            if pos_x1 + block_size > window_w or pos_x1 < 0:
                velocity[2] = -velocity[2]

            if pos_y1 + block_size > window_h or pos_y1 < 0:
                velocity[3] = -velocity[3]
            # DRAW
            window.fill(white)
            pygame.draw.rect(window, black, [pos_x, pos_y, block_size, block_size])
            pygame.draw.rect(window, red, [pos_x1, pos_y1, block_size, block_size])

            pygame.display.update()
            clock.tick(FPS)


    game_loop()
while  False:
    pygame.init()
    window_w = 800
    window_h = 600
    white = (255, 255, 255)
    black = (0, 0, 0)
    FPS = 120
    window = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption("Game: ")
    clock = pygame.time.Clock()
    def game_loop():
        block_size = 20
        velocity = [1, 1]
        pos_x = window_w/2
        pos_y = window_h/2
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pos_x += velocity[0]
            pos_y += velocity[1]
            if pos_x + block_size > window_w or pos_x < 0:
                velocity[0] = -velocity[0]
            if pos_y + block_size > window_h or pos_y < 0:
                velocity[1] = -velocity[1]
            # DRAW
            window.fill(white)
            pygame.draw.rect(window, black, [pos_x, pos_y, block_size, block_size])
            pygame.display.update()
            clock.tick(FPS)
    game_loop()

