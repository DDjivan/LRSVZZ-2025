from moteur_args import *
from testFeed import *
from rechercheChemin import *

if __name__ == "__main__":
    image_path = "grille.png"  # image d'entrée
    block_size = 20

    grid, start, end = load_grid_from_image_blocks(image_path, block_size=block_size)
    chemin = astar_directions(grid, start, end)
