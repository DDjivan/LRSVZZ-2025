from flask import Blueprint

from flask import request
from PIL import Image
import os

app_upload = Blueprint('upload', __name__)

# DIRECTORY = 'PLANS_À_RÉSOUDRE'
# app_upload.config['UPLOADS_DIR'] = DIRECTORY

def hex(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def color_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2

def closest_color_of(color):

    PURE_COLORS = [
        (255, 255, 255),  # LIBRE
        (  0,   0,   0),  # OBSTACLE
        hex('#ff0000'), # START
        hex('#00FF00'), # FIN
    ]

    if color in PURE_COLORS:
        return color

    r, g, b = color

    closest_color = min(PURE_COLORS, key=lambda pure_color: color_distance(pure_color, color))

    return closest_color

@app_upload.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image found', 400

    image_file = request.files['image']

    image = Image.open(image_file)

    image = image.convert('RGB')

    new_image = Image.new('RGB', image.size)

    # Color reduction: replace each pixel with the closest pure color
    for x in range(image.width):
        for y in range(image.height):
            original_color = image.getpixel((x, y))
            new_color = closest_color_of(original_color)
            new_image.putpixel((x, y), new_color)

    image_path = os.path.join('PLANS_À_RÉSOUDRE', image_file.filename)

    # name = 1
    # image_path = os.path.join('PLANS_À_RÉSOUDRE', f'{name}.png')
    new_image.save(image_path, format='PNG')

    return 'Image received and saved', 200
