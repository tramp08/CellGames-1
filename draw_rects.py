import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('Blue'))

    clock = pygame.time.Clock()
    running = True
    clock = pygame.time.Clock()
    radius = 0
    v = 10
    fps = 60
    draw = False
    pos = 0, 0
    balls = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball = {}
                ball['pos'] = list(event.pos)
                ball['speed'] = [int(-100 / fps), int(-100 / fps)]
                if event.pos[0] > 10 and event.pos[0] < width - 10 and event.pos[1] > 10 and event.pos[1] < height - 10:
                    balls.append(ball)
        screen.fill(pygame.Color('black'))
        for ball in balls:
            ball['pos'][0] += ball['speed'][0]
            ball['pos'][1] += ball['speed'][1]
            if ball['pos'][0] < 10 or ball['pos'][0] > width - 10:
                ball['speed'][0] = -ball['speed'][0]
            if ball['pos'][1] < 10 or ball['pos'][1] > height - 10:
                ball['speed'][1] = -ball['speed'][1]
            pygame.draw.circle(screen, pygame.Color('white'), ball['pos'], 10)
        clock.tick(fps)
        pygame.display.flip()
