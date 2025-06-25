from PIL import Image, ImageDraw
from heapq import heappush, heappop
import os

def load_grid_from_image_pixels(path):
    img = Image.open(path).convert('RGB')
    width, height = img.size
    data = img.load()

    grid = [[0 for _ in range(width)] for _ in range(height)]
    start = None
    end = None

    for y in range(height):
        for x in range(width):
            r, g, b = data[x, y]

            if (r, g, b) == (255, 0, 0):  # Rouge = Start
                start = (y, x)
                grid[y][x] = 0  # Libre
            elif (r, g, b) == (0, 255, 0):  # Vert = End
                end = (y, x)
                grid[y][x] = 0  # Libre
            elif (r, g, b) == (0, 0, 0):  # Noir = obstacle
                grid[y][x] = 1
            elif (r, g, b) == (255, 255, 255):  # Blanc = libre
                grid[y][x] = 0
            else:
                # Pour d'autres couleurs : considérer comme libre (ou adapte ici si besoin)
                grid[y][x] = 0

    if start is None or end is None:
        raise ValueError("Start (rouge) ou End (vert) non trouvés dans l'image")

    return grid, start, end


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_coords(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    open_set = []
    heappush(open_set, (manhattan(start, end), 0, start))
    came_from = {start: None}
    g_score = {start: 0}
    closed_set = set()

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while open_set:
        _, current_g, current = heappop(open_set)
        if current in closed_set:
            continue
        closed_set.add(current)

        if current == end:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            return path

        row, col = current
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                tentative_g = current_g + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + manhattan(neighbor, end)
                    came_from[neighbor] = current
                    heappush(open_set, (f_score, tentative_g, neighbor))

    return None


def astar_directions(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None

    open_set = []
    heappush(open_set, (manhattan(start, end), 0, start))
    came_from = {start: None}
    g_score = {start: 0}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    dir_names = {
        (-1, 0): "haut",
        (1, 0): "bas",
        (0, -1): "gauche",
        (0, 1): "droite"
    }

    while open_set:
        _, current_g, current = heappop(open_set)

        if current == end:
            path_dirs = []
            node = current
            while came_from[node] is not None:
                prev = came_from[node]
                dr = node[0] - prev[0]
                dc = node[1] - prev[1]
                path_dirs.append(dir_names[(dr, dc)])
                node = prev
            path_dirs.reverse()
            return path_dirs

        row, col = current
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                tentative_g = current_g + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + manhattan(neighbor, end)
                    came_from[neighbor] = current
                    heappush(open_set, (f_score, tentative_g, neighbor))

    return None

def analyze_path_with_obstacle_ahead(grid, start, end):
    path = astar_coords(grid, start, end)
    if not path or len(path) < 2:
        return []  # Aucun chemin ou trop court

    obstacle_ahead_list = []

    for i in range(len(path)-1):
        curr = path[i]
        next_ = path[i+1]
        dr = next_[0] - curr[0]
        dc = next_[1] - curr[1]

        # case suivante dans la même direction
        next_next = (next_[0] + dr, next_[1] + dc)
        if 0 <= next_next[0] < len(grid) and 0 <= next_next[1] < len(grid[0]):
            obstacle_ahead = grid[next_next[0]][next_next[1]] == 1
        else:
            obstacle_ahead = True  # hors grille = considéré comme obstacle

        obstacle_ahead_list.append(obstacle_ahead)

    return obstacle_ahead_list


if __name__ == "__main__":
    # image_path = "grille.png"

    os.chdir('..')
    os.chdir('/pretty-python/PLANS_À_RÉSOUDRE/')
    files = os.listdir()

    if !files :
        raise Exception("The directory is empty.")

    image_path = files[0]



    grid, start, end = load_grid_from_image_pixels(image_path)
    chemin = astar_directions(grid, start, end)

    if chemin:
        print("Chemin trouvé :", chemin)
    else:
        print("Aucun chemin trouvé.")
    analyze_path_with_obstacle_ahead(grid, start, end)

