import pygame
from PIL import Image

def save_grid_as_image(grid, start, end, filename="grille.png", cell_size=20):
    rows, cols = len(grid), len(grid[0])
    img = Image.new("RGB", (cols * cell_size, rows * cell_size), color=(255, 255, 255))

    pixels = img.load()

    for i in range(rows):
        for j in range(cols):
            color = (255, 255, 255)  # blanc par défaut
            if (i, j) == start:
                color = (255, 0, 0)  # rouge start
            elif (i, j) == end:
                color = (0, 255, 0)  # vert end
            elif grid[i][j] == 1:
                color = (0, 0, 0)  # noir obstacle

            # Remplir la case (cell_size x cell_size pixels)
            for x in range(j*cell_size, (j+1)*cell_size):
                for y in range(i*cell_size, (i+1)*cell_size):
                    pixels[x, y] = color

    img.save(filename)
    print(f"Grille sauvegardée sous '{filename}'")

# Configuration
TAILLE_CASE = 20
LIGNES, COLS = 20, 30
LARGEUR = COLS * TAILLE_CASE
HAUTEUR = LIGNES * TAILLE_CASE

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
GRIS = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Editeur de grille interactif")

# Initialisation grille (0 = libre, 1 = obstacle)
grid = [[0 for _ in range(COLS)] for _ in range(LIGNES)]
start = None
end = None

mode = 'obstacle'  # modes possibles: obstacle, start, end

def draw_grid():
    for i in range(LIGNES):
        for j in range(COLS):
            rect = pygame.Rect(j*TAILLE_CASE, i*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
            if (start == (i,j)):
                pygame.draw.rect(screen, ROUGE, rect)
            elif (end == (i,j)):
                pygame.draw.rect(screen, VERT, rect)
            elif grid[i][j] == 1:
                pygame.draw.rect(screen, NOIR, rect)
            else:
                pygame.draw.rect(screen, BLANC, rect)
            pygame.draw.rect(screen, GRIS, rect, 1)  # grille

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Changer mode avec clavier
            if event.key == pygame.K_o:
                mode = 'obstacle'
                print("Mode : obstacle")
            elif event.key == pygame.K_s:
                mode = 'start'
                print("Mode : start")
            elif event.key == pygame.K_e:
                mode = 'end'
                print("Mode : end")
            elif event.key == pygame.K_p:  # p pour save Picture
                if start is not None and end is not None:
                    save_grid_as_image(grid, start, end)
                else:
                    print("Place start et end avant de sauvegarder.")


        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            j, i = x // TAILLE_CASE, y // TAILLE_CASE

            if mode == 'obstacle':
                grid[i][j] = 1 - grid[i][j]  # toggle obstacle
            elif mode == 'start':
                if start:
                    old_i, old_j = start
                    if (old_i, old_j) != (i, j):
                        grid[old_i][old_j] = 0  # enlever start précédent
                start = (i, j)
                grid[i][j] = 0
            elif mode == 'end':
                if end:
                    old_i, old_j = end
                    if (old_i, old_j) != (i, j):
                        grid[old_i][old_j] = 0
                end = (i, j)
                grid[i][j] = 0

    screen.fill(BLANC)
    draw_grid()
    pygame.display.flip()

pygame.quit()
