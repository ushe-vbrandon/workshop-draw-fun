"""
Draw

Render a draw fun sql image.
"""

import logging
from PIL import Image

logger = logging.getLogger(__name__)



scale_size = (256, 256)
logger.info(f'Scale size: {scale_size}')


def draw_complete_image(images: list, output_path: str = 'draw_fun.jpg') -> Image:
    """Draw complete image."""
    # scale each image
    [im.thumbnail(scale_size) for im in images]

    # create new image
    new_image = Image.new('RGB', (len(images)*scale_size[0], scale_size[1]), (250,250,250))

    # paste each image
    for pos, image in enumerate(images):
        new_image.paste(image, (pos * scale_size[0], 0))

    # save image
    new_image.save(output_path)

    return new_image