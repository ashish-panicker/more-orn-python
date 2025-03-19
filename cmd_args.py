"""Working with command line arguments: [argparse]"""
import logging
import argparse

"""Create a logger for this python module"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Simple user detail argument parser")

parser.add_argument("name", type=str, help="Name of the user")
parser.add_argument("--email", type=str, help="Email of the user")
parser.add_argument("--locked", action="store_true", help="Account status of the user")

args = parser.parse_args()

logger.debug(f"Args: {args}")