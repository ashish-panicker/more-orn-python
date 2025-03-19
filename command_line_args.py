"""
  Working with command line arguments
  Option 1: use the sys module
"""
import logging
import sys

"""Create a logger for this python module"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

"""
  argv list is provided by the sys module, contains the command line arguments
  first argument is the name of the python file
"""
numbers = sys.argv[1:]

logger.debug(f"cmd args: {numbers}")

logger.debug("Calculating the sum of all numbers")
sum = 0
for number in numbers:
  try:
    sum += int(number)
  except ValueError as ve:
    logger.critical(f"Error: {ve}")

logger.info(f"Sum = {sum}")