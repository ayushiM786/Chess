# import pygame, sys
# # Horse/Knight - +2 and turn
# # Rook = diagonal
# # Pawn - forward and diagonal capture
# # queen - 1 up and 1 down 1 right 1 left and diagonals
# # King - +1 up and down right and left 1 diagonal only
# # castle - straight up or straight side L _|

import pygame
from engine import *
Width = Height = 512
Dimension = 8
SQ_SIZE = Height // Dimension
FPS = 15
IMAGES = {}

def loadimages():
    pieces = ["wR", "wN", "wB","wQ","wK", "wp", "bp", "bQ", "bK", "bB", "bN", "bR"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(piece + ".png"), (SQ_SIZE,SQ_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Chess")
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    gs = GameState()
    loadimages()
    running = True
    sqselected = ()
    playerClicks = []
    while running:
        print("save me " + "test charge")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqselected == (row,col):
                    sqselected = ()
                    playerClicks = []
                else:
                    sqselected = (row, col)
                    playerClicks.append(sqselected)
                if len(playerClicks) == 2:
                    pass


        clock.tick(FPS)
        pygame.display.flip()
        drawGameState(screen,gs)
        # pygame.draw.rect()
        # pygame.display.update()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)

def drawBoard(screen):
    colors = [(89, 77, 43),(232, 210, 149)]
    for r in range(Dimension):
        for c in range(Dimension):
            color = colors[((r+c)%2)]
            pygame.draw.rect(screen, color,pygame.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


def drawPieces(screen, board):
    for r in range(Dimension):
        for c in range(Dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



main()