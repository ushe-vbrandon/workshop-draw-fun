"""
Draw Subarser

Argument parser for draw subcommand.
"""

import argparse
import logging
import os
from typing import Sequence

from draw.query_images import collect_queries, query_serialize_image
from draw.draw import draw_complete_image

logger = logging.getLogger(__name__)


#########################
## Draw Action Classes ##
#########################

class DrawAllAction(argparse.Action):
    
    def __init__(self, option_strings: Sequence[str], dest, nargs=None, **kwargs) -> None:
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super().__init__(option_strings, dest, **kwargs)
        

    def __call__(self, parser, namespace, values, option_string=None):
        
        print('%r %r %r' % (namespace, values, option_string))
        values = self._check_init(values)
        setattr(namespace, self.dest, values)
        
        if values:
            print('Collecting Queries')
            queries = collect_queries(os.getcwd())
            print('Querying Database')
            images = []
            for query in queries:
                images.append(
                    query_serialize_image(query)
                )
            print('Rendering Image')
            draw_complete_image(images)




    def _check_init(self, value):
        return True



###########################
## Integration Functions ##
###########################

def register_draw_subparser(subparsers):
    parser = subparsers.add_parser('draw', help=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--all', 
        action=DrawAllAction, 
        help='Configure whether to run all queries or not.',
        default=True)
    ## Following is a placeholder for the query directory.  Not in use yet.
    parser.add_argument(
        '--dir',
        help='Directory containing query files.',
        default='')