# query_images.py


import os
import numpy as np
import pandas as pd
from PIL import Image
from typing import List

from database import query_db


def collect_queries(path: os.PathLike) -> List[str]:
    """Collects all query files in a given directory.

    Args:
        path (os.PathLike): Path to directory containing query files.

    Returns:
        List[str]: List of query strings from files.
    """
    query_paths = [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.sql')]
    queries = [open(query_path, 'r').read() for query_path in query_paths]
    return queries



def query_serialize_image(query: os.PathLike, db: str = None) -> np.ndarray:
    """Executes a query and serializes the result as an image.

    Args:
        query (os.PathLike): Path to query file.

    Returns:
        bytes: Serialized image.
    """
    def _build_img_from_df(df: pd.DataFrame):
        mx = df.x.max() + 1
        my = df.y.max() + 1
        
        r = df[df.rgb == 0].val.to_numpy()\
            .reshape(my, mx)
        g = df[df.rgb == 1].val.to_numpy()\
            .reshape(my, mx)
        b = df[df.rgb == 2].val.to_numpy()\
            .reshape(my, mx)
        
        return Image.fromarray(np.dstack((r, g, b)).astype(np.uint8), mode='RGB')

    img_dataframe = pd.DataFrame(
        query_db(query, db_file=db),
        columns=['x', 'y', 'z', 'rgb', 'val'],
        )
    img = _build_img_from_df(img_dataframe)
    return img