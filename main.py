# import pygame, sys
# # Horse/Knight - +2 and turn
# # Rook = diagonal
# # Pawn - forward and diagonal capture
# # queen - 1 up and 1 down 1 right 1 left and diagonals
# # King - +1 up and down right and left 1 diagonal only
# # castle - straight up or straight side L _|
#
#
# class Piece():
#     def __init__(self, type):
#         pass
#     def move(self):
#         if type == "rook":
#
# class King(pygame.sprite.Sprite):
#     def __init__(self, w,h):
#         super.__init__(self)
#         self.king = pygame.transform.scale(pygame.image.load("king.png"), (100, 100))
#         self.rect = self.king.get_rect()
#
#
# class Main():
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((800, 800))
#         pygame.display.set_caption("Chess")
#         self.snake_block = 100
#         self.run()
#         self.list = pygame.sprite.Group()
#         self.all_sprites = pygame.sprite.Group()
#
#
#     def run(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#             for y in range(0, int(self.screen.get_height())):
#                 for x in range(0, int(self.screen.get_width())):
#                     if (x + y) % 2 == 0:
#                         r = pygame.Rect((x * self.snake_block, y * self.snake_block),
#                                         (self.snake_block, self.snake_block))
#                         pygame.draw.rect(self.screen, (89, 77, 43), r)
#                     else:
#                         rr = pygame.Rect((x * self.snake_block, y * self.snake_block),
#                                          (self.snake_block, self.snake_block))
#                         pygame.draw.rect(self.screen, (232, 210, 149), rr)
#
#             king = King(20,20)
#             self.all_sprites.add(king)
#             pygame.display.update()
#
#
# m = Main()
import  pygame
from engine import *
Width = Height = 512
Dimension = 8
SQ_SIZE = Height // Dimension
FPS = 15
IMAGES = []

def loadimages():
    pieces = ["wR", "wN", "wB","wQ","wK", "wp", "bp", "bQ", "bK", "bB", "bN", "bR"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(piece + ".png"), (SQ_SIZE,SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((512,512))
    pygame.display.set_caption("Chess")
    screen.fill((0,0,0))
    gs = GameState()
    print(gs.board)
    loadimages()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        drawgs(screen,gs)
        # pygame.draw.rect()
        # pygame.display.update()

def drawgs(screen, gs):
    drawboard(screen)
    drawPiece(screen,gs.board)

def drawboard(self,screen):
    pass

def drawPiece(self,screen, list):
    pass


main()