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


def start_screen():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Chess")
    bg = pygame.transform.scale(pygame.image.load("bkg.png"),(512,512))
    screen.blit(bg, (0,0))
    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    main()
        clock.tick(FPS)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Chess")
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    gs = GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #Flag

    loadimages()
    running = True
    sqselected = ()
    playerClicks = []
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gs.undoMove()
                    moveMade = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqselected == (row, col):
                    sqselected = ()
                    playerClicks = []
                else:
                    sqselected = (row, col)
                    playerClicks.append(sqselected)
                if len(playerClicks) == 2:
                    move = Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqselected = ()
                        playerClicks = []
                    else:
                        playerClicks = [sqselected]

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
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



# main()
start_screen()