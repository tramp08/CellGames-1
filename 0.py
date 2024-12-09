import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                color = pygame.Color('white')
                pygame.draw.rect(screen, color,
                                 ((self.left + j * self.cell_size, self.top + i * self.cell_size),
                                  ( self.cell_size,  self.cell_size)), width=1)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()