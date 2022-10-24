"""
Draw Fun SQL

Argument parser and entry point for draw fun sql.
"""

import argparse
import logging
import os

from draw import register_draw_subparser

logger = logging.getLogger(__name__)

######################
### RunTime Config ###
######################

DEBUG = True
VERSION = '0.0.1'

def _build_config() -> dict:
    """Build config."""
    def _get_env_var(key: str, default: str) -> str:
        """Get environment variable."""
        if not DEBUG:
            return os.environ.get(key)
        return os.environ.get(key, default)

    return {
        'output_file_name': _get_env_var('DRAWFUN_OUTPUT_FILENAME', 'draw-fun.png'),
        'timeout': _get_env_var('TIMEOUT', 300),
    }


config = _build_config()

#########################
### Utility Functions ###
#########################

def _log(message: str, log_level: str = 'info') -> str:
    """Log message."""
    if log_level == 'info':
        logger.info(message)
    elif log_level == 'debug':
        logger.debug(message)
    elif log_level == 'warning':
        logger.warning(message)
    elif log_level == 'error':
        logger.error(message)
    print(message)
    return message



def _validate_config(config: dict) -> None:
    """Validate config."""
    for key, value in config.items():
        if not value:
            raise ValueError(f'Config {key} is not set.')



def _build_parser() -> argparse.ArgumentParser:
    """Build parser."""
    
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='UDRC CLI')
    parser.add_argument('--debug', action='store_true', help='Debug mode', default=DEBUG)
    parser.add_argument('--version', action='version', version=VERSION)

    # Create subparsers registry
    subparsers = parser.add_subparsers(help='sub-command help')

    # Register subparsers
    register_draw_subparser(subparsers)

    return parser


#####################
### Main Function ###
#####################

def main(*args, **kwargs) -> None:
    print(f"Debug: {kwargs['debug']}")
    print(f'Config: {config}')



if __name__ == '__main__':

    # Build parser
    parser = _build_parser()    
    
    # Parse arguments
    args = parser.parse_args()
    
    # Set debug mode & validate config
    if args.debug:
        DEBUG = True
    _validate_config(config)

    # Run main function
    main(debug=DEBUG, config=config)