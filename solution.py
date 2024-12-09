from pprint import pprint
import sys
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
        for i in range(len(self.board[0])):
            for j in range(len(self.board)):
                color = pygame.Color('white')
                rect = self.left + i * self.cell_size, self.top + j * self.cell_size, self.cell_size, self.cell_size
                pygame.draw.rect(screen, color, rect, 1)

                if self.board[j][i] == 0:
                    color = pygame.Color('black')

                pygame.draw.rect(screen, color, (rect[0] + 1, rect[1] + 1, rect[2] - 2, rect[3] - 2), 0)


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if (self.left + len(self.board[0]) * self.cell_size < x or x < self.left
                or self.top + len(self.board) * self.cell_size < y or y < self.top):
            return None
        else:
            return ((x - self.left) // self.cell_size, (y - self.top) // self.cell_size)

    def on_click(self, cell):
        if cell:
            x, y = cell
            self.board[y][x] = 1 - self.board[y][x]
            # pprint(self.board)




def main():
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    sys.exit(main())
