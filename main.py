import pygame, sys
from model import GameModel
from constants import Constants

WIDTH = Constants.WIDTH
HEIGHT = Constants.HEIGHT
SQUARE = Constants.SQUARE
LINE_WIDTH = Constants.LINE_WIDTH
CIRCLE_COLOR = Constants.CIRCLE_COLOR
CIRCLE_RADIUS = Constants.CIRCLE_RADIUS
CIRCLE_WIDTH = Constants.CIRCLE_WIDTH
SPACE = Constants.SPACE
CROSS_COLOR = Constants.CROSS_COLOR
CROSS_WIDTH = Constants.CROSS_WIDTH
WIN_COLOR = Constants.WIN_COLOR
TEXT_COLOR = Constants.TEXT_COLOR
BG_COLOR = Constants.BG_COLOR
RESTART_BTN = Constants.RESTART_BTN

# setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.Font(None, 40)
button_font = pygame.font.SysFont('arial', 24)

# helper functions
def draw_lines():
    for i in range(1, Constants.BOARD_ROWS):
        for i in range(1, Constants.BOARD_ROWS):
            pygame.draw.line(screen, Constants.LINE_COLOR,
                             (0, i * SQUARE),
                             (WIDTH, i * SQUARE),
                             LINE_WIDTH)
            pygame.draw.line(screen, Constants.LINE_COLOR,
                             (i * SQUARE, 0),
                             (i * SQUARE, Constants.BOARD_HEIGHT),
                             LINE_WIDTH)

def draw_figures(model):
    for r in range(Constants.BOARD_ROWS):
        for c in range(Constants.BOARD_COLS):
            v = model.board[r, c]
            cx, cy = c*Constants.SQUARE + Constants.SQUARE//2, r*SQUARE + SQUARE//2
            if v == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (cx, cy), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif v == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (c*SQUARE+SPACE, r*SQUARE+SQUARE-SPACE),
                                 (c*SQUARE+SQUARE-SPACE, r*SQUARE+SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (c*SQUARE+SPACE, r*SQUARE+SPACE),
                                 (c*SQUARE+SQUARE-SPACE, r*SQUARE+SQUARE-SPACE), CROSS_WIDTH)

def highlight_win(cells):
    start = (cells[0][1]*SQUARE + SQUARE//2, cells[0][0]*SQUARE + SQUARE//2)
    end   = (cells[2][1]*SQUARE + SQUARE//2, cells[2][0]*SQUARE + SQUARE//2)
    pygame.draw.line(screen, WIN_COLOR, start, end, LINE_WIDTH)

def display_message(msg):
    bg_snapshot = screen.copy()
    for size in range(30, 90, 5):
        screen.blit(bg_snapshot, (0, 0))
        zoom_font = pygame.font.Font(None, size)
        text = zoom_font.render(msg, True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(30)
    pygame.time.delay(800)

def restart(model):
    screen.fill(BG_COLOR)
    draw_lines()
    model.__init__()  


model = GameModel()
player = 1
game_over = False
win_cells  = None        
win_text   = None 
screen.fill(BG_COLOR)
draw_lines()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if RESTART_BTN.collidepoint(e.pos):
                restart(model)
                game_over = False
                player = 1
                win_cells = None
                win_text = None
                continue

            if not game_over:
                mx, my = e.pos
                row, col = my // SQUARE, mx // SQUARE
                if model.available_square(row, col):
                    model.mark_square(row, col, player)
                    draw_figures(model)
                    pygame.display.update()
                    pygame.time.delay(150)
                    win, cells = model.check_win(player)
                    if win:
                        game_over = True
                        win_cells = cells
                        win_text  = "Player wins!"
                        display_message(win_text)
                    else:
                        player = 2

        if player == 2 and not game_over:
            model.ai_move()
            draw_figures(model)
            pygame.display.update()
            pygame.time.delay(150)
            win, cells = model.check_win(2)
            if win:
                game_over = True
                win_cells = cells
                win_text  = "AI wins!"
                display_message(win_text)
            else:
                player = 1

    draw_figures(model)
    if game_over and win_cells:
        highlight_win(win_cells)

    toolbar = pygame.Rect(0, Constants.BOARD_HEIGHT, WIDTH, Constants.TOOLBAR_HEIGHT)
    pygame.draw.rect(screen, (40, 40, 40), toolbar)
    pygame.draw.rect(screen, (200, 50, 50), RESTART_BTN)
    lbl = button_font.render("Restart", True, TEXT_COLOR)
    screen.blit(lbl, (RESTART_BTN.x + 5, RESTART_BTN.y + 2))
    pygame.display.update()